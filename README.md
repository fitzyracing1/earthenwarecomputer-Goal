# Earthenware Computer Goal

**A computer that selects all of its own programs.**

At every boot the machine:

1. Senses its live environment (CPU, memory, observed needs)
2. Discovers every program that has *self-registered* by announcing its capabilities
3. Scores each program against the current high-level goal
4. Selects a coherent subset that fits inside a resource budget
5. Loads *only* those programs
6. Runs them cooperatively

There is no hard-coded list of required software.  
The only permanent pieces are the discovery + selection kernel.  
Everything else is chosen.

## Quick start

```bash
git clone https://github.com/fitzyracing1/earthenwarecomputer-Goal.git
cd earthenwarecomputer-Goal
python3 main.py --terminal      # interactive terminal (recommended)
python3 main.py -t              # same as --terminal
```

Examples of goals:

- `"become a useful, self-monitoring, self-improving computer that reports its own state"`
- `"connect to the internet, use a browser and report what I find online"`
- `"run an http server and serve my status to the network"`
- `"use the gpu for heavy tensor compute and matrix acceleration"`

## Live server

When the `server` program is selected it listens on port **8765**:

- `http://127.0.0.1:8765/` — HTML status page
- `/status` `/programs` `/goal` `/results` — JSON API

## GitHub Pages

Public site lives in `/docs`. Enable in repo Settings → Pages → Deploy from branch `main` / `/docs`.

## Design principles

- Minimal kernel
- Programs are self-describing
- Selection is goal + environment driven
- Resource-aware
- Capable of growing its own software surface

## Documentation

- In-repo docs: [docs/](docs/index.md)
- Wiki: [https://github.com/fitzyracing1/earthenwarecomputer-Goal/wiki](https://github.com/fitzyracing1/earthenwarecomputer-Goal/wiki)
