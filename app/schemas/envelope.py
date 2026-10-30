from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class ResponseMeta(BaseModel):
    """Metadata for pagination, traces, and execution tracking."""

    request_id: str | None = None
    page: int | None = None
    per_page: int | None = None
    total_count: int | None = None
    has_more: bool | None = None


class ResponseEnvelope(BaseModel, Generic[DataT]):
    """Standardized top-level response envelope for single/list resources."""

    success: bool = True
    data: DataT
    meta: ResponseMeta | None = None


class ProblemDetails(BaseModel):
    """RFC 9457 standard problem details object for API errors."""

    type: str = "about:blank"
    title: str
    status: int
    detail: str | None = None
    instance: str | None = None
    code: str | None = None
    errors: list[dict[str, Any]] | None = None
    extra: dict[str, Any] = Field(default_factory=dict)
