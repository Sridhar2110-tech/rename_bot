import os

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://sridharlogavani2003_db_user:AQ9HRgRQzNpq6nEm@cluster0.zuxkmip.mongodb.net/?appName=Cluster0")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", 0))
