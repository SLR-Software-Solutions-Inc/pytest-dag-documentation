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

## Does pytest-dag make network calls?

No. License verification is done entirely locally — no HTTP requests are made
at any point, not at startup, not during the run, and not at teardown. The
plugin works identically on air-gapped machines and behind firewalls.

## "Free tier: DAG exceeds node/depth limit"

The free tier supports up to 25 DAG nodes and depth 5. If your suite exceeds
these limits:

- Split the suite into smaller independent DAGs, or
- Upgrade to pro: `https://slrsoft.ca/app/pytest-dag/purchase`

## Pro features not activating (HTML report / workers)

Verify the key is set correctly:

```bash
PYTEST_DAG_LICENSE_KEY=<your-license-key> pytest --dag-report-out report.html -v
```

If the key is expired or invalid the plugin falls back to free tier silently.
Contact `support@slrsoft.ca` if a valid key is not activating pro features.
