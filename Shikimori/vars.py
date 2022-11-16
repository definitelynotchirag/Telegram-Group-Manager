import os


ENV = bool(os.environ.get("ENV", True))

if ENV:
    TOKEN = os.environ.get("BOT_TOKEN", "5756571846:AAF1XIJ7SwOrkpQm6p_1YgEuE7GoX6fu1qw")

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", 1109460378))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")
     
    ERROR_LOG_CHANNEL = os.environ.get("ERROR_LOG_CHANNEL", "-1001795543122")
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "chirag57")

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "1716925723").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "1109460378").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1001795543122")
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    API_ID = os.environ.get("API_ID", "12335430")
    API_HASH = os.environ.get("API_HASH", "2a9046339be3b90ec40891896b95f77e")
    DB_URL = os.environ.get("DATABASE_URL", "postgresql://bbiovhcz:I6YB-BEFAlMclvJNhAtzBLMMY8oE8K0P@satao.db.elephantsql.com/bbiovhcz")
    # DB_URL = DB_URL.get("postgres://", "postgresql://", 1)
    FUNC_DB_URL = os.environ.get("FUNC_DB_URL", "postgresql://bbiovhcz:I6YB-BEFAlMclvJNhAtzBLMMY8oE8K0P@satao.db.elephantsql.com/bbiovhcz")
    # FUNC_DB_URL = FUNC_DB_URL.get("postgres://", "postgresql://", 1)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://chirag57:A9325442737a@cluster0.yeisy5y.mongodb.net/?retryWrites=true&w=majority")
    ARQ_API = os.environ.get("ARQ_API_BASE_URL")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD")
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", True)
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    API_WEATHER = os.environ.get("API_WEATHER", None)
    WALL_API = os.environ.get("WALL_API", None)
    REDIS_URL = os.environ.get("REDIS_URL", "redis://admin:A9325442737a@@redis-10041.c301.ap-south-1-1.ec2.cloud.redislabs.com:10041/bot-free-db")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "peronaxsupport")
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    ARQ_API_KEY = os.environ.get("ARQ_API", "KAWQFT-VKAEYR-AAMZCN-CKSEUZ-ARQ")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "peronatest")
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY","1d15e75b-c831-4a69-b3a8-b0743d662f3b")
    APOD_API_KEY = os.environ.get("APOD_API_KEY", None)
    ANIME_NAME = os.environ.get("ANIME_NAME", "One Piece")
    START_MEDIA = os.environ.get("START_MEDIA", "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "perona_xbot")
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "macnetwork7")
    ALIVE_MEDIA = os.environ.get("ALIVE_MEDIA", "https://telegra.ph/file/2a965bf4dcd562ce4e9da.mp4")
    BOT_ID = os.environ.get("BOT_ID", "5756571846")
    STATS_IMG = os.environ.get("STATS_IMG", None)
    NETWORK = os.environ.get("NETWORK", "Mac")
    NETWORK_USERNAME = os.environ.get("NETWORK_USERNAME", "macnetwork7")
    MEDIA_GM = os.environ.get("MEDIA_GM", None)
    MEDIA_GN = os.environ.get("MEDIA_GN", None)
    MEDIA_HELLO = os.environ.get("MEDIA_HELLO", None)
    MEDIA_BYE = os.environ.get("MEDIA_BYE", None)
    INLINE_IMG = os.environ.get("INLINE_IMG", None)
    OWNER_WELCOME_MEDIA = os.environ.get("OWNER_WELCOME_MEDIA", None)

    try:
        WHITELIST_CHATS = {int(x) for x in os.environ.get('WHITELIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

    try:
        BLACKLIST_CHATS = {int(x) for x in os.environ.get('BLACKLIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

else:
    from Shikimori.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")
    ERROR_LOG_CHANNEL = Config.ERROR_LOG_CHANNEL
    OWNER_USERNAME = Config.OWNER_USERNAME

    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    LOG_CHANNEL = Config.LOG_CHANNEL
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH
    HEROKU_API_KEY = Config.HEROKU_API_KEY
    HEROKU_APP_NAME = Config.HEROKU_APP_NAME
    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    LOAD = Config.LOAD
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    AI_API_KEY = Config.AI_API_KEY
    API_WEATHER = Config.API_WEATHER
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    APOD_API_KEY = Config.APOD_API_KEY
    REDIS_URL = Config.REDIS_URL
    ANIME_NAME = Config.ANIME_NAME
    START_MEDIA = Config.START_MEDIA
    BOT_USERNAME = Config.BOT_USERNAME
    UPDATE_CHANNEL = Config.UPDATE_CHANNEL
    ALIVE_MEDIA = Config.ALIVE_MEDIA
    BOT_ID = Config.BOT_ID
    STATS_IMG = Config.STATS_IMG
    NETWORK = Config.NETWORK
    NETWORK_USERNAME = Config.NETWORK_USERNAME
    MEDIA_GM = Config.MEDIA_GM
    MEDIA_GN = Config.MEDIA_GN
    MEDIA_HELLO = Config.MEDIA_HELLO
    MEDIA_BYE = Config.MEDIA_BYE
    INLINE_IMG = Config.INLINE_IMG
    OWNER_WELCOME_MEDIA = Config.OWNER_WELCOME_MEDIA

    try:
        WHITELIST_CHATS = {int(x) for x in os.environ.get('WHITELIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")

    try:
        BLACKLIST_CHATS = {int(x) for x in os.environ.get('BLACKLIST_CHATS', "").split()}
    except ValueError:
        raise Exception(
            "Your blacklisted chats list does not contain valid integers.")
            
PM_START_TEXT = """
════════《✧》════════
𝙺𝚘𝚗𝚗𝚒𝚌𝚑𝚒𝚠𝚊 *{} - 𝚜𝚊𝚗*

𝙸 𝚊𝚖 *{}*, 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚖𝚊𝚗𝚊𝚐𝚎𝚖𝚎𝚗𝚝 𝚋𝚘𝚝 𝚋𝚊𝚜𝚎𝚍 𝚘𝚗 𝚝𝚑𝚎 𝚊𝚗𝚒𝚖𝚎 *{}*.
════════════════
♡ 𝐔𝐬𝐞𝐫𝐬: `{}`
♡ 𝐂𝐡𝐚𝐭𝐬: `{}`
♡ 𝐔𝐩𝐭𝐢𝐦𝐞: `{}`
════════════════
𝚄𝚜𝚎 `/help` 𝚝𝚘 𝚐𝚘 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚖𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜.
════════《✧》════════
"""

HELP_STRINGS = """
𝙲𝚕𝚒𝚌𝚔 𝚘𝚗 𝚝𝚑𝚎 𝚋𝚞𝚝𝚝𝚘𝚗 𝚋𝚎𝚕𝚕𝚘𝚠 𝚝𝚘 𝚐𝚎𝚝 𝚍𝚎𝚜𝚌𝚛𝚒𝚙𝚝𝚒𝚘𝚗 𝚊𝚋𝚘𝚞𝚝 𝚜𝚙𝚎𝚌𝚒𝚏𝚒𝚌𝚜 𝚌𝚘𝚖𝚖𝚊𝚗𝚍."""