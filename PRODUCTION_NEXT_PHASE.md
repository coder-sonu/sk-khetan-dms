# DMS Fleet Pro V11 — Production Deployment Phase

This package is the Vercel-ready continuation of V10.

## Included
- Existing DMS application and UI
- 339 source vehicle rows / 336 unique vehicle registrations in the supplied master
- Mobile daily KM + diesel entry
- Breakdown + photo workflow
- Service tracking and alerts
- Vehicle 360°
- Dashboard / 30-day diesel analytics
- MIS exports / audit trail / Copilot
- Vercel deployment configuration

## Production requirement
The current application package still uses SQLite. SQLite on Vercel is ephemeral, so it must not be treated as the final production database.

Before production go-live, configure:
- `DMS_SECRET_KEY` — strong random secret
- `DATABASE_URL` — managed PostgreSQL connection string
- Persistent object storage for breakdown photos (Vercel Blob or S3-compatible storage)
- Scheduled notification worker / Vercel Cron for service and missing-entry alerts
- Email/WhatsApp provider credentials

## Deployment status
The Vercel account connection is available, but this chat deployment workspace does not currently expose the project-file upload arguments required by the deployment endpoint. Therefore no claim of a successful production deployment is made from this package.

## Immediate go-live sequence
1. Create a PostgreSQL database (Neon/Supabase/RDS/etc.).
2. Run the database migration against PostgreSQL.
3. Move uploaded photos to object storage.
4. Add Vercel environment variables.
5. Deploy this project to Vercel.
6. Import/verify the vehicle master.
7. Change `admin/admin123` immediately.
8. Run a daily-entry, breakdown-photo, service-alert and export smoke test.

## Local fallback
The included SQLite database remains useful for local/demo use.
