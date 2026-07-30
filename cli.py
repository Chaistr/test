"""Command-line interface module using argparse."""

import argparse


def parse_args(args=None):
    """Parse command-line arguments.

    Args:
        args: Optional list of arguments (useful for testing).

    Returns:
        argparse.Namespace containing parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="A sample application with layered entry points."
    )
    # Add application-specific arguments here.
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
