import click

from ms_annotator.data_validation.validate import validate_metadata


@click.group()
def cli():
    """MS Annotator CLI"""
    pass


@cli.command()
@click.argument("metadata_file", type=click.Path(exists=True))
@click.option("--schema", default="path/to/your/metadata_schema.yaml", help="Path to the schema file")
def validate(metadata_file, schema):
    """Validate a metadata file against a schema."""
    validate_metadata(metadata_file, schema)
    click.echo(f"Validation completed for {metadata_file}")


if __name__ == "__main__":
    cli()
