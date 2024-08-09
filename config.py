from os import environ 

class Config:
    API_ID = environ.get("API_ID", "29640188")
    API_HASH = environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7406110931:AAEv13lgNk8ux3ucSMTerL1aGyqGYHI53yU") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://syangshibo1:mongodbdatabase500@cluster0.vtkrte7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Hackerautoforwarderbot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6364152774').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
