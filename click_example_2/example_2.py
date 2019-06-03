import click

@click.command()
@click.option('--version', default='1.0.0', help='Who are you?')
def cli(version):
    click.echo(version)
