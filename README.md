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

## How to Use for Actual Learning / Drilling Now

The project is harness-formalized and ready:
- Follow the progression in the modules table above.
- In any notebook, use the "Try This" sections: change a named constant (e.g. a rate or extra payment), re-execute the relevant cells, observe how the finance outcome changes.
- This turns passive reading into active experimentation so the concepts stick.
- Use the CLI scripts for quick "what if" scenarios outside Jupyter.
- Git is active locally — branch to experiment, commit your learnings.

When you're done with a learning session, we can use the harness to wrap (handoff) what you discovered.

## Current Harness Formalization (Chunk 1+)

This project follows the approved plan from the harness session:

- Registered in grok-harness/config/registry.yaml (stack: data-science-conda-jupyter, rigor: prototype)
- Root hygiene: this README + .gitignore
- Future chunks (see plan.md in session): environment standardization, notebook documentation quality, script robustness + error handling, end-to-end verification

**Process notes** (human-in-the-loop by design):
- All changes go through explicit diagnosis → plan → human review + approval.
- Visibility: registry, plans, command output, and diffs are always surfaced.
- You steer creative direction and high-level decisions. The harness handles structure, verification, and mundane execution.

## Learning Path & How to Drill Concepts

The modules form a progressive curriculum:

1. Basics (01-02): Real data + viz, Jupyter practice.
2. Core Finance (03): Statements → ratios/health → TVM → stocks → portfolios.
3. Application (04): Personal finance + CLI tools extracted from notebooks.

**Now that it's harness-formalized:**
- Each notebook has narrative docs + "Try This" exercises (tweak a constant like rate or extra payment, re-run, observe the effect).
- Key parameters are named constants (not magic numbers) so you can experiment safely.
- Run in order for building intuition, or jump in and modify to test "what if".
- Activate the env, open Jupyter, tweak, learn.

See per-module READMEs for phases. This setup keeps things organized and lean while maximizing learning.

## Principles We're Applying

- Diagnose before acting
- Explicit trade-offs (documented in the plan)
- Reproducibility and documentation even for learning work
- One chunk at a time with verification gates
- Code quality, error handling at boundaries, and reader-focused docs (drawing from established patterns)

Generated charts are currently committed (trade-off decision logged in plan). Environments are being improved from full pinned exports toward minimal declarative specs.

---

See `/Users/stevenromero/Development/grok-harness/docs/session-handoff-2026-07-03-anaconda.md` and the executed plan for full context.