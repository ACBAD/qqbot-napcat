from pathlib import Path
from ncatbot.core import BotClient
from ncatbot.plugin_system import on_group_poke
from ncatbot.core.event import RequestEvent
from ncatbot.utils import status
bot = BotClient()
WHAT_JPG = Path('what.jpg')


@on_group_poke
async def at_func(event: RequestEvent):
    if WHAT_JPG.exists():
        await status.global_api.send_group_image(event.group_id, str(WHAT_JPG))


bot.run_frontend()
