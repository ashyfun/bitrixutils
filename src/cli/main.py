import click

from bitrixutils.litra import Define, AdminPasswordh


@click.group()
def cli():
    pass


@click.command()
@click.option('--days', default=30, help='Days before trial expires.')
def genlitra(days):
    define = Define(days)
    admin_passwordh = AdminPasswordh(days)

    click.echo(define.encode())
    click.echo(admin_passwordh.encode())


cli.add_command(genlitra)

if __name__ == '__main__':
    cli()
