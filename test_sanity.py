"""
Sanity check the tests in the suite.

To run this, unless you otherwise know what you're doing:

    * install ``pipx`` (see its documentation page)
    * install nox via ``pipx install nox``
    * run ``nox`` in the root of this repository
"""

from pathlib import Path
import json

from jsonschema.validators import validator_for
import pytest

ROOT = Path(__file__).parent
TESTS = ROOT / "tests"
SCHEMA = json.loads(ROOT.joinpath("test-schema.json").read_text())


def test_schema_is_valid():
    validator_for(SCHEMA).check_schema(SCHEMA)


@pytest.mark.parametrize("test_path", TESTS.rglob("*.json"))
def test_tests_are_valid(test_path):
    try:
        test = json.loads(test_path.read_text())
    except json.JSONDecodeError:
        assert False, f"{test_path} contains invalid JSON"
    else:
        validator_for(SCHEMA)(SCHEMA).validate(test)
