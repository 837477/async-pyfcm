"""
This module contains the error classes for AsyncPyFCM.
https://firebase.google.com/docs/reference/fcm/rest/v1/ErrorCode
"""


class InvalidCredentialsError(Exception):
    """
    Raised when the credentials provided are invalid.
    """
    pass


class AsyncPyFCMError(Exception):
    """
    Raised when an error occurs in AsyncPyFCM.
    """
    pass


class UnspecifiedError(AsyncPyFCMError):
    """
    No more information is available about this error.
    """
    pass


class InvalidArgumentError(AsyncPyFCMError):
    """
    Request parameters were invalid.
    An extension of type google.rpc.BadRequest is returned to specify which field was invalid.
    """
    pass


class UnregisteredError(AsyncPyFCMError):
    """
    App instance was unregistered from FCM.
    This usually means that the token used is no longer valid and a new one must be used.
    """
    pass


class SenderIdMismatchError(AsyncPyFCMError):
    """
    The authenticated sender ID is different from the sender ID for the registration token.
    """
    pass


class QuotaExceededError(AsyncPyFCMError):
    """
    Sending limit exceeded for the message target.
    An extension of type google.rpc.QuotaFailure is returned to specify which quota was exceeded.
    """
    pass


class UnavailableError(AsyncPyFCMError):
    """The server is overloaded."""
    pass


class InternalServerError(AsyncPyFCMError):
    """An unknown internal error occurred."""
    pass


class ThirdPartyAuthError(AsyncPyFCMError):
    """APNs certificate or web push auth key was invalid or missing."""
    pass
