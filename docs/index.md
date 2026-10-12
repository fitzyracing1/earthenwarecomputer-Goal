# Earthenware Computer Goal

The README describes "a computer that selects all of its own programs". At boot it senses the environment, discovers self-registered programs, scores them against a goal, picks a subset that fits a resource budget, and runs them. It also describes a `server` program on port 8765 (`/status`, `/programs`, `/goal`, `/results`).

**State of the repo:** `main.py` imports `core.computer.SelfSelectingComputer` and `core.terminal.Terminal`, but `core/` and `programs/` contain only empty `__init__.py` files. **The documented commands (`python3 main.py --terminal`) cannot run from this repo as committed.** The program modules described in the README are not present.

Files: `main.py`, `core/__init__.py`, `programs/__init__.py`, `docs/index.html` (site). The repo has no tests and no LICENSE file.

Copyright (c) 2026 Joshua Almeida
