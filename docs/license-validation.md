# License Validation

`pytest-dag` can validate licensing before test collection starts.

## Endpoints used by the plugin

- `GET /licenses/feature-flag`
- `POST /licenses/validate` (only when paywall is enabled)

## Environment variables

- `PYTEST_DAG_LICENSE_KEY`
- `PYTEST_DAG_DEBUG=1`

## Debug output

With `PYTEST_DAG_DEBUG=1`, the plugin logs:

- The resolved license endpoint
- The exact feature-flag and validate URLs
- Request method and timeout
- Response status and a short body preview
