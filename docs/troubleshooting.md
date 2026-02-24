# Troubleshooting

## Pytest shows `dag-<version>` instead of `pytest-dag-<version>`

This is normal. Pytest shortens plugin names in output by dropping the
`pytest-` prefix.

## Virtualenv activated but `pytest` still points to a global binary

Use:

```bash
python -m pytest ...
```

This avoids shell path/alias issues and guarantees the current interpreter is
used.
