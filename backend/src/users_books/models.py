import uuid

from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database import BaseAlchemyModel


class UsersBooksModel(BaseAlchemyModel):
    __tablename__ = "users_books"

    book_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("books.book_id"),
        primary_key=True,
        nullable=False,
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.user_id"),
        primary_key=True,
        nullable=False,
    )

    book_shelf: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

