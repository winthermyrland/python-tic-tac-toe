---
tags:
  - "#dev"
  - "#project"
created: 2026-04-14
status: active
---

## Purpose
A simple two-player GUI Tic Tac Toe game built with Python and tkinter. No external dependencies required.

## Stack
- **Language:** Python 3.13
- **GUI:** tkinter (stdlib)
- **Dependencies:** none

## Architecture
Single-file application — all logic lives in `main.py`.

| Component | Responsibility |
|---|---|
| `TicTacToe` class | Game state, UI construction, event handling |
| `_build_ui()` | Assembles status bar, grid, and restart button |
| `_on_cell_click()` | Handles moves, checks win/draw, advances turn |
| `_check_winner()` | Tests all 8 win lines against current board state |
| `main()` | Entry point — creates root window and starts loop |

## How to run
```
python3 main.py
```

## Features
- Two human players on a single machine (X and O)
- Win detection across all rows, columns, and diagonals
- Winning cells highlighted on victory
- Draw detection when board is full
- Restart button resets the board without closing the window
- Dark colour theme

## Repository
`winthermyrland/python-tic-tac-toe` via `git@github-aurora`
