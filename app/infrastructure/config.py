from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expire_minutes: int

    db_user: str
    db_password: str
    db_host: str
    db_name: str
    pass_admin_user: str

    class Config:
        env_file = ".env"

settings = Settings()
