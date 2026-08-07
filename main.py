#!/usr/bin/env python3
"""
Earthenware Computer Goal — main entry point.

A computer that chooses every program it runs.
Use --terminal (or -t) for an interactive command loop.
"""

import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from core.computer import SelfSelectingComputer
from core.terminal import Terminal


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Earthenware Computer Goal — chooses all of its own programs")
    parser.add_argument("--goal", "-g",
        default="become a useful, self-monitoring, self-improving computer that reports its own state",
        help="High-level goal that drives program selection")
    parser.add_argument("--cycles", "-c", type=int, default=2)
    parser.add_argument("--name", default="ECG-Prime")
    parser.add_argument("--terminal", "-t", action="store_true",
        help="Launch interactive terminal instead of one-shot run")
    args = parser.parse_args()

    if args.terminal:
        computer = SelfSelectingComputer(name=args.name, goal=args.goal)
        term = Terminal(computer)
        term.start()
        return

    computer = SelfSelectingComputer(name=args.name, goal=args.goal)
    computer.boot()
    print()
    print(computer.status())
    print()
    computer.run(cycles=args.cycles)
    print()
    print("=== Final status ===")
    print(computer.status())
    print()
    print("For interactive use:  python3 main.py --terminal")


if __name__ == "__main__":
    main()
