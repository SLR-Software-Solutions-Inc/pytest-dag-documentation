# Usage

## Basic marker usage

```python
import pytest

def test_login():
    assert True

@pytest.mark.dag(depends=["test_login"])
def test_profile():
    assert True
```

## Multiple dependencies

```python
@pytest.mark.dag(depends=["test_login", "test_db_connect"])
def test_dashboard():
    assert True
```

## Full nodeid (cross-file)

```python
@pytest.mark.dag(depends=["tests/auth/test_auth.py::test_login"])
def test_profile():
    assert True
```

## YAML DAG

`pyproject.toml`:

```toml
[tool.pytest.ini_options]
dag_file = "tests/dag.yaml"
```

`tests/dag.yaml`:

```yaml
nodes:
  - id: tests/test_flow.py::test_a
  - id: tests/test_flow.py::test_b
    depends: [tests/test_flow.py::test_a]
```

## CLI reference

| Option | Default | Description |
| ------ | ------- | ----------- |
| `--dag-block-on-outcomes OUTCOMES` | `fail` | Comma-separated outcomes that block dependents: `fail`, `skip`, `xfail`, `error` |
| `--dag-print-graph` | off | Print DAG order and edges after collection |
| `--pytest-dag-license-key KEY` | unset | Provide license key on the command line |
| `--pytest-dag-license-key-file PATH` | unset | Read license key from a file |

Examples:

```bash
# Skip dependents when a dependency fails or is skipped
pytest --dag-block-on-outcomes fail,skip

# Show computed DAG after collection
pytest --dag-print-graph

# Inspect skip reasons
pytest -v -rs
```

## Migrating from pytest-dependency

If you have an existing suite using `pytest.mark.dependency`, use the built-in
migration tool to generate a `dag.yaml` and remove old markers in one step.

| Option | Default | Description |
| ------ | ------- | ----------- |
| `--migrate-from-pytest-dependency` | off | Run preflight validation, emit `dag.yaml`, remove `pytest.mark.dependency` markers from source, then exit |
| `--dag-file-out PATH` | `tests/dag.yaml` | Output path for the generated YAML |
| `--migrate-dry-run` | off | Preview output without writing files |

```bash
# Preview
pytest --migrate-from-pytest-dependency --migrate-dry-run

# Run full migration (writes dag.yaml, removes old markers)
pytest --migrate-from-pytest-dependency --dag-file-out tests/dag.yaml
```
