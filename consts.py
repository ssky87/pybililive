WS_HOST = 'broadcastlv.chat.bilibili.com'
WS_PORT = 2244
WS_URI = 'sub'
WS_HEADER_STRUCT = '!IHHII'
WS_OP_HEARTBEAT = 2
WS_OP_HEARTBEAT_REPLY = 3
WS_OP_MESSAGE = 5
WS_OP_USER_AUTHENTICATION = 7
WS_OP_CONNECT_SUCCESS = 8
GIFT_SYS_GIFT = 0
GIFT_SYS_LUCKY_MONEY = 1
GIFT_SYS_TV = 2
GIFT_SYS_ANNOUNCEMENT = 3
GIFT_SYS_GUARD = 4
GIFT_SYS_ACTIVITY_RED_PACKET = 6
WS_PACKAGE_OFFSET = 0
WS_HEADER_OFFSET = 4
WS_VERSION_OFFSET = 6
WS_OPERATION_OFFSET = 8
WS_SEQUENCE_OFFSET = 12
WS_PACKAGE_HEADER_TOTAL_LENGTH = 16
WS_HEADER_DEFAULT_VERSION = 1
WS_HEADER_DEFAULT_OPERATION = 1
WS_HEADER_DEFAULT_SEQUENCE = 1

API_LIVE_BASE_URL = 'api.live.bilibili.com'
GET_REAL_ROOM_URI = 'room/v1/Room/room_init'
REQUEST_TIME_OUT = 15

VERSION = 1
MAGIC = 16
MAGIC_PARAM = 1
HEADER_LENGTH = 16

# actions
HEART_BEAT = 2
JOIN_CHANNEL = 7

HEARTBEAT_DELAY = 10
CHECK_ERROR_DELAY = 15