from ncatbot.core import BotClient
from ncatbot.core.event import PrivateMessageEvent

bot = BotClient()


@bot.on_group_message()
async def on_private_message(event: PrivateMessageEvent):
    print("收到消息")

bot.run_frontend()
