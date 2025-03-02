
from maythusharmusic.core.bot import YukkiBot
from maythusharmusic.core.dir import dirr
from maythusharmusic.core.git import git
from maythusharmusic.core.userbot import Userbot
from maythusharmusic.misc import dbb, heroku, sudo

from .logging import LOGGER
import config

# Pyrogram Client

app = YukkiBot(
    "maythusharmusic",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    sleep_threshold=240,
    max_concurrent_transmissions=5,
    workers=50,
)

userbot = Userbot()

for i, session in enumerate(config.STRING_SESSIONS, start=1):
    userbot.add(
        f"YukkiString{i}",
        api_id=config.API_ID,
        api_hash=config.API_HASH,
        session_string=session.strip(),
    )

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()


from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}