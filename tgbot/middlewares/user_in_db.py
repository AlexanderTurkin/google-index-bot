from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message
from connections.database.requests import get_user, user_exists, add_user


class UserInDatabaseMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.db_user = None

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        if not await user_exists(event.from_user.id):
            referral_code = None



            user_id = await add_user(event.from_user.id)


        self.db_user = await get_user(event.from_user.id)
        data["db_user"] = self.db_user

        return await handler(event, data)