# License & Tiers

`pytest-dag` ships with a **freemium model**. No license key is required to
get started. A pro key unlocks additional capabilities.

## Tier comparison

| Feature | Free | Pro |
|---|---|---|
| DAG enforcement | ✓ | ✓ |
| YAML DAG file | ✓ | ✓ |
| Cross-file dependencies | ✓ | ✓ |
| Max DAG nodes | 25 | Unlimited |
| Max DAG depth | 3 | Unlimited |
| Parallel workers (`--dag-workers`) | — | ✓ |
| HTML report (`--dag-report-out`) | — | ✓ |
| Run banner | shown | silent |

## Free tier

No configuration needed. Install and run:

```bash
pip install pytest-dag
pytest
```

A one-line banner is printed on each run to indicate the free tier. Tests run
sequentially. DAGs up to 25 nodes and depth 3 are supported.

## Pro tier

Set the license key via environment variable, CLI flag, or key file.

### Environment variable (recommended for CI)

```bash
export PYTEST_DAG_LICENSE_KEY=pdv2_<payload>.<signature>
pytest --dag-report-out report.html --dag-workers 4
```

### CLI flag

```bash
pytest --pytest-dag-license-key pdv2_<payload>.<signature>
```

### Key file

```bash
pytest --pytest-dag-license-key-file /path/to/key.txt
```

## CI setup

Store the key as a secret in your CI provider and expose it as
`PYTEST_DAG_LICENSE_KEY`. The plugin reads it automatically — no extra flags
needed.

**GitHub Actions / Forgejo Actions:**

```yaml
env:
  PYTEST_DAG_LICENSE_KEY: ${{ secrets.PYTEST_DAG_LICENSE_KEY }}
```

## Purchase or renew

- `https://slrsoft.ca/app/pytest-dag/purchase`

## How verification works

Keys are verified **locally** using an embedded Ed25519 public key. No
network calls are made at any point — the plugin works identically on
air-gapped machines, behind firewalls, and in offline CI environments.

## Support

- `support@slrsoft.ca`
