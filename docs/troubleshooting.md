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

No. License verification is done entirely locally using an embedded Ed25519
public key. No HTTP requests are made at any point — not at startup, not
during the run, and not at teardown. The plugin works identically on
air-gapped machines and behind firewalls.

## "Free tier: DAG exceeds node/depth limit"

The free tier supports up to 25 DAG nodes and depth 3. If your suite exceeds
these limits:

- Split the suite into smaller independent DAGs, or
- Upgrade to pro: `https://slrsoft.ca/app/pytest-dag/purchase`

## Pro features not activating (HTML report / workers)

Verify the key is set and valid:

```bash
PYTEST_DAG_LICENSE_KEY=pdv2_... pytest --dag-report-out report.html -v
```

If the key is expired or invalid, the plugin silently falls back to free tier.
Run with `PYTEST_DAG_DEBUG=1` to see the exact tier resolved:

```bash
PYTEST_DAG_DEBUG=1 pytest -q 2>&1 | grep "tier"
```
