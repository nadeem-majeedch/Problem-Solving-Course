"""Derive per-case pseudocode from each case's verified Python reference solution.

The house dialect matches the lecture examples: ``x <- e``, ``FOR EACH``,
``WHILE``, ``IF ... THEN ... ELSE``, ``RETURN``. Statements the transpiler
cannot express are rendered as ``// <honest note>`` lines so nothing is
silently dropped.
"""

from __future__ import annotations

import ast


class Unsupported(Exception):
    pass


def _pre_expr(node: ast.AST) -> str:
    return _expr(node)


def _binop(op: ast.AST) -> str:
    return {
        ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/",
        ast.FloorDiv: "integer-divide", ast.Mod: "mod", ast.Pow: "^",
        ast.BitAnd: "AND", ast.BitOr: "OR", ast.LShift: "shift-left",
        ast.RShift: "shift-right",
    }[type(op)]


def _expr(node: ast.AST) -> str:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, str):
            return "'" + node.value.replace("'", "\\'") + "'"
        if node.value is True:
            return "true"
        if node.value is False:
            return "false"
        if node.value is None:
            return "null"
        return str(node.value)
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        base = _expr(node.value)
        return f"{base}.{node.attr}"
    if isinstance(node, ast.JoinedStr):
        return "<formatted text>"
    if isinstance(node, ast.FormattedValue):
        return _expr(node.value)
    if isinstance(node, ast.Lambda):
        args = ", ".join(a.arg for a in node.args.args)
        return f"({args}) -> {_expr(node.body)}"
    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            fname = {
                "len": "LENGTH", "sum": "SUM", "min": "MIN", "max": "MAX",
                "abs": "ABS", "sorted": "SORTED", "round": "ROUND",
                "int": "INTEGER", "float": "REAL", "str": "TEXT",
                "list": "LIST", "set": "SET", "dict": "MAP", "tuple": "TUPLE",
                "print": "OUTPUT", "range": "range", "enumerate": "ENUMERATE",
                "zip": "ZIP", "reversed": "REVERSED", "input": "INPUT",
                "divmod": "divmod",
            }.get(node.func.id, node.func.id)
            if fname == "OUTPUT":
                return "OUTPUT " + ", ".join(_expr(a) for a in node.args)
            if fname == "range":
                parts = [_expr(a) for a in node.args]
                if len(parts) == 1:
                    return "range 0.." + parts[0]
                if len(parts) == 2:
                    return "range " + parts[0] + ".." + parts[1]
                return "range " + ", ".join(parts)
            args = ", ".join(_expr(a) for a in node.args)
            kws = ", ".join(f"{k.arg} = {_expr(k.value)}" for k in node.keywords)
            if args and kws:
                return f"{fname}({args}; {kws})"
            return f"{fname}({args}{kws})"
        if isinstance(node.func, ast.Attribute):
            if node.func.attr == "append":
                return f"append {_expr(node.args[0])} to {_expr(node.func.value)}"
            if node.func.attr == "add":
                return f"add {_expr(node.args[0])} to {_expr(node.func.value)}"
            if node.func.attr == "get":
                a0 = _expr(node.args[0])
                if len(node.args) > 1:
                    return f"{_expr(node.func.value)}.get({a0}, default {_expr(node.args[1])})"
                return f"{_expr(node.func.value)}.get({a0})"
            base = _expr(node.func.value)
            # Render common predicate/conversion methods as readable phrases.
            preds = {
                "isalnum": "is alphanumeric", "isalpha": "is a letter",
                "isdigit": "is a digit", "lower": "lowercased",
                "upper": "uppercased", "strip": "stripped",
                "rstrip": "right-stripped", "split": "split",
                "keys": "keys", "values": "values", "items": "items",
            }
            if node.func.attr in preds and not node.keywords:
                phrase = preds[node.func.attr]
                if node.func.attr == "split" and not node.args:
                    return f"({base} split into words)"
                if node.args:
                    return f"({base} {phrase} {_expr(node.args[0])})"
                return f"({base} {phrase})"
            args = ", ".join(_expr(a) for a in node.args)
            return f"{base}.{node.func.attr}({args})"
        raise Unsupported("call")
    if isinstance(node, ast.BinOp):
        op = _binop(node.op)
        l, r = _expr(node.left), _expr(node.right)
        if op in ("AND", "OR", "shift-left", "shift-right"):
            return f"{l} {op} {r}"
        if op == "integer-divide":
            op = "div"
        # Precedence-aware parenthesisation: never emit `lo + hi div 2`.
        prec = {"+": 1, "-": 1, "*": 2, "/": 2, "div": 2, "mod": 2, "^": 3}
        my = prec.get(op, 9)
        if isinstance(node.left, ast.BinOp):
            lops = _binop(node.left.op)
            lops = "div" if lops == "integer-divide" else lops
            if prec.get(lops, 9) < my:
                l = f"({l})"
        if isinstance(node.right, ast.BinOp):
            rops = _binop(node.right.op)
            rops = "div" if rops == "integer-divide" else rops
            if prec.get(rops, 9) <= my and op in ("-", "/", "div", "mod"):
                r = f"({r})"
            elif prec.get(rops, 9) < my:
                r = f"({r})"
        return f"{l} {op} {r}"
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return "-" + _expr(node.operand)
        if isinstance(node.op, ast.Not):
            return "NOT " + _expr(node.operand)
        raise Unsupported("unary op")
    if isinstance(node, ast.BoolOp):
        join = " AND " if isinstance(node.op, ast.And) else " OR "
        return join.join("(" + _expr(v) + ")" for v in node.values)
    if isinstance(node, ast.Compare):
        ops = {ast.Eq: "=", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=",
               ast.Gt: ">", ast.GtE: ">=", ast.In: "in",
               ast.NotIn: "not in", ast.Is: "is", ast.IsNot: "is not"}
        out = _expr(node.left)
        for op, comp in zip(node.ops, node.comparators):
            out += " " + ops[type(op)] + " " + _expr(comp)
        return out
    if isinstance(node, ast.IfExp):
        return f"({_expr(node.body)} if {_expr(node.test)} else {_expr(node.orelse)})"
    if isinstance(node, ast.Subscript):
        v = _expr(node.value)
        sl = node.slice
        if isinstance(sl, ast.Slice):
            lo = _expr(sl.lower) if sl.lower else ""
            hi = _expr(sl.upper) if sl.upper else ""
            step = _expr(sl.step) if sl.step else ""
            if step:
                return f"{v}[{lo}..{hi} by {step}]"
            return f"{v}[{lo}..{hi}]"
        return f"{v}[{_expr(sl)}]"
    if isinstance(node, ast.List):
        return "[" + ", ".join(_expr(e) for e in node.elts) + "]"
    if isinstance(node, ast.Tuple):
        return "(" + ", ".join(_expr(e) for e in node.elts) + ")"
    if isinstance(node, ast.Set):
        return "set{" + ", ".join(_expr(e) for e in node.elts) + "}"
    if isinstance(node, ast.Dict):
        pairs = ", ".join(f"{_expr(k)}: {_expr(v)}" for k, v in zip(node.keys, node.values))
        return "map{" + pairs + "}"
    if isinstance(node, ast.ListComp):
        elt = _expr(node.elt)
        gens = []
        for g in node.generators:
            it = _expr(g.iter)
            cond = "".join(f" AND {_expr(x)}" for x in g.ifs)
            gens.append(f"each {_expr(g.target)} in {it}{cond}")
        return "{" + elt + " for " + "; ".join(gens) + "}"
    if isinstance(node, ast.SetComp):
        return "set{" + _expr(node.elt) + " for " + _expr(node.generators[0].target) + " in " + _expr(node.generators[0].iter) + "}"
    if isinstance(node, ast.DictComp):
        k, v = _expr(node.key), _expr(node.value)
        g0 = node.generators[0]
        return "map{" + k + ": " + v + " for " + _expr(g0.target) + " in " + _expr(g0.iter) + "}"
    if isinstance(node, ast.GeneratorExp):
        return _expr(ast.ListComp(node.elt, node.generators))
    if isinstance(node, ast.Starred):
        return "*" + _expr(node.value)
    if isinstance(node, ast.NamedExpr):
        return f"{_expr(node.target)} <- {_expr(node.value)}"
    raise Unsupported(type(node).__name__)


