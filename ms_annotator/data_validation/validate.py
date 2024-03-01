from frictionless import Resource, validate


def validate_metadata(file_path, schema_path):
    # Load the metadata table as a Frictionless resource, specifying TSV format
    resource = Resource(path=file_path, schema=schema_path, format="tsv")

    # Perform validation
    report = validate(resource)

    # Check if there were any validation errors
    if report.valid:
        print("Metadata is valid according to the schema.")
    else:
        print("Validation errors found:")
        for error in report.flatten(["rowPosition", "fieldPosition", "code", "message"]):
            print(error)
