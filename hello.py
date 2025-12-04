import typer #required library
from typing import Optional


# make func for the script
def greet_user(
    first_name: str,
    last_name: Optional[str] = typer.Option(None, "--last-name", "-l", help="User's last name."),
    is_formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting.")
) -> None:

    """
    Prints a greeting to the user.
    Supports optional last name and formal style.
    """
    if is_formal and last_name:
        print(f"Good day, {first_name} {last_name}!")
    elif is_formal:
        print(f"Good day, {first_name}!")
    else:
        print(f"Hello, {first_name}!")

if __name__ == "__main__": #launching
    typer.run(greet_user)