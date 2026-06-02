# pytest-dag

`pytest-dag` is a pytest plugin that lets tests declare dependencies and run in
dependency-safe order.

It builds a directed acyclic graph (DAG) from markers and/or YAML definitions,
then enforces topological execution and skips blocked dependents with a clear
reason.

## Highlights

- DAG-based test ordering
- Cycle detection at collection time
- Cascading skip behavior (`--dag-block-on-outcomes`)
- Optional YAML DAG definitions
- Freemium model — works out of the box, pro tier unlocks advanced features
- xdist safety guard on free tier

See the pages below for installation, setup, license usage, and troubleshooting.

```{toctree}
:maxdepth: 2
:caption: Contents

installation
usage
comparison
license-validation
troubleshooting
```
