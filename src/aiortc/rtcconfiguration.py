from dataclasses import dataclass
import enum
from typing import List, Optional


@dataclass
class RTCIceServer:
    """
    The :class:`RTCIceServer` dictionary defines how to connect to a single
    STUN or TURN server. It includes both the URL and the necessary credentials,
    if any, to connect to the server.
    """

    urls: str
    """
    This required property is either a single string or a list of strings,
    each specifying a URL which can be used to connect to the server.
    """
    username: Optional[str] = None
    "The username to use during authentication (for TURN only)."
    credential: Optional[str] = None
    "The credential to use during authentication (for TURN only)."
    credentialType: str = "password"

class RTCBundlePolicy(enum.Enum):
    """
    See https://w3c.github.io/webrtc-pc/#rtcbundlepolicy-enum
    """

    BALANCED = "balanced"
    MAX_COMPAT = "max-compat"
    MAX_BUNDLE = "max-bundle"



@dataclass
class RTCConfiguration:
    """
    The :class:`RTCConfiguration` dictionary is used to provide configuration
    options for an :class:`RTCPeerConnection`.
    """

    iceServers: Optional[List[RTCIceServer]] = None
    "A list of :class:`RTCIceServer` objects to configure STUN / TURN servers."

    bundlePolicy: Optional[RTCBundlePolicy] = RTCBundlePolicy.BALANCED
    "Note: only max-compat is implemented currently."
