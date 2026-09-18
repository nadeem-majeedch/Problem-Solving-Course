# Python & Terminal Setup (Student Guide)

You need this done **before Lecture 04**. It takes about 20 minutes.

## 1. Install Python

Install Python 3.10 or newer from the installer your institution provides, or
search the web for "python download" and use the official result for your
operating system.

- **Windows**: run the installer; on the first screen tick **Add Python to
  PATH**, then Install Now.
- **macOS**: use the installer and follow the defaults.
- **Linux**: most distributions include Python 3 already; check with the
  command below.

Verify in a terminal (Terminal on macOS/Linux, PowerShell or CMD on Windows):

```bash
python3 --version
# Windows may use:
python --version
```

You should see something like `Python 3.12.4`. Any 3.10+ is fine.

## 2. Pick an editor

Pick **one** and stay with it all semester:

| Option | Good for |
| --- | --- |
| IDLE (installs with Python) | simplest start; run with F5 |
| VS Code (free; search "VS Code download") | comfortable editing + terminal in one window |
| Any plain-text editor + terminal | minimal, always works |

In VS Code, install the official Python extension (search "Python" in the
Extensions panel and take the one published by the Python Software
Foundation / Microsoft-distributed build).

## 3. Run your first program

Create a file `hello.py` containing:

```python
print("hello from cs-ds problem solving")
```

In a terminal opened in the same folder:

```bash
python hello.py      # or: python hello.py
```

Expected output:

```
hello from cs-ds problem solving
```

## 4. The interactive console

Typing `python` (no file name) opens the **interactive console** — a
calculator on steroids where each line runs immediately:

```python
>>> 2 + 3 * 4
14
>>> "cs" * 3
'cscscs'
>>> exit()
```

Use it to test tiny ideas before putting them in a file. This habit pays off
in every case study of the course.

## 5. Minimal terminal vocabulary

| Command | Meaning |
| --- | --- |
| `cd folder` | move into `folder` |
| `cd ..` | move one folder up |
| `dir` / `ls` | list files (Windows / macOS-Linux) |
| `python3 file.py` | run a Python file |
| `python` | open the interactive console |

## 6. Troubleshooting

- **`python` not found (macOS/Linux)**: use `python3`; on Windows, if that opens the Microsoft
  Store, the PATH box was missed — reinstall and tick it.
- **`can't open file 'hello.py'`**: your terminal is in a different folder;
  `cd` to the folder first (or use your editor's "open terminal here").
- **Syntax errors everywhere**: check you are editing `.py` files as plain
  text, not saving them as `.py.txt` from a word processor.

If stuck, bring the exact error text to the next lecture — reading error
messages is a course skill, and we will practise it in Lecture 07.
