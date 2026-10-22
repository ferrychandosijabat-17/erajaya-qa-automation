import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Central configuration for test environment."""
    BASE_URL = os.getenv("BASE_URL", "https://katalon-demo-cura.herokuapp.com")
    LOGIN_URL = f"{BASE_URL}/profile.php#login"
    DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))  # 10 seconds
