import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@"
        f"{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/"
        f"{os.getenv('DB_NAME')}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "secret")
print("DB_USER =", os.getenv("DB_USER"))
print("DB_PASSWORD =", os.getenv("DB_PASSWORD"))
print("DB_HOST =", os.getenv("DB_HOST"))
print("DB_NAME =", os.getenv("DB_NAME"))
print(Config.SQLALCHEMY_DATABASE_URI)