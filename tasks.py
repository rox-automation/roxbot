# type: ignore
import os
from click import prompt
from invoke import task

# Constants
CI_IMG = "roxbot-ci"


@task
def clean(ctx):
    """
    Remove all files and directories that are not under version control to ensure a pristine working environment.
    Use caution as this operation cannot be undone and might remove untracked files.

    """

    ctx.run("git clean -nfdx")

    if (
        prompt(
            "Are you sure you want to remove all untracked files? (y/n)", default="n"
        )
        == "y"
    ):
        ctx.run("git clean -fdx")


@task
def lint(ctx):
    """
    Perform static analysis on the source code to check for syntax errors and enforce style consistency.
    """
    ctx.run("ruff check src")
    ctx.run("mypy src")


@task
def test(ctx):
    """
    Run tests with coverage reporting to ensure code functionality and quality.
    """
    ctx.run("pytest --cov=src --cov-report term-missing tests")


@task(pre=[clean])
def build(ctx):
    """
    Build the package after cleaning up previous builds. This ensures that the distribution package is fresh.
    After building, display the contents of the tar.gz package file to verify structure.
    """
    ctx.run("python -m build")
    # Display package contents
    dist_files = next(os.walk("dist"))[2]
    for file in dist_files:
        if file.endswith(".tar.gz"):
            ctx.run(f"tar -tzf dist/{file}")


@task
def ci(ctx):
    """
    Build and run a Docker container locally to simulate the Continuous Integration process. This helps in testing
    the Docker environment before deploying.
    """
    ctx.run(f"docker build -t {CI_IMG} -f docker/ci/Dockerfile .")
    ctx.run(f"docker run {CI_IMG}")
