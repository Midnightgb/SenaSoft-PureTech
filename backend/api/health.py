# ./api/health.py
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from fastapi import Depends
from db.session import get_db, server_status
import asyncio
from core.utils.logger import Logger

router = APIRouter()

logger = Logger()

@router.get("/health_check")
async def health_check(db: Session = Depends(get_db)):
    try:
        is_healthy = await asyncio.wait_for(asyncio.to_thread(server_status, db), timeout=5.0)
        if is_healthy:
            logger.success("Health check passed: Service is up and database is connected")
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"status": "healthy", "message": "Service is up and database is connected"}
            )
        else:
            logger.warning("Health check failed: Service is up but database is not responding correctly")
            return JSONResponse(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                content={"status": "unhealthy", "message": "Service is up but database is not responding correctly"}
            )
    except asyncio.TimeoutError:
        logger.error("Health check failed: Database connection check timed out")
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "unhealthy", "message": "Service is slow or unresponsive"}
        )
    except Exception as e:
        logger.error(f"Unexpected error during health check: {str(e)}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"status": "error", "message": f"An unexpected error occurred: {str(e)}"}
        )