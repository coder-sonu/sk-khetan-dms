# Vercel Runtime 500 Fix

The previous package initialized SQLite only inside `if __name__ == "__main__"`. Vercel imports the Flask app as a module, so the database schema was never initialized and `/` could fail with a 500 when checking the user session.

This build runs the idempotent `init()` during module import/cold start, after the database helper functions are defined. On Vercel the demo database remains in `/tmp/dms.sqlite3` and is therefore ephemeral.
