# License Validation

`pytest-dag` can validate licensing before test collection starts.

## Endpoints used by the plugin

- `GET /licenses/feature-flag`
- `POST /licenses/validate` (only when paywall is enabled)

## Environment variables

- `PYTEST_DAG_LICENSE_ENDPOINT`
- `PYTEST_DAG_LICENSE_KEY`
- `PYTEST_DAG_DEBUG=1`
- `PYTEST_DAG_USER_AGENT` (optional override)

## Local backend example

```bash
export PYTEST_DAG_LICENSE_ENDPOINT=http://127.0.0.1:8003
export PYTEST_DAG_DEBUG=1
python -m pytest -v -rs
```

Use `http://` for a local plain HTTP service. If you use `https://` against a
non-TLS local server, the backend may log invalid HTTP request warnings.

## Debug output

With `PYTEST_DAG_DEBUG=1`, the plugin logs:

- The resolved license endpoint
- The exact feature-flag and validate URLs
- Request method and timeout
- Response status and a short body preview
