import datetime
from connections.database.models import User, session_pool
from sqlalchemy import select, insert, update, delete

async def add_user(tid: int):
    async with session_pool() as session:
        result = await session.execute(insert(User).values(tid=tid))
        await session.commit()

        return result.inserted_primary_key[0]

async def get_user(tid: int):
    async with session_pool() as session:
        result = await session.execute(select(User).where(User.tid == tid))
        return result.scalar()

async def get_all_users():
    async with session_pool() as session:
        result = await session.execute(select(User))
        return result.scalars().all()

async def user_exists(tid: int) -> bool:
    async with session_pool() as session:
        result = await session.execute(select(User).where(User.tid == tid))
        return bool(result.scalar())