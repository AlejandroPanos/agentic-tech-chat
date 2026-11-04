from fastapi import APIRouter, status

router = APIRouter(tags=["health"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def health():
    return {"app": "agentic_chat", "status": "healthy", "version": "1.0.0"}
