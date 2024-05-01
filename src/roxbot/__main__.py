""" main entry point for roxbot. """

from roxbot import __version__


def main() -> None:
    """main entry point for roxbot."""
    print(f"Hello from roxbot version: {__version__}!")


if __name__ == "__main__":  # pragma: no cover
    main()
