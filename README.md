# anaconda-learning

Hands-on Anaconda, conda, Jupyter, and Python-for-finance learning experiments.

This project is the first being formalized with the **Grok Harness** (router + Plan-Architect diagnosis completed 2026-07-03).

## Modules (Learning Progression)

| Module | Focus | Key Artifacts |
|--------|-------|---------------|
| `01-first-chart/` | Basic data pull + visualization | `chart.py`, environment.yml |
| `02-jupyter-explore/` | Jupyter notebook basics | `country_explorer.ipynb` |
| `03-finance-101/` | Financial statements, ratios, TVM, stocks, portfolios | Full notebooks/ (with narrative markdown + cleaned hardcodes), scripts/, data/, README.md |
| `04-finance-201/` | Personal finance (budgeting, debt, rent vs buy) + CLI tools | notebooks/, scripts/, data/charts/, README.md |

## Quick Start

Each module manages its own conda environment.

Example (finance-101):

```bash
cd 03-finance-101
conda env create -f environment.yml
conda activate finance-101
jupyter lab
```

See the `README.md` inside `03-finance-101/` and `04-finance-201/` for detailed phases, data descriptions, CLI examples, and chart explanations.

## Current Harness Formalization (Chunk 1+)

This project follows the approved plan from the harness session:

- Registered in grok-harness/config/registry.yaml (stack: data-science-conda-jupyter, rigor: prototype)
- Root hygiene: this README + .gitignore
- Future chunks (see plan.md in session): environment standardization, notebook documentation quality, script robustness + error handling, end-to-end verification

**Process notes** (human-in-the-loop by design):
- All changes go through explicit diagnosis → plan → human review + approval.
- Visibility: registry, plans, command output, and diffs are always surfaced.
- You steer creative direction and high-level decisions. The harness handles structure, verification, and mundane execution.

## Principles We're Applying

- Diagnose before acting
- Explicit trade-offs (documented in the plan)
- Reproducibility and documentation even for learning work
- One chunk at a time with verification gates
- Code quality, error handling at boundaries, and reader-focused docs (drawing from established patterns)

Generated charts are currently committed (trade-off decision logged in plan). Environments are being improved from full pinned exports toward minimal declarative specs.

---

See `/Users/stevenromero/Development/grok-harness/docs/session-handoff-2026-07-03-anaconda.md` and the executed plan for full context.