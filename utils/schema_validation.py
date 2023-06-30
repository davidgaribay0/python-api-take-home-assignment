import json
import os

from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate


def is_valid_schema(schema_file, response_body):
    # load the expected schema json file
    schema_path = os.path.join('schemas', schema_file)
    with open(schema_path, 'r') as f:
        data = json.load(f)
    try:
        # if no exceptions are raised, the schema is validated successfully
        validate(instance=response_body, schema=data)
    except ValidationError as e:
        raise e
