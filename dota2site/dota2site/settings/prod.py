from .base import *

DEBUG = False

class RequireForProduction(Exception):
    pass

if not SECRET_KEY:
    logger.warning("SECRET_KEY is empty")

if not DB_SETUP:
    logger.warning("Database connection not setup")

if not EMAIL_SMTP_ENABLED:
    logger.warning("EMAIL_HOST_USER and EMAIL_HOST_PASSWORD are empty")

if not GITHUB_CLIENT_ID or not GITHUB_SECRET_KEY:
    logger.warning("GITHUB CLIENT_ID and SECRET_KEY are empty")
