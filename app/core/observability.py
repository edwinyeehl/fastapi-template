from collections.abc import Generator

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger("app.observability.langfuse")


def get_langfuse_callback() -> Generator[object | None, None, None]:
    """Dependency that yields a Langfuse CallbackHandler for LangGraph / LangChain runs.

    If Langfuse keys are absent or disabled, yields None gracefully.
    """
    if not (
        settings.LANGFUSE_ENABLED
        and settings.LANGFUSE_PUBLIC_KEY
        and settings.LANGFUSE_SECRET_KEY
    ):
        yield None
        return

    try:
        from langfuse.langchain import CallbackHandler

        handler = CallbackHandler(
            public_key=settings.LANGFUSE_PUBLIC_KEY,
            secret_key=settings.LANGFUSE_SECRET_KEY,
            host=settings.LANGFUSE_BASE_URL,
        )
        yield handler
    except (ImportError, ValueError, RuntimeError) as exc:
        logger.warning("Failed to initialize Langfuse CallbackHandler", error=str(exc))
        yield None
