# Installation

## Install from PyPI

```bash
pip install pytest-dag
```

## Verify plugin is available

```bash
python -m pytest --trace-config -q
```

Look for the `pytest-dag` plugin in the plugin list.

## Virtualenv note

If activating a virtualenv still leaves `pytest` pointing to a global binary,
prefer:

```bash
python -m pytest ...
```

This ensures the virtualenv interpreter and installed plugin are used.
