from pathlib import Path

from ms_annotator.data_validation.validate import validate_metadata

# Path to the directory where this script is located
base_path = Path(__file__).parent

# Construct relative paths to the data and schema
relative_base_path = base_path.relative_to(base_path)

# Construct paths to the data and schema relative to this script
data_path = relative_base_path / "examples" / "metadata_example.tsv"
schema_path = relative_base_path / "schemas" / "metadata_schema.yaml"

# Validate the metadata
validate_metadata(str(data_path), str(schema_path))
