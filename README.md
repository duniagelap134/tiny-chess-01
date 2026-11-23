# tiny-chess-01

An original chess engine in under 4 KB of Python, written for make.fun's
"Build the strongest chess engine in 4 KB of Python" bounty.

- 120-char string board, alpha-beta with iterative deepening to a fixed node budget
- Quiescence over captures and check evasions
- Best-move-only transposition table for move ordering, MVV ordering
- Tapered material + piece-square evaluation (middlegame/endgame, king centralisation); fully deterministic, no clock, no randomness

`main.py` is the whole engine: Python 3.13 standard library only. It talks
to the trial env at `MAKEFUN_ENV_URL` and plays the house gauntlet.
