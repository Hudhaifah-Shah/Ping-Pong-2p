# Ping Pong

A classic 2-player Ping Pong game built with Python. This project highlights Object-Oriented Programming (OOP) principles, event-driven keyboard controls, and GUI integration using Python's built-in `turtle` and `tkinter` modules.

## Key Features
- **Dynamic Win Conditions:** Asks players for a target score before launching the game.
- **Local Two-Player Support:** Simultaneous key-listening allowing fluid movement for both players.

## Controls

| Player | Movement | Keys |
| :--- | :--- | :--- |
| **Player 1 (Left)** | Move Up / Down | `W` / `S` |
| **Player 2 (Right)** | Move Up / Down | `Up Arrow` / `Down Arrow` |

## Computer Science Concepts Applied
- **Object-Oriented Design (OOP):** Decoupled entities into specialized classes (`Paddle`, `Ball`, `Scoreboard`, and `Border`) to enforce encapsulation and code reusability.
- **Event-Driven Architecture:** Used asynchronous key-press listeners (`screen.onkey`) to handle real-time user inputs without blocking the main game loop.
- **State Management & Tkinter Integration:** Leveraged `screen.numinput` to collect target score state before starting the main game execution loop.

### Prerequisites
- Python 3.x (Includes `turtle` and `tkinter` standard libraries)
