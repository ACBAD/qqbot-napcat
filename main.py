from pathlib import Path
from ncatbot.core import BotClient
from ncatbot.plugin_system import on_group_poke
from ncatbot.core.event import PokeNoticeEvent
from ncatbot.utils import status, get_log, ncatbot_config
bot = BotClient()
WHAT_JPG = Path('what.jpg')
logger = get_log('Main')


@on_group_poke
async def poke_func(event: PokeNoticeEvent):
    if event.target_id != ncatbot_config.bt_uin:
        return
    if WHAT_JPG.exists():
        await status.global_api.send_group_image(event.group_id, str(WHAT_JPG))


bot.run_frontend()
