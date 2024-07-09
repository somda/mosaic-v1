from datetime import datetime
from typing import Optional

from sqlmodel import create_engine, Field, SQLModel

# Define the URL for the SQLite database
DATABASE_URL = "sqlite+aiosqlite:///{ROOT_DIR}/mosaic.db"

async_engine = create_engine(DATABASE_URL, echo=True)


class Thread(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    role: str
    content: str
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)


SQLModel.metadata.create_all(async_engine)
