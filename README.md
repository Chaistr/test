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
4. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

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

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
