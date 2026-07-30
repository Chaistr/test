"""Main entry point for the application."""

from app import run_app
from cli import parse_args


def main():
    """Parse CLI arguments and invoke the core application."""
    args = parse_args()
    run_app(args)


