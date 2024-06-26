"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class StoreAndForward(google.protobuf.message.Message):
    """
    TODO: REPLACE
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _RequestResponse:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _RequestResponseEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[StoreAndForward._RequestResponse.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        UNSET: StoreAndForward._RequestResponse.ValueType  # 0
        """
        Unset/unused
        """
        ROUTER_ERROR: StoreAndForward._RequestResponse.ValueType  # 1
        """
        Router is an in error state.
        """
        ROUTER_HEARTBEAT: StoreAndForward._RequestResponse.ValueType  # 2
        """
        Router heartbeat
        """
        ROUTER_PING: StoreAndForward._RequestResponse.ValueType  # 3
        """
        Router has requested the client respond. This can work as a
        "are you there" message.
        """
        ROUTER_PONG: StoreAndForward._RequestResponse.ValueType  # 4
        """
        The response to a "Ping"
        """
        ROUTER_BUSY: StoreAndForward._RequestResponse.ValueType  # 5
        """
        Router is currently busy. Please try again later.
        """
        ROUTER_HISTORY: StoreAndForward._RequestResponse.ValueType  # 6
        """
        Router is responding to a request for history.
        """
        ROUTER_STATS: StoreAndForward._RequestResponse.ValueType  # 7
        """
        Router is responding to a request for stats.
        """
        ROUTER_TEXT_DIRECT: StoreAndForward._RequestResponse.ValueType  # 8
        """
        Router sends a text message from its history that was a direct message.
        """
        ROUTER_TEXT_BROADCAST: StoreAndForward._RequestResponse.ValueType  # 9
        """
        Router sends a text message from its history that was a broadcast.
        """
        CLIENT_ERROR: StoreAndForward._RequestResponse.ValueType  # 64
        """
        Client is an in error state.
        """
        CLIENT_HISTORY: StoreAndForward._RequestResponse.ValueType  # 65
        """
        Client has requested a replay from the router.
        """
        CLIENT_STATS: StoreAndForward._RequestResponse.ValueType  # 66
        """
        Client has requested stats from the router.
        """
        CLIENT_PING: StoreAndForward._RequestResponse.ValueType  # 67
        """
        Client has requested the router respond. This can work as a
        "are you there" message.
        """
        CLIENT_PONG: StoreAndForward._RequestResponse.ValueType  # 68
        """
        The response to a "Ping"
        """
        CLIENT_ABORT: StoreAndForward._RequestResponse.ValueType  # 106
        """
        Client has requested that the router abort processing the client's request
        """

    class RequestResponse(_RequestResponse, metaclass=_RequestResponseEnumTypeWrapper):
        """
        001 - 063 = From Router
        064 - 127 = From Client
        """

    UNSET: StoreAndForward.RequestResponse.ValueType  # 0
    """
    Unset/unused
    """
    ROUTER_ERROR: StoreAndForward.RequestResponse.ValueType  # 1
    """
    Router is an in error state.
    """
    ROUTER_HEARTBEAT: StoreAndForward.RequestResponse.ValueType  # 2
    """
    Router heartbeat
    """
    ROUTER_PING: StoreAndForward.RequestResponse.ValueType  # 3
    """
    Router has requested the client respond. This can work as a
    "are you there" message.
    """
    ROUTER_PONG: StoreAndForward.RequestResponse.ValueType  # 4
    """
    The response to a "Ping"
    """
    ROUTER_BUSY: StoreAndForward.RequestResponse.ValueType  # 5
    """
    Router is currently busy. Please try again later.
    """
    ROUTER_HISTORY: StoreAndForward.RequestResponse.ValueType  # 6
    """
    Router is responding to a request for history.
    """
    ROUTER_STATS: StoreAndForward.RequestResponse.ValueType  # 7
    """
    Router is responding to a request for stats.
    """
    ROUTER_TEXT_DIRECT: StoreAndForward.RequestResponse.ValueType  # 8
    """
    Router sends a text message from its history that was a direct message.
    """
    ROUTER_TEXT_BROADCAST: StoreAndForward.RequestResponse.ValueType  # 9
    """
    Router sends a text message from its history that was a broadcast.
    """
    CLIENT_ERROR: StoreAndForward.RequestResponse.ValueType  # 64
    """
    Client is an in error state.
    """
    CLIENT_HISTORY: StoreAndForward.RequestResponse.ValueType  # 65
    """
    Client has requested a replay from the router.
    """
    CLIENT_STATS: StoreAndForward.RequestResponse.ValueType  # 66
    """
    Client has requested stats from the router.
    """
    CLIENT_PING: StoreAndForward.RequestResponse.ValueType  # 67
    """
    Client has requested the router respond. This can work as a
    "are you there" message.
    """
    CLIENT_PONG: StoreAndForward.RequestResponse.ValueType  # 68
    """
    The response to a "Ping"
    """
    CLIENT_ABORT: StoreAndForward.RequestResponse.ValueType  # 106
    """
    Client has requested that the router abort processing the client's request
    """

    @typing_extensions.final
    class Statistics(google.protobuf.message.Message):
        """
        TODO: REPLACE
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        MESSAGES_TOTAL_FIELD_NUMBER: builtins.int
        MESSAGES_SAVED_FIELD_NUMBER: builtins.int
        MESSAGES_MAX_FIELD_NUMBER: builtins.int
        UP_TIME_FIELD_NUMBER: builtins.int
        REQUESTS_FIELD_NUMBER: builtins.int
        REQUESTS_HISTORY_FIELD_NUMBER: builtins.int
        HEARTBEAT_FIELD_NUMBER: builtins.int
        RETURN_MAX_FIELD_NUMBER: builtins.int
        RETURN_WINDOW_FIELD_NUMBER: builtins.int
        messages_total: builtins.int
        """
        Number of messages we have ever seen
        """
        messages_saved: builtins.int
        """
        Number of messages we have currently saved our history.
        """
        messages_max: builtins.int
        """
        Maximum number of messages we will save
        """
        up_time: builtins.int
        """
        Router uptime in seconds
        """
        requests: builtins.int
        """
        Number of times any client sent a request to the S&F.
        """
        requests_history: builtins.int
        """
        Number of times the history was requested.
        """
        heartbeat: builtins.bool
        """
        Is the heartbeat enabled on the server?
        """
        return_max: builtins.int
        """
        Maximum number of messages the server will return.
        """
        return_window: builtins.int
        """
        Maximum history window in minutes the server will return messages from.
        """
        def __init__(
            self,
            *,
            messages_total: builtins.int = ...,
            messages_saved: builtins.int = ...,
            messages_max: builtins.int = ...,
            up_time: builtins.int = ...,
            requests: builtins.int = ...,
            requests_history: builtins.int = ...,
            heartbeat: builtins.bool = ...,
            return_max: builtins.int = ...,
            return_window: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["heartbeat", b"heartbeat", "messages_max", b"messages_max", "messages_saved", b"messages_saved", "messages_total", b"messages_total", "requests", b"requests", "requests_history", b"requests_history", "return_max", b"return_max", "return_window", b"return_window", "up_time", b"up_time"]) -> None: ...

    @typing_extensions.final
    class History(google.protobuf.message.Message):
        """
        TODO: REPLACE
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        HISTORY_MESSAGES_FIELD_NUMBER: builtins.int
        WINDOW_FIELD_NUMBER: builtins.int
        LAST_REQUEST_FIELD_NUMBER: builtins.int
        history_messages: builtins.int
        """
        Number of that will be sent to the client
        """
        window: builtins.int
        """
        The window of messages that was used to filter the history client requested
        """
        last_request: builtins.int
        """
        Index in the packet history of the last message sent in a previous request to the server.
        Will be sent to the client before sending the history and can be set in a subsequent request to avoid getting packets the server already sent to the client.
        """
        def __init__(
            self,
            *,
            history_messages: builtins.int = ...,
            window: builtins.int = ...,
            last_request: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["history_messages", b"history_messages", "last_request", b"last_request", "window", b"window"]) -> None: ...

    @typing_extensions.final
    class Heartbeat(google.protobuf.message.Message):
        """
        TODO: REPLACE
        """

        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PERIOD_FIELD_NUMBER: builtins.int
        SECONDARY_FIELD_NUMBER: builtins.int
        period: builtins.int
        """
        Period in seconds that the heartbeat is sent out that will be sent to the client
        """
        secondary: builtins.int
        """
        If set, this is not the primary Store & Forward router on the mesh
        """
        def __init__(
            self,
            *,
            period: builtins.int = ...,
            secondary: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["period", b"period", "secondary", b"secondary"]) -> None: ...

    RR_FIELD_NUMBER: builtins.int
    STATS_FIELD_NUMBER: builtins.int
    HISTORY_FIELD_NUMBER: builtins.int
    HEARTBEAT_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    rr: global___StoreAndForward.RequestResponse.ValueType
    """
    TODO: REPLACE
    """
    @property
    def stats(self) -> global___StoreAndForward.Statistics:
        """
        TODO: REPLACE
        """
    @property
    def history(self) -> global___StoreAndForward.History:
        """
        TODO: REPLACE
        """
    @property
    def heartbeat(self) -> global___StoreAndForward.Heartbeat:
        """
        TODO: REPLACE
        """
    text: builtins.bytes
    """
    Text from history message.
    """
    def __init__(
        self,
        *,
        rr: global___StoreAndForward.RequestResponse.ValueType = ...,
        stats: global___StoreAndForward.Statistics | None = ...,
        history: global___StoreAndForward.History | None = ...,
        heartbeat: global___StoreAndForward.Heartbeat | None = ...,
        text: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["heartbeat", b"heartbeat", "history", b"history", "stats", b"stats", "text", b"text", "variant", b"variant"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["heartbeat", b"heartbeat", "history", b"history", "rr", b"rr", "stats", b"stats", "text", b"text", "variant", b"variant"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["variant", b"variant"]) -> typing_extensions.Literal["stats", "history", "heartbeat", "text"] | None: ...

global___StoreAndForward = StoreAndForward
