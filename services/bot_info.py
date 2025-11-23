from aiogram import Bot, types


class BotInfo:
    me: types.User | None = None
    username: str | None = None

    @classmethod
    async def update_class_username(cls, bot: Bot) -> str:
        """Updates the bot instance and retrieves the username."""
        if cls.username is None:
            cls.me = await bot.get_me()
            cls.username = cls.me.username
        return cls.username
