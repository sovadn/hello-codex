"""Simple greeting module."""

from __future__ import annotations

import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    name = args[0] if args else "World"
    print(greet(name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
