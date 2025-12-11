from pathlib import Path
from ncatbot.core import BotClient
from ncatbot.plugin_system import on_group_at
from ncatbot.core.event import GroupMessageEvent
bot = BotClient()
WHAT_JPG = Path('what.jpg')


@on_group_at
async def at_func(event: GroupMessageEvent):
    if WHAT_JPG.exists():
        await event.reply(image=str(WHAT_JPG))


bot.run_frontend()
