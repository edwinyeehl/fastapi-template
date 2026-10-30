import uuid

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.schemas.envelope import ProblemDetails, ResponseEnvelope, ResponseMeta

app = FastAPI(
    title="FastAPI Agentic Backend",
    version="0.1.0",
)


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    """Attach or propagate X-Request-ID across the request lifecycle."""
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    return response


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Format HTTP exceptions into RFC 9457 Problem Details envelopes."""
    problem = ProblemDetails(
        type=f"https://errors.api.internal/{exc.status_code}",
        title=exc.detail if isinstance(exc.detail, str) else "HTTP Error",
        status=exc.status_code,
        detail=str(exc.detail),
        instance=request.url.path,
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=problem.model_dump(exclude_none=True),
        media_type="application/problem+json",
        headers={"x-request-id": getattr(request.state, "request_id", "")},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Format request validation errors into RFC 9457 Problem Details envelopes."""
    problem = ProblemDetails(
        type="https://errors.api.internal/validation-error",
        title="Request Validation Failed",
        status=422,
        detail="The submitted request body, query, or path parameters failed schema validation.",
        instance=request.url.path,
        errors=[
            {
                "loc": [str(x) for x in err.get("loc", [])],
                "msg": err.get("msg"),
                "type": err.get("type"),
            }
            for err in exc.errors()
        ],
    )
    return JSONResponse(
        status_code=422,
        content=problem.model_dump(exclude_none=True),
        media_type="application/problem+json",
        headers={"x-request-id": getattr(request.state, "request_id", "")},
    )


@app.get("/", response_model=ResponseEnvelope[dict[str, str]])
async def main(request: Request) -> ResponseEnvelope[dict[str, str]]:
    return ResponseEnvelope(
        data={"message": "Hello World"},
        meta=ResponseMeta(request_id=getattr(request.state, "request_id", None)),
    )
