# pytest-dag Documentation

This repository hosts the public user documentation for `pytest-dag`.

- Product/source repository: `SLR-Software-Solutions-Inc/pytest-dag`
- Docs hosting target: Read the Docs (`readthedocs.com`)

## Local Preview

```bash
python -m pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html
python -m http.server -d docs/_build/html 8000
```

## Read the Docs

This repo is configured with:

- `.readthedocs.yaml`
- `docs/conf.py`

Import this repository into Read the Docs and build from your default branch.

After the first successful build, copy the final docs URL and badge URL into the
main project README in `SLR-Software-Solutions-Inc/pytest-dag`.
