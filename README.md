> 中文版本请见 [README_zh.md](README_zh.md)

# Sample Application

A sample Python application with layered entry points, CLI argument parsing, and utility modules.  
It demonstrates a simple structure for building command-line tools with Python.

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

Run the main entry point:
```bash
python main.py --name YourName
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

### `app.py`
Core application module. Contains the `run_app(args)` function which prints a welcome message and the received arguments.

### `cli.py`
Command-line interface module using `argparse`. Provides `parse_args(args=None)` to parse command-line arguments like `--name` and `--verbose`.

### `math_utils.py`
Utility module for mathematical functions.

#### `factorial(n)`
Returns the factorial of `n`. Raises `TypeError` if `n` is not an integer, and `ValueError` if `n` is negative.

Example:
```python
from math_utils import factorial

print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

### `snake.py`
Implements the `Snake` class for a classic snake game. The class manages the snake's body, movement, growth, collision detection, and direction changes.

Basic usage:
```python
from snake import Snake

snake = Snake(start_x=5, start_y=5, length=3)
snake.move()
snake.grow()
snake.change_direction((0, -1))
if snake.check_collision(width=20, height=20):
    print("Game Over")
```

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