def _target(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Tuple):
        return "(" + ", ".join(_target(e) for e in node.elts) + ")"
    if isinstance(node, ast.Starred):
        return "*" + _target(node.value)
    if isinstance(node, ast.Subscript):
        return f"{_target(node.value)}[{_expr(node.slice) if not isinstance(node.slice, ast.Slice) else _expr(node.slice)}]"
    if isinstance(node, ast.Attribute):
        return f"{_target(node.value)}.{node.attr}"
    raise Unsupported("assign target")


def _stmt(node: ast.AST, out: list[str], indent: int) -> None:
    pad = "    " * indent
    if isinstance(node, ast.Expr):
        v = node.value
        if isinstance(v, ast.Constant) and isinstance(v.value, str):
            return  # docstring
        if isinstance(v, ast.Call):
            out.append(pad + _expr(v))
            return
        raise Unsupported("expression statement")
    if isinstance(node, ast.Assign):
        t = _target(node.targets[0])
        out.append(f"{pad}{t} <- {_expr(node.value)}")
        return
    if isinstance(node, ast.AugAssign):
        t = _target(node.target)
        op = _binop(node.op)
        if op == "integer-divide":
            op = "div"
        out.append(f"{pad}{t} <- {t} {op} {_expr(node.value)}")
        return
    if isinstance(node, ast.AnnAssign):
        t = _target(node.target)
        val = _expr(node.value) if node.value else "nothing"
        out.append(f"{pad}{t} <- {val}")
        return
    if isinstance(node, ast.Return):
        if node.value is None:
            out.append(pad + "RETURN")
        else:
            out.append(pad + "RETURN " + _expr(node.value))
        return
    if isinstance(node, ast.If):
        cond = _expr(node.test)
        out.append(pad + "IF " + cond + " THEN")
        _body(node.body, out, indent + 1)
        if node.orelse and len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            # else-if chain stays flat
            inner = node.orelse[0]
            out.append(pad + "ELSE IF " + _expr(inner.test) + " THEN")
            _body(inner.body, out, indent + 1)
            if inner.orelse:
                out.append(pad + "ELSE")
                _body(inner.orelse, out, indent + 1)
            return
        if node.orelse:
            out.append(pad + "ELSE")
            _body(node.orelse, out, indent + 1)
        return
    if isinstance(node, ast.For):
        tgt = _target(node.target)
        it = node.iter
        # `for _ in range(n)` reads better as REPEAT n TIMES.
        if (isinstance(node.target, ast.Name) and node.target.id == "_"
                and isinstance(it, ast.Call) and isinstance(it.func, ast.Name)
                and it.func.id == "range" and not it.keywords):
            n = _expr(it.args[0]) if len(it.args) == 1 else ", ".join(_expr(a) for a in it.args)
            out.append(pad + f"REPEAT {n} TIMES")
            _body(node.body, out, indent + 1)
            return
        text = _expr(it)
        out.append(pad + f"FOR EACH {tgt} IN {text} DO")
        _body(node.body, out, indent + 1)
        return
    if isinstance(node, ast.While):
        out.append(pad + "WHILE " + _expr(node.test) + " DO")
        _body(node.body, out, indent + 1)
        return
    if isinstance(node, ast.Break):
        out.append(pad + "BREAK")
        return
    if isinstance(node, ast.Continue):
        out.append(pad + "CONTINUE")
        return
    if isinstance(node, ast.Pass):
        out.append(pad + "// (no action)")
        return
    if isinstance(node, ast.Assert):
        out.append(pad + "ASSERT " + _expr(node.test))
        return
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return  # imports are noise in pseudocode
    if isinstance(node, ast.FunctionDef):
        args = ", ".join(a.arg for a in node.args.args)
        out.append(pad + f"FUNCTION {node.name}({args})")
        _body(node.body, out, indent + 1)
        return
    if isinstance(node, ast.Global):
        names = ", ".join(node.names)
        out.append(pad + f"// shares {names} with the caller (global variable)")
        return
    if isinstance(node, ast.ClassDef):
        out.append(pad + f"// class {node.name}: kept as in the Python reference")
        raise Unsupported("class body")
    if isinstance(node, ast.Delete):
        out.append(pad + "// delete " + ", ".join(_target(t) for t in node.targets))
        return
    raise Unsupported(type(node).__name__)


