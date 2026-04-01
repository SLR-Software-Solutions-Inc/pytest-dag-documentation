# pytest-dag

`pytest-dag` is a pytest plugin that lets tests declare dependencies and run in
dependency-safe order.

It builds a directed acyclic graph (DAG) from markers and/or YAML definitions,
then enforces topological execution and skips blocked dependents with a clear
reason.

## Highlights

- DAG-based test ordering
- Cycle detection at collection time
- Cascading skip behavior (`--dag-block-on`)
- Optional YAML DAG definitions
- License-gated usage when required
- xdist safety guard when `-n` is active

See the pages below for installation, setup, license usage, and troubleshooting.

```{toctree}
:maxdepth: 2
:caption: Contents

installation
usage
license-validation
troubleshooting
```
