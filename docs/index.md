# pytest-dag

`pytest-dag` is a pytest plugin that lets tests declare dependencies and run in
dependency-safe order.

It builds a directed acyclic graph (DAG) from markers and/or YAML definitions,
then enforces topological execution and skips blocked dependents with a clear
reason.

Source code repository:

- `SLR-Software-Solutions-Inc/pytest-dag`

## Highlights

- DAG-based test ordering
- Cycle detection at collection time
- Cascading skip behavior (`--dag-block-on`)
- Optional YAML DAG definitions
- License validation with debug logging support
- Automatic xdist guard when `-n` is active

See the other pages for installation, usage, and troubleshooting details.
