#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "36123528"))
API_HASH = environ.get("API_HASH", "7f77eb79febe2b7cf5d33d6d57bc8ac0")
BOT_TOKEN = environ.get("BOT_TOKEN", "8640143346:AAGUFxqf9PvQa6w9PKalQQYHz_aQzycWAZc")

OWNER = int(environ.get("OWNER", "8532700793"))
CREDIT = environ.get("CREDIT", "𝘽𝙊𝙏𝙎")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7831923713').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



