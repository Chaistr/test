> 中文版本请见 [README_zh.md](README_zh.md)

# Sample Application

A sample Python application with layered entry points, CLI argument parsing, and utility modules.  
It demonstrates a simple structure for building command-line tools with Python and includes a classic Snake game.

## Installation

1. Ensure you have Python 3.8+ installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/Chaistr/test.git
   cd test
   ```
3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. No external dependencies required. The project uses only the Python standard library.

## Usage

### Snake Game

Run the classic Snake game:

```bash
python main.py
```

**Controls:**
- **Arrow keys** or **WASD** to move the snake
- **Q** to quit the game

The snake moves on a 20×15 board. Eat the `*` (food) to grow and increase your score. Colliding with walls or your own body ends the game.

### CLI Tool

Run the command-line example tool:

```bash
python app.py --name YourName
```

Example output:
```
Running the application...
Received arguments: Namespace(name='YourName', verbose=False)
```

Available options:
- `--name NAME`   Name to greet (default: World)
- `--verbose`     Enable verbose output

You can also use Python's `-m` flag:
```bash
python -m __main__ --name Developer
```

## Modules

### `main.py`
Entry point for the Snake game. Handles keyboard input, rendering, and the main game loop.

### `snake.py`
Defines the `Snake` class, including movement, growth, collision detection, and direction control.

### `app.py`
Core application module. Contains the `run_app(args)` function which prints a welcome message and the received arguments.

### `cli.py`
Command-line interface module using `argparse`. Provides `parse_args(args=None)` for parsing `--name` and `--verbose`.

### `__main__.py`
Enables `python -m` execution by importing `main` from `main.py` and calling it.

### `math_utils.py`
Utility module containing a `factorial(n)` function with type and value checking.