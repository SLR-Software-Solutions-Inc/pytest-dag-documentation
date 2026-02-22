# Comparison with `pytest-dependency` and `pytest-order`

This page explains where `pytest-dag` fits relative to two well-known pytest
plugins:

- `pytest-dependency`
- `pytest-order`

These tools solve adjacent problems, and they can be useful in different cases.

## Short version

- Use `pytest-order` when you primarily want explicit ordering (`first`, `last`,
  `before`, `after`, numeric positions).
- Use `pytest-dependency` when you primarily want dependency result tracking and
  skip behavior.
- Use `pytest-dag` when you want a dependency-first workflow that combines graph
  validation, topological ordering, and dependency skip propagation in one
  plugin.

## `pytest-dependency`: strengths and tradeoffs

### What it does well

- Tracks test dependencies
- Skips dependents when prerequisites fail/skip
- Supports naming and scoping for dependency references

### Tradeoffs for larger dependency-heavy suites

- It does not solve execution ordering by itself.
- Suites can require additional ordering logic/plugin configuration if
  collection order does not naturally place prerequisites first.
- Dependency names and scopes add flexibility, but also add setup/debugging
  overhead in larger suites.

## `pytest-order`: strengths and tradeoffs

### What it does well

- Explicit ordering markers (numeric and relative)
- Good fit for "run this before/after that" workflows

### Tradeoffs for dependency-driven test suites

- Ordering is not the same as dependency semantics.
- Blocking/skipping dependents based on upstream outcomes is not its primary
  model.
- For dependency-aware ordering, its docs describe integration with
  `pytest-dependency` (`--order-dependencies`), which introduces multi-plugin
  coordination and only supports static dependency markers for ordering.

## Where `pytest-dag` fits better

`pytest-dag` is designed around the dependency graph itself.

### What `pytest-dag` provides in one plugin

- Marker-based dependencies (`@pytest.mark.dag(depends=...)`)
- Optional YAML DAG file (`dag_file`)
- Topological ordering from declared dependencies
- Cycle detection at collection time
- Missing dependency handling (strict vs lenient)
- Cascading skip behavior configurable via `--dag-block-on`
- Clear skip reasons naming the blocker and outcome

## Practical decision guide

Choose `pytest-dag` when:

- You have prerequisite chains across many tests/files
- You want graph validation and deterministic dependency ordering
- You want a single plugin instead of combining ordering + dependency plugins

Choose `pytest-order` when:

- You only need explicit execution ordering, not dependency semantics

Choose `pytest-dependency` when:

- You mainly need dependency result gating and are comfortable managing
  ordering separately (or collection order is already sufficient)
