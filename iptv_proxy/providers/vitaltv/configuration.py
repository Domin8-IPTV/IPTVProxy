import logging

from iptv_proxy.providers.vitaltv.constants import VitalTVConstants
from iptv_proxy.providers.iptv_provider.configuration import ProviderConfiguration
from iptv_proxy.providers.iptv_provider.configuration import ProviderOptionalSettings

logger = logging.getLogger(__name__)


class VitalTVConfiguration(ProviderConfiguration):
    __slots__ = []

    _configuration_schema = {'Provider': ['url', 'username', 'password'],
                             'Playlist': ['protocol', 'type'],
                             'EPG': ['source', 'url']}
    _provider_name = VitalTVConstants.PROVIDER_NAME.lower()


class VitalTVOptionalSettings(ProviderOptionalSettings):
    __slots__ = []

    _provider_name = VitalTVConstants.PROVIDER_NAME.lower()
