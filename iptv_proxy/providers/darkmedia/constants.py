class DarkMediaConstants(object):
    __slots__ = []

    DB_FILE_NAME = 'darkmedia.db'
    DEFAULT_EPG_SOURCE = 'darkmedia'
    DEFAULT_PLAYLIST_PROTOCOL = 'hls'
    DEFAULT_PLAYLIST_TYPE = 'dynamic'
    PROVIDER_NAME = 'DarkMedia'
    TEMPORARY_DB_FILE_NAME = 'darkmedia_temp.db'
    VALID_EPG_SOURCE_VALUES = ['other', 'darkmedia']
    VALID_PLAYLIST_PROTOCOL_VALUES = ['hls', 'mpegts']
    VALID_PLAYLIST_TYPE_VALUES = ['dynamic', 'static']

    _provider_name = PROVIDER_NAME.lower()
