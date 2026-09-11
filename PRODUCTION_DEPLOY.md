# DMS Fleet Pro V12 — Production Deployment

## Current state
- Flask DMS application
- Vercel-ready entrypoint and configuration
- Preloaded vehicle master
- SQLite included as local/demo fallback

## Production architecture
Vercel (Flask) -> PostgreSQL -> Persistent object storage -> Notification worker/cron -> Email/WhatsApp provider

## Required before real production
1. Create a managed PostgreSQL database.
2. Migrate application persistence from SQLite to PostgreSQL.
3. Move breakdown photos from local `/tmp` to persistent object storage (Vercel Blob/S3-compatible storage).
4. Set a strong `DMS_SECRET_KEY`.
5. Change the default `admin/admin123` account credentials immediately.
6. Configure email/WhatsApp provider credentials outside source control.
7. Add scheduled jobs for service-due, missing-entry and breakdown escalation notifications.
8. Run a production smoke test: login, vehicle lookup, daily entry, breakdown/photo, service, dashboard, exports.

## Important
Do not treat the bundled SQLite database as production persistence on Vercel. Serverless instances can be replaced and local filesystem data is not a durable database.
