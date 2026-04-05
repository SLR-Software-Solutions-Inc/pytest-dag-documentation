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
| `--dag-strict` / `--no-dag-strict` | strict | Missing dependency → collection error (strict) or skip (lenient) |
| `--dag-block-on OUTCOMES` | `fail` | Comma-separated outcomes that block dependents: `fail`, `skip`, `xfail`, `error` |
| `--dag-dump` | off | Print DAG order and edges after collection |
| `--pytest-dag-license-key KEY` | unset | Provide license key on the command line |
| `--pytest-dag-license-key-file PATH` | unset | Read license key from a file |

Examples:

```bash
# Skip dependents when a dependency fails or is skipped
pytest --dag-block-on fail,skip

# Downgrade missing deps from error to skip
pytest --no-dag-strict

# Show computed DAG after collection
pytest --dag-dump

# Inspect skip reasons
pytest -v -rs
```

## Migrating from pytest-dependency

If you have an existing suite using `pytest.mark.dependency`, use the built-in migration tool to generate a `dag.yaml`.

| Option | Default | Description |
| ------ | ------- | ----------- |
| `--migrate-from-pytest-dependency` | off | Scan for `pytest.mark.dependency` markers, emit `dag.yaml`, then exit |
| `--dag-file-out PATH` | `tests/dag.yaml` | Output path for the generated YAML |
| `--migrate-dry-run` | off | Preview output without writing files |
| `--migrate-write-inplace` | off | Also remove old `pytest.mark.dependency` decorators from source |
| `--migrate-backup-suffix SUFFIX` | `.bak` | Backup suffix when using `--migrate-write-inplace` (empty string disables backups) |
| `--migrate-scope SCOPE` | `auto` | Scope for bare dependency name resolution: `auto`, `module`, `package`, `session`, `class` |
| `--migrate-strict` | off | Unresolved references become errors instead of YAML comments |

```bash
# Preview
pytest --migrate-from-pytest-dependency --migrate-dry-run

# Generate dag.yaml
pytest --migrate-from-pytest-dependency --dag-file-out tests/dag.yaml

# Generate dag.yaml and remove old markers
pytest --migrate-from-pytest-dependency --dag-file-out tests/dag.yaml --migrate-write-inplace
```
