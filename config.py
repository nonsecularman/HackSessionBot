import os

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    TOKEN = os.getenv("TOKEN")
    START_PIC = os.getenv("START_PIC")
    CHAT = os.getenv("CHAT")
