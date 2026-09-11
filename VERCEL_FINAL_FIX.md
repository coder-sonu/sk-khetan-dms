# Vercel Final Fix

This package explicitly declares the Flask entrypoint for Vercel:

```toml
[tool.vercel]
entrypoint = "app:app"
```

Upload the CONTENTS of this folder to the GitHub repository root, so `app.py`, `pyproject.toml`, `requirements.txt`, `templates/`, and `static/` are directly visible at repository root.

In Vercel:
- Framework Preset: Other
- Root Directory: leave blank
- Build Command: no override
- Output Directory: no override
- Install Command: no override

Then redeploy the latest commit.
