# Troubleshooting

## Pytest shows `dag-<version>` instead of `pytest-dag-<version>`

This is normal. Pytest shortens plugin names in output by dropping the
`pytest-` prefix.

## No plugin debug logs appear

If `PYTEST_DAG_DEBUG=1` is set but no `pytest-dag [DEBUG]` lines appear, the
plugin may not be loaded in that process.

Check plugin loading:

```bash
python -m pytest --trace-config -q
```

Force-load plugin (useful for debugging):

```bash
python -m pytest -p pytest_dag.plugin ...
```

## Virtualenv activated but `pytest` still points to a global binary

Use:

```bash
python -m pytest ...
```

This avoids shell path/alias issues and guarantees the current interpreter is
used.
