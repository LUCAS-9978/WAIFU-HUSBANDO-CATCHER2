class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7812770062"
    sudo_users = ""
    GROUP_ID = -1002296333139

    TOKEN = "8160950383:AAE4ddE0nG9R2xCbyG_u1a7lYBXngFdyRlc"
    mongo_url = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/"
    PARTNER = "7361967332", "7795212861", "5758240622"
    PHOTO_URL = ["https://files.catbox.moe/7vr2im.jpg", "https://files.catbox.moe/7vr2im.jpg"]
    SUPPORT_CHAT = "https://t.me/hwkwjieie"
    UPDATE_CHAT = "https://t.me/DBZ_COMMUNITY_2"
    BOT_USERNAME = "@XYZ_WAIFU_BOT"
    CHARA_CHANNEL_ID = "-1002621413939"
    api_id = 23287799
    api_hash = "9f4f17dae2181ee22c275b9b40a3c907"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
