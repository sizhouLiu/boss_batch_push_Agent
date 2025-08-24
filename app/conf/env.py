from dotenv import load_dotenv
from pydantic import BaseSettings
from pydantic import Field

load_dotenv()


class Settings(BaseSettings):
    ENV: str = Field(default="dev", env="ENV")
    BIZ_DB_CONNECTION: str = Field(..., env="BIZ_DB_CONNECTION")
    VEC_DB_CONNECTION: str = Field(..., env="VEC_DB_CONNECTION")
    REDIS_CONNECTION: str = Field(default="redis://localhost:6379", env="REDIS_CONNECTION")
    CLASH_HTTP_PROXY: str = Field(
        default="http://118.195.183.76:17890", env="CLASH_HTTP_PROXY"
    )
    DEEPL_API_KEY: str = Field(default="sk-xxx", env="DEEPL_API_KEY")
    HTTP_PROXY_TUNNEL: str = Field(default="t586.kdltps.com:15818", env="HTTP_PROXY_TUNNEL")
    HTTP_PROXY_USERNAME: str = Field(default="t14124284704238", env="HTTP_PROXY_USERNAME")
    HTTP_PROXY_PASSWORD: str = Field(default="tbqknlst", env="HTTP_PROXY_PASSWORD")
    ZHIPU_API_KEY: str = Field(default="358b9d52741edb2964b449f03dbae324.tVUKAAPERqatadcg", env="ZHIPU_API_KEY")
    LOGURU_LEVEL: str = Field(default="INFO", env="LOGURU_LEVEL")


settings = Settings()
