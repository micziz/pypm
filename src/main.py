from os import system
import click

def install(x):
    system(f"curl -sL https://raw.githubusercontent.com/micziz/pypm/main/script/{x}.sh | sh")

@click.command()
@click.option('--package', prompt='The Package Name')
def main(package):
    click.echo(f"Installing: {package}!")
    install(package)


main()