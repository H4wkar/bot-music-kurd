import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "12901852"))
    API_HASH = os.environ.get("API_HASH", "79653a25e9798a8a6a97918a16b91842")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5747867296:AAGIT-eyHaVkHCB5RQx8shwji4nl-e9_9nY")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu2YmrPbuKL7lJfdVxFKyT9cP8hn3qxtvFzPB7j9qXMsGV0qIZZ6vTpT6vqG1SwtpI29zODPZU397uiBKg4RuXONSjtx-PVkksGhQZDuhVcrG3AUzKHkS2CcZ69bDPWrIxhrNrSgi3TxObqngfJQrNxZ1jo_0gl-8tmK7SyDPqYr_hufUvx6TgLZIulFVF7vPqOVftkoN3_JweSX8PSxqfJ-UPkUo6duVK1dECed0i-L6akcNfcak7H0jbgPZokrkariH6lPhjclzIUtO-9eAGyUtJMfRtDMdTQKP2PNlwNUXNC1kgKpCsszoIsA18fMwqHjbq1akkFGxsOzf0QhrHAs=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MusiccKurdbot")
    SUPPORT = os.environ.get("SUPPORT", "JEPTHONSUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "JEPTHON")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/958d5d3aeaf64d2c64348.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/1d9d53d99d22a5b5e514c.jpg")
