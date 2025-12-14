import typer #required library
from typing import Optional


# make func for the script
def greet_user(
    first_name: str = typer.Argument(..., help="User's first name."),  # Добавляем Argument для обязательного параметра
    last_name: Optional[str] = typer.Option(None, "--last-name", "-l", help="User's last name."),
    is_formal: bool = typer.Option(False, "--formal", "-f", help="Use formal greeting.")
) -> None:

    """
    Prints a greeting to the user.
    Supports optional last name and formal style.
    """
    greeting = "Good day" if is_formal else "Hello"
    name = f"{first_name} {last_name}" if last_name else first_name
    print(f"{greeting}, {name}!")

if __name__ == "__main__": #launching
    typer.run(greet_user)