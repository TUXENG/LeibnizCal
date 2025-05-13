# test_env.py
from src.config import settings

print("App Name:", settings.app_name)
print("Debug Mode:", settings.debug)
print("Database URL:", settings.database_url)
print("Host:", settings.host)
print("Port:", settings.port)
