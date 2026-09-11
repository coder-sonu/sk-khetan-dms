# Sk Khetan Group — V12 Vercel Deployment

This bundle is prepared for Vercel's Python/Flask runtime. Vercel supports Flask directly with the Python runtime.

## Important production note

The current V10 application uses SQLite. On Vercel, the filesystem is ephemeral, so this bundle uses `/tmp` when `VERCEL=1`. That is suitable for a deployment smoke-test/demo, **not for production fleet records**.

For production, the next step is to move the database to managed PostgreSQL (Neon/Supabase/etc.) and photos to object storage (Vercel Blob/S3). Do not use `/tmp` as the permanent DMS database.

## Deploy with Vercel CLI

```bash
npm i -g vercel
vercel login
cd DMS_Fleet_Pro_V10
vercel
```

For production:

```bash
vercel --prod
```

## Environment variable

Set a strong `DMS_SECRET_KEY` in Vercel Project Settings → Environment Variables.

Example locally:

```bash
vercel env add DMS_SECRET_KEY production
```

## Default login

`admin / admin123`

**Change the admin password before real use.**

## Recommended V11 production architecture

Vercel Flask → PostgreSQL → Blob/S3 → scheduled alerts → WhatsApp/Email → AI assistant.
