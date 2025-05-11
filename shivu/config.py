class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7812770062"
    sudo_users = ""
    GROUP_ID = -1002296333139

    TOKEN = "8160950383:AAE4ddE0nG9R2xCbyG_u1a7lYBXngFdyRlc"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
    PARTNER = ""
    PHOTO_URL = ["https://files.catbox.moe/7vr2im.jpg", "https://files.catbox.moe/7vr2im.jpg"]
    SUPPORT_CHAT = "https://t.me/XYZ_SUPPORT_TM"
    UPDATE_CHAT = "https://t.me/XYZ_UPDATE_TM"
    BOT_USERNAME = "@XYZ_WAIFU_BOT"
    CHARA_CHANNEL_ID = "-1002296333139"
    api_id = 20737348
    api_hash = "c5a1aa4d0aa8a25c39b44eb456118e12"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
