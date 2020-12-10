import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = "1311180684:AAH-nN6xYfKymNl8iv16kbjgP29xvkpxlXs"
    # The Telegram API things
    APP_ID = 1663998
    API_HASH ="a2daed7667424220b2fca694394c5e22"
    OWNER_ID = 1238571337
    # Get these values from my.telegram.org
    # to store the channel ID who are authorized to use the bot
    AUTH_CHANNEL = [-1001393504482]
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    #
    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))
    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 5))
    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 5))
    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "█")
    UN_FINISHED_PROGRESS_STR = os.environ.get("UN_FINISHED_PROGRESS_STR", "░")
    # add offensive API
    TG_OFFENSIVE_API = os.environ.get("TG_OFFENSIVE_API", None)
    CUSTOM_FILE_NAME = os.environ.get("CUSTOM_FILE_NAME", "")
    LEECH_COMMAND = os.environ.get("LEECH_COMMAND", "leech")
    YTDL_COMMAND = os.environ.get("YTDL_COMMAND", "ytdl")
    RCLONE_CONFIG = os.environ.get("RCLONE_CONFIG", "type = drive
client_id = 617414999453-ads3n4r07r3jsuqm2ld7uuv6tvtf4gf6.apps.googleusercontent.com
client_secret = ias_jADb6J4O-Om7pG0ZOnc7
scope = drive
root_folder_id =
token = {"access_token":"ya29.a0AfH6SMCcmpfqDttM_tXWZSwbllQPWB8yopk7RyA92e9OsL7xY9BkM7BpnmcySf6XuL_WHngXDCI3pO24xNM2RgoaqhUOMvEP_1bSlvz1lV257LOUcsykBTd-yqEEZ6Er9IXboyDpYLyK2ZQT-8IOPBMrrf4DqGgG7iAqM67pHWs","token_type":"Bearer","refresh_token":"1//0gOm7Dk3KoxUFCgYIARAAGBASNwF-L9IrkN6KVTaqcuLDyGRJqk87TsAg1CV-sgigJ2n4F1RL81HMcLhlxmh-lPgF9AsANLSUJqA","expiry":"2020-12-10T14:56:49.501763797Z"}
team_drive = 0AM_13IiFDgFsUk9PVA")
    DESTINATION_FOLDER = os.environ.get("DESTINATION_FOLDER", "Mirror Bot")
    GLEECH_COMMAND = os.environ.get("GLEECH_COMMAND", "gleech")
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://td.thyviking.workers.dev/0:/Mirror%20Bot")
    TELEGRAM_LEECH_COMMAND_G = os.environ.get("TELEGRAM_LEECH_COMMAND_G", "tleech")
    CANCEL_COMMAND_G = os.environ.get("CANCEL_COMMAND_G", "cancel")
    GET_SIZE_G = os.environ.get("GET_SIZE_G", "getsize")
    STATUS_COMMAND = os.environ.get("STATUS_COMMAND", "status")
    SAVE_THUMBNAIL = os.environ.get("SAVE_THUMBNAIL", "savethumbnail")
    CLEAR_THUMBNAIL = os.environ.get("CLEAR_THUMBNAIL", "clearthumbnail")
    UPLOAD_AS_DOC = os.environ.get("UPLOAD_AS_DOC", "False")
    PYTDL_COMMAND_G = os.environ.get("PYTDL_COMMAND_G", "pytdl")
    LOG_COMMAND = os.environ.get("LOG_COMMAND", "log")
    CLONE_COMMAND_G = os.environ.get("CLONE_COMMAND_G", "gclone")
    UPLOAD_COMMAND = os.environ.get("UPLOAD_COMMAND", "upload")
    RENEWME_COMMAND = os.environ.get("RENEWME_COMMAND", "renewme")
