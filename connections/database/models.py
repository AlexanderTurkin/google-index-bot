import datetime
from sqlalchemy import BigInteger, ForeignKey, func, String
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from tgbot.config import load_config, DbConfig

config = load_config('.env')
db = DbConfig(host=config.db.host, user=config.db.user, password=config.db.password, database=config.db.database, port=config.db.port)

engine = create_async_engine(
    db.construct_sqlalchemy_url(),
    query_cache_size=1200,
    pool_size=20,
    max_overflow=200,
    future=True,
    echo=False,
)

session_pool = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tid: Mapped[int] = mapped_column(BigInteger)
    balance: Mapped[int] = mapped_column(BigInteger, default=0)
    language: Mapped[int] = mapped_column(BigInteger, default=0)
    registered_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

async def configure_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)