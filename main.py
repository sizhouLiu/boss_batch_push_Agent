import uvicorn
from dotenv import load_dotenv
from loguru import logger

from app.conf.env import settings

if __name__ == "__main__":
    load_dotenv()
    logger.info(f"current env: {settings.ENV}")
    port = 8000
    logger.info(f"Server will be available at: http://localhost:{port}")
    uvicorn.run("model_service.app:app", host="0.0.0.0", port=port)
