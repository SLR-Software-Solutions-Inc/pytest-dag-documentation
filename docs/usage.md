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

## YAML DAG (for larger test suite, where it really shine!)

For larger suites, define dependencies in a YAML file instead of — or in
addition to — inline markers. This keeps test files clean and centralises
the dependency graph.

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

Marker dependencies and YAML dependencies are merged. You can use both in
the same suite.

## CLI reference

| Option | Tier | Default | Description |
| ------ | ---- | ------- | ----------- |
| `--dag-block-on-outcomes OUTCOMES` | Free+ | `fail` | Comma-separated outcomes that block dependents: `fail`, `skip`, `xfail`, `error` |
| `--dag-print-graph` | Free+ | off | Print DAG order and edges after collection |
| `--pytest-dag-license-key KEY` | — | unset | Provide license key on the command line |
| `--pytest-dag-license-key-file PATH` | — | unset | Read license key from a file |
| `--dag-workers N` | **Pro** | 1 | Run DAG-independent tests in parallel with N workers |
| `--dag-report-out PATH` | **Pro** | unset | Write an interactive HTML DAG report to PATH |

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

## Viewing skip reasons

Pass `-v -rs` to see the exact reason each test was skipped:

```bash
pytest -v -rs
```

Example output:

```text
SKIPPED [2] pytest-dag: blocked by test_demo.py::test_login (FAILED)
SKIPPED [1] test_demo.py:104: feature not yet implemented
```

The `pytest-dag: blocked by` prefix identifies skips triggered by the
dependency graph, distinct from skips in your own test code.

## HTML report (Pro)

Generate an interactive single-page report after a run:

```bash
pytest --dag-report-out report.html
```

The report includes:
- **Overview** — pass/fail/skip counts and animated stat cards
- **DAG Graph** — interactive pan/zoom flowchart of node dependencies, colour-coded by outcome
- **Results** — filterable, searchable, sortable test table

## Parallel workers (Pro)

Run tests whose DAG dependencies are already satisfied in parallel:

```bash
pytest --dag-workers 4
```

DAG ordering is enforced — dependents still wait for their dependencies to
complete before starting.

## pytest-xdist compatibility

On the **free tier**, `pytest-dag` disables `pytest-xdist` parallel execution
(`-n`) automatically when detected and prints a warning. Tests run
sequentially with full DAG enforcement.

On the **pro tier**, `--dag-workers N` provides native DAG-aware parallelism
and xdist is not disabled.

If xdist is installed but `-n` is not passed, behaviour is unchanged on both
tiers.
