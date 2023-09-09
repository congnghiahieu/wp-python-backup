import click


@click.group()
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(ctx: click.Context, debug):
    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)
    click.echo(ctx)

    ctx.obj["DEBUG"] = debug


@cli.command()
@click.pass_context
def sync(ctx: click.Context):
    click.echo(ctx)
    click.echo(f"Debug is {'on' if ctx.obj['DEBUG'] else 'off'}")


if __name__ == "__main__":
    cli(obj={})
