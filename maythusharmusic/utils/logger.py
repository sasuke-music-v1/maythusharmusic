
from config import LOG, LOG_GROUP_ID
from maythusharmusic import app
from maythusharmusic.utils.database import is_on_off


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "Private Group"

        logger_text = f"""
**{app.mention} Play Log**

**Chat ID:** `{message.chat.id}`
**Chat Name:** {message.chat.title}
**Chat Username:** {chatusername}

**User ID:** `{message.from_user.id}`
**Name:** {message.from_user.mention}
**Username:** @{message.from_user.username}

**Query:** {message.text.split(None, 1)[1]}
**Stream Type:** {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    disable_web_page_preview=True,
                )
            except Exception:
                pass
        return
