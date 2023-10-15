import os


class Config:
    BACKEND_HOST = os.environ.get("BACKEND_HOST")
    BACKEND_API_KEY = os.environ.get("BACKEND_API_KEY")
