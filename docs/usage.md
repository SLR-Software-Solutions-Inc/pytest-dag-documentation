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

## Useful flags

- `--dag-strict` / `--no-dag-strict`
- `--dag-block-on fail,skip`
- `--dag-dump`
- `-v -rs` (to inspect skip reasons)
