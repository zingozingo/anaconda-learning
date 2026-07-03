# anaconda-learning

Hands-on Anaconda, conda, Jupyter, and Python-for-finance learning experiments.

This project is formalized with the **Grok Harness** (see registry entry and handoff for harness context).

## Modules (Learning Progression)

| Module | Focus | Key Artifacts |
|--------|-------|---------------|
| `01-first-chart/` | Basic data pull + visualization | `chart.py`, environment.yml |
| `02-jupyter-explore/` | Jupyter notebook basics | `country_explorer.ipynb` |
| `03-finance-101/` | Financial statements, ratios, TVM, stocks, portfolios | notebooks/ (narrative + "Try This" + constants), scripts/, data/, README.md |
| `04-finance-201/` | Personal finance + CLI tools | notebooks/ (with Try This), scripts/, data/charts/, README.md |

## Quick Start (Exact Commands)

1. Recreate and activate the environment for a module (example for 03):

```bash
cd 03-finance-101
conda env create -f environment.yml
conda activate finance-101
```

2. Launch JupyterLab:

```bash
jupyter lab
```

3. In JupyterLab:
   - Navigate the file browser on the left.
   - Open `notebooks/<something>.ipynb` (double-click).
   - Run cells with **Shift + Enter** (or Run menu).

4. Use the CLI scripts (example):

```bash
python scripts/rent_vs_buy.py --help
python scripts/rent_vs_buy.py --rent 1800 --price 400000 --down 0.2 --rate 0.065 --years 30
```

See per-module `README.md` (in 03/ and 04/) for phases and more examples.

## How to Use for Actual Learning / Drilling

- Follow the progression above for building concepts step by step.
- In notebooks: Read the markdown cells (overviews + explanations). Find **"Try This"** sections at the end of many notebooks.
  - Example: Edit a named constant (e.g. change a value in `RATES = [...]` or `SIM_YEARS`), then **Shift+Enter** on the cell(s) that use it.
  - Watch the chart/output update live. This is how you actively drill "what if this changes?".
- Tweak, re-run, observe, repeat. Git lets you branch your experiments.
- Scripts are for quick non-Jupyter "what if" runs (see --help).

## Current State

- Environments: Minimal declarative `environment.yml` (full exports backed up as `environment-full-export.yml` in 03/04).
- Notebooks: Narrative docs + extracted constants + Try This exercises for active learning.
- Scripts: Improved validation/error handling on key ones.
- Structure: Root + per-module READMEs (03/04), .gitignore, local git.
- Harness: Registered (data-science-conda-jupyter, prototype). See grok-harness docs/handoff for AI session history.

## Learning Path Summary

Progressive build:
- 01-02: Get data in, plot it, Jupyter comfort.
- 03: Core finance skills (statements → health metrics → TVM → market analysis → portfolio risk/return).
- 04: Apply to real life (budgeting, debt, housing) + turn explorations into reusable CLI tools.

The harness layer adds: reproducibility, clear docs, tunable params for experiments, version control, and high standards without bloat.

## Principles We're Applying

- Diagnose before acting
- Explicit trade-offs (documented in the plan)
- Reproducibility and documentation even for learning work
- One chunk at a time with verification gates
- Code quality, error handling at boundaries, and reader-focused docs (drawing from established patterns)

Charts committed for instant visuals (trade-off noted in plan). See per-module READMEs for details.

---

For harness/AI session context: `/Users/stevenromero/Development/grok-harness/docs/session-handoff-2026-07-03-anaconda.md` (and latest handoff). Project content lives here; harness state is external for clean sessions.