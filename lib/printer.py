from rich.console import Console

console = Console()


class Printer:
    def __init__(self, prefix="[finder]"):
        self.prefix = prefix

    def print(self, message: str):
        console.print(f"[green]{self.prefix}[/green] => {message}")

    def print_error(self, message):
        console.print(f"[red]{self.prefix}[/red] => {message}")

    def print_warning(self, message):
        console.print(f"[yellow]{self.prefix}[/yellow] => {message}")

    # TODO: Format error nicely
    def error(self, error):
        self.print_error(error.args[0])
