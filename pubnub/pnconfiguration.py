from .enums import PNHeartbeatNotificationOptions, PNReconnectionPolicy
from . import utils


class PNConfiguration(object):
    def __init__(self):
        # TODO: add validation
        self.uuid = None
        self.origin = "pubsub.pubnub.com"
        self.ssl = False
        self.non_subscribe_request_timeout = 10
        self.subscribe_timeout = 310
        self.connect_timeout = 5
        self.subscribe_key = None
        self.publish_key = None
        self.cipher_key = None
        self.auth_key = None
        self.filter_expression = None
        self.enable_subscribe = True
        self.heartbeat_notification_options = PNHeartbeatNotificationOptions.FAILURES
        self.reconnect_policy = PNReconnectionPolicy.NONE

        self._presence_timeout = None
        self._heartbeat_interval = None

        self.set_presence_timeout(10)

    def validate(self):
        assert self.uuid is None or isinstance(self.uuid, str)

        if self.uuid is None:
            self.uuid = utils.uuid()

    def scheme(self):
        if self.ssl:
            return "https"
        else:
            return "http"

    def scheme_extended(self):
        return self.scheme() + "://"

    def scheme_and_host(self):
        return self.scheme_extended() + self.origin

    def set_presence_timeout_with_custom_interval(self, timeout, interval):
        self._presence_timeout = timeout
        self._heartbeat_interval = interval

    def set_presence_timeout(self, timeout):
        self.set_presence_timeout_with_custom_interval(timeout, (timeout / 2) - 1)

    @property
    def presence_timeout(self):
        return self._presence_timeout

    @property
    def heartbeat_interval(self):
        return self._heartbeat_interval

        # TODO: set log level
        # TODO: set log level