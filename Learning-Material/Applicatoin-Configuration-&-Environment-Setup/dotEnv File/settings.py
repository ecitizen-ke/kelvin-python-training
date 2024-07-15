
# Import the dotenv modules to load environment specific config values to the settings.py file
from dotenv import load_dotenv

# Importing the os package
import os

# Load environment variables from .env file
load_dotenv()

# Database settings
# The URI for connecting to the database. Default is a local SQLite database.
DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///default.db')

# Username for the database connection.
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'default_user')

# Password for the database connection.
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'default_password')

# Debug mode
# Enables or disables debug mode. In debug mode, the server will reload on code changes and provide detailed error pages.
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Logging settings
# Path to the log file where logs should be written.
LOG_FILE = os.getenv('LOG_FILE', 'app.log')

# Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Controls the severity of messages that are logged.
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

# Secret key for sessions
# A secret key used by Flask to encrypt session cookies. This should be a long random string.
SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

# Email settings
# SMTP server for sending emails.
MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.defaultmail.com')

# SMTP server port.
MAIL_PORT = int(os.getenv('MAIL_PORT', 587))

# Username for the email server.
MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'default_email_username')

# Password for the email server.
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'default_email_password')

# API keys
# API key for accessing Google services.
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'default_google_api_key')

# Pagination settings
# Number of items to display per page in paginated views.
ITEMS_PER_PAGE = int(os.getenv('ITEMS_PER_PAGE', 10))

# Application title
# The title of the application, which might be used in templates and web pages.
APP_TITLE = os.getenv('APP_TITLE', 'My Flask App')

# File upload settings
# Directory where uploaded files will be stored.
UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', '/path/to/uploads')

# Cache settings
# Type of caching to use (e.g., 'SimpleCache', 'RedisCache').
CACHE_TYPE = os.getenv('CACHE_TYPE', 'SimpleCache')

# URL for connecting to the Redis server if Redis caching is used.
CACHE_REDIS_URL = os.getenv('CACHE_REDIS_URL', '')

# Security settings
# Salt for hashing passwords. This should be a long random string.
SECURITY_PASSWORD_SALT = os.getenv(
    'SECURITY_PASSWORD_SALT', 'default_password_salt')

# Hashing algorithm for hashing passwords.
SECURITY_PASSWORD_HASH = os.getenv('SECURITY_PASSWORD_HASH', 'bcrypt')

# CORS settings
# List of origins that are allowed to make cross-origin requests.
CORS_ALLOWED_ORIGINS = os.getenv(
    'CORS_ALLOWED_ORIGINS', 'http://localhost:3000,https://example.com').split(',')

# Other settings
# Maximum size of uploaded files (e.g., 16 MB).
MAX_CONTENT_LENGTH = int(
    os.getenv('MAX_CONTENT_LENGTH', 16 * 1024 * 1024))  # 16 MB

# Additional settings can be added here as needed

# Example of additional configuration
# Timezone setting for the application.
TIMEZONE = os.getenv('TIMEZONE', 'UTC')

# Default language for the application.
DEFAULT_LANGUAGE = os.getenv('DEFAULT_LANGUAGE', 'en')

# Session timeout in seconds.
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT', 3600))  # 1 hour

# Whether to use secure cookies for session management.
SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'False') == 'True'

# OAuth settings
# OAuth client ID for authentication.
OAUTH_CLIENT_ID = os.getenv('OAUTH_CLIENT_ID', 'default_client_id')

# OAuth client secret for authentication.
OAUTH_CLIENT_SECRET = os.getenv('OAUTH_CLIENT_SECRET', 'default_client_secret')

# Base URL for the OAuth provider.
OAUTH_BASE_URL = os.getenv('OAUTH_BASE_URL', 'https://oauth.provider.com')

# URL to redirect to after successful OAuth login.
OAUTH_REDIRECT_URI = os.getenv(
    'OAUTH_REDIRECT_URI', 'https://myapp.com/oauth/callback')
