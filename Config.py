import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 5975793487:AAH3aj_COuelckXvLtF8m0Ad91M3l38XYOk)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOJUBu4vvwieQZ_u3MByl21rd__pP9VztnIVpKHfNXo2LTWtvWhiHT6T46uM-Nr4uu0ameJSFSwvwsWxV5Zl1RP6H0ScQQARwui3LmL5iDh9uhiRR6kxNt39ooExkfT1CxvdE1NCHOcAKFZpiBq1qqEWaSl6rFn-KJSK7Z66-JkIPuBPvm_XtKXkcLM0dMueTYm7SNYbsFwv_eWrS0XhpcfYThb2px8yoe9LI_ibhXn9KT1ec0on6JFFqpNdxAIwmOy0AubnxiWgdw7GwXt5aTZDv5l3e-PeSVo5ROvuzrMlE16F4qTaly_DzAmvWSueIxa5tXMb_zrifDm0iw7RAzztsduU=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
