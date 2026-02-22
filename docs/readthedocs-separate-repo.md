# Repository Layout and Read the Docs Setup

This documentation repository is intended to be separate from the main
`pytest-dag` source repository.

Recommended layout:

- Code/package repo: `SLR-Software-Solutions-Inc/pytest-dag`
- Docs repo: `SLR-Software-Solutions-Inc/pytest-dag-documentation`

## Why use a separate docs repo

- Cleaner docs contribution workflow
- Docs releases/versioning can move independently
- Non-code contributors can work without touching packaging/release pipeline

## Docs repo structure

Recommended structure for `SLR-Software-Solutions-Inc/pytest-dag-documentation`:

```text
pytest-dag-documentation/
├── .readthedocs.yaml
├── mkdocs.yml
└── docs/
    ├── requirements.txt
    ├── index.md
    ├── installation.md
    ├── usage.md
    ├── comparison.md
    ├── license-validation.md
    └── troubleshooting.md
```

You may also add a small repo-level `README.md` describing that this repository
contains the public docs site for `pytest-dag`.

## Read the Docs setup (`readthedocs.com`)

1. Create/import the `pytest-dag-documentation` repository in Read the Docs.
2. Confirm RTD detects `.readthedocs.yaml`.
3. Build from the default branch (for example, `main`).
4. Verify the generated project URL and badge URL.
5. Add those links to the main code repo `README.md`.

## Main repo README docs badge/link template

After the first RTD build succeeds, patch the main repo `README.md` with the
real RTD project slug/URL.

Template:

```md
[![Docs status](https://app.readthedocs.com/projects/<RTD_ORG_SLUG>/badges/<RTD_PROJECT_SLUG>/?version=latest)](https://<your-docs-domain>/en/latest/)

Documentation: https://<your-docs-domain>/en/latest/
```

If you use the default RTD-hosted domain, it may be something like:

```text
https://pytest-dag.readthedocs.io/en/latest/
```

Use the exact URL shown by Read the Docs after the first successful build.
