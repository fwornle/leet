# LeetCode Patterns

The 15 essential LeetCode patterns in Python, as an MkDocs site: how to recognise each one, a diagram of how it works, its time and space complexity, and tested solutions. The whole site is designed to be learned in 2–3 hours.

Published at <https://fwornle.github.io/leet/> (GitHub Pages, deployed by `.github/workflows/deploy-docs.yml` on push to `main`).

## Layout

```
docs/               MkDocs pages (one per pattern + complexity primer, decision tree, cheatsheet)
src/patterns/       Python solutions; sections marked with --8<-- are embedded into the docs
tests/              pytest tests for every embedded solution
```

## Local use

```bash
make test    # uv run pytest -q
make serve   # uv run mkdocs serve  → http://127.0.0.1:8000
make build   # uv run mkdocs build --strict
```

Based on the pattern list from [LeetCode was HARD until I Learned these 15 Patterns](https://www.youtube.com/watch?v=DjYZk8nrXVY) by Ashish Pratap Singh.
