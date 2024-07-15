# Database settings
DATABASE_URI = 'sqlite:///mydatabase.db'
DATABASE_USERNAME = 'admin'
DATABASE_PASSWORD = 'password'

# Debug mode
DEBUG = True

# Logging settings
LOG_FILE = 'app.log'
LOG_LEVEL = 'DEBUG'

# Secret key for sessions
SECRET_KEY = 'your_secret_key_here'

# Email settings
MAIL_SERVER = 'smtp.example.com'
MAIL_PORT = 587
MAIL_USERNAME = 'username'
MAIL_PASSWORD = 'password'

# API keys
GOOGLE_API_KEY = 'your_google_api_key'

# Pagination settings
ITEMS_PER_PAGE = 10

# Application title
APP_TITLE = 'My Flask App'

# File upload settings
UPLOAD_FOLDER = '/path/to/uploads'

# Cache settings
CACHE_TYPE = 'redis'
CACHE_REDIS_URL = 'redis://localhost:6379/0'

# Security settings
SECURITY_PASSWORD_SALT = 'your_password_salt_here'
SECURITY_PASSWORD_HASH = 'bcrypt'

# CORS settings
CORS_ALLOWED_ORIGINS = ['http://localhost:3000', 'https://example.com']

# Other settings
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
