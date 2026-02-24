# License

`pytest-dag` may require a license key before test collection starts,
depending on the current license policy.

## Provide your license key

You can provide the key using any of these methods:

- `PYTEST_DAG_LICENSE_KEY`
- `--pytest-dag-license-key`
- `--pytest-dag-license-key-file`

### Example: environment variable

```bash
export PYTEST_DAG_LICENSE_KEY=pd-XXXX-XXXX-XXXX-XXXX
python -m pytest -v -rs
```

### Example: key file

```bash
pytest --pytest-dag-license-key-file /path/to/key.txt -v -rs
```

## Purchase or renew

- `https://pytest-dag.slrsoft.ca/licenses/purchase`

## Support

- `support@slrsoft.ca`
