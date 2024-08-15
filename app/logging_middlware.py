import json
import logging
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging
from app.logging_setup import LoggerSetup

logger = logging.getLogger("app_logger")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        client_ip = request.client.host

        body = await request.body()
        request_body = body.decode("utf-8")
        log_request_body = json.loads(request_body) if request_body else {}

        log_body_formatted = (
            json.dumps(log_request_body, indent=1) if log_request_body else "{}"
        )
        if log_body_formatted == "{}":
            logger.info(
                f"Client: {client_ip} - Method: {request.method} - URL: {request.url}"
            )
        else:
            logger.info(
                f"Client: {client_ip} - Method:{request.method} - URL: {request.url} Body:\n{log_body_formatted}"
            )

        response = await call_next(request)
        process_time = time.time() - start_time

        logger.info(
            f"Response: status_code={response.status_code}, process_time={process_time:.4f}s"
        )

        return response
