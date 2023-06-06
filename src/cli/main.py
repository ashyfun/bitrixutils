import click

from bitrixutils.litra import Define, AdminPasswordh
from bitrixutils.litra.exceptions import LitraException


@click.group()
def cli():
    pass


@click.command()
@click.option('--days', default=30, help='Days before trial expires.')
def genlitra(days):
    """Generate hashes (30 days by default)."""

    define = Define(days)
    admin_passwordh = AdminPasswordh(days)

    click.echo(define.encode())
    click.echo(admin_passwordh.encode())


@click.command()
@click.argument('target', nargs=-1, required=True)
def declitra(target):
    """Decode hashes."""

    res = ''
    define = Define()
    admin_passwordh = AdminPasswordh()
    for v in target:
        try:
            res = define.decode(v)
        except LitraException:
            try:
                res = admin_passwordh.decode(v)
            except LitraException as e:
                res = str(e)
        finally:
            click.echo('{} ... {}'.format(v, res))


cli.add_command(genlitra)
cli.add_command(declitra)

if __name__ == '__main__':
    cli()
