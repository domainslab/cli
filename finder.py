import typer

from lib.daddy import Daddy
from lib.ai import AI

app = typer.Typer()
daddy = Daddy()


@app.command()
def check_domain(domain: str):
    daddy.print(f"{':white_heavy_check_mark:' if daddy.is_available(domain) else ':cross_mark:'} {domain} is {'NOT ' if not daddy.is_available(domain) else ''}available")


@app.command()
def search(desc: str, page_size=10):
    ai = AI()
    domains = ai.next(desc)
    # TODO: Add `in loop` search asking for feedback
    # Implement chat-like behavior
    for domain in domains:
        check_domain(domain)


if __name__ == "__main__":
    app()