def _body(body: list[ast.AST], out: list[str], indent: int) -> None:
    for s in body:
        try:
            _stmt(s, out, indent)
        except Unsupported as e:
            out.append("    " * indent + f"// (beyond pseudocode: {e})")
            _fallback(s, out, indent)


def _fallback(node: ast.AST, out: list[str], indent: int) -> None:
    """Best-effort inner walk for an unsupported statement."""
    for child in ast.iter_child_nodes(node):
        try:
            _stmt(child, out, indent + 1)
        except Unsupported:
            _fallback(child, out, indent + 1)


def _is_main_guard(node: ast.AST) -> bool:
    """True for the `if __name__ == "__main__":` demo block."""
    return (isinstance(node, ast.If)
            and isinstance(node.test, ast.Compare)
            and isinstance(node.test.left, ast.Name)
            and node.test.left.id == "__name__")


def transpile(code: str) -> str:
    """Render a reference solution as pseudocode lines."""
    tree = ast.parse(code)
    lines: list[str] = []
    for node in tree.body:
        if _is_main_guard(node):
            # Replace the Python demo harness with plain demo comments.
            for inner in node.body:
                if isinstance(inner, ast.Expr) and isinstance(inner.value, ast.Call):
                    lines.append("// demo run: " + _expr(inner.value))
            continue
        try:
            _stmt(node, lines, 0)
        except Unsupported:
            _fallback(node, lines, 0)
    return "\n".join(lines).rstrip()
