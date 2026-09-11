# DMS Security Checklist

- [ ] Set `DMS_SECRET_KEY` to a long random secret.
- [ ] Replace default admin password.
- [ ] Use HTTPS only.
- [ ] Keep database credentials in Vercel environment variables.
- [ ] Keep notification/API credentials in environment variables.
- [ ] Restrict Admin/Manager-only actions.
- [ ] Validate uploaded photo type and size before production use.
- [ ] Use persistent object storage for uploaded photos.
- [ ] Enable database backups/point-in-time recovery.
- [ ] Review audit logs regularly.
- [ ] Add rate limiting/SSO if the DMS is internet-facing at scale.
