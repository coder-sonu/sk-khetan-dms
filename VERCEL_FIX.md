# Vercel Fix — V12

The previous deployment failed because `vercel.json` explicitly declared `functions.api/index.py`, while the current Vercel Flask deployment flow can detect a top-level Flask `app.py` automatically.

This build intentionally removes `vercel.json` and the `api/index.py` wrapper. Vercel should detect the top-level `app.py` as a Flask application automatically.

## GitHub update
Replace the files in the GitHub repository with the contents of this folder, keeping `app.py` at repository root.

Then Vercel → Deployments → Redeploy.

If Vercel has a custom Root Directory, it must point to the folder containing `app.py`.
