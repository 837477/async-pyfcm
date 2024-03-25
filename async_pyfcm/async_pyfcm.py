import aiohttp
from typing import Union
from .pyfcm_auth import PyFCMAuth
from .message import Message
from .errors import (
    UnspecifiedError, InvalidArgumentError, UnregisteredError,
    SenderIdMismatchError, QuotaExceededError, UnavailableError,
    InternalServerError, ThirdPartyAuthError
)


class AsyncPyFCM(PyFCMAuth):

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.session.close()

    def __init__(
        self,
        google_application_credentials: Union[str, dict],
        token_auto_refresh: bool = True,
    ):
        """
        AsyncPyFCM Initialization

        :param google_application_credentials:
        Private key issued from Firebase's project service account
        (Json File Path or Json String inside File or Json Object(dict) inside File)

        :param token_auto_refresh:
        Google API's Access Token expires after a certain period of time.
        Decide whether to automatically refresh the Access Token.

        True (Default): The Access Token is checked immediately before sending the message, and is automatically renewed 30 minutes before expiration.
        False: Access Token is not refreshed automatically.
            - In this case, the AsyncPyFCM object must be created again.
            - Suitable for short-term use.
        """
        super().__init__(
            google_application_credentials=google_application_credentials,
            token_auto_refresh=token_auto_refresh
        )
        self.endpoint = "https://fcm.googleapis.com"

    async def send(self, message: Message):
        """
        Send to FCM Server

        :param message: The message to send.
        :return: JSON response from the FCM Server.
        """
        if not hasattr(self, "session"):
            async with aiohttp.ClientSession() as session:
                self.session = session
                return await self._post_message(message)
        else:
            return await self._post_message(message)

    async def _post_message(self, message: Message):
        """
        Internal method to post a message.
        """
        async with self.session.post(
            url=f"{self.endpoint}/v1/projects/{self.project_id}/messages:send",
            headers={
                "Authorization": f"Bearer {self.access_token}",
                "Content-Type": "application/json"
            },
            json={"message": message}
        ) as response:
            result = await response.json()
            if response.status == 200:
                return result
            elif response.status == 400:
                raise InvalidArgumentError(result)
            elif response.status == 401:
                raise ThirdPartyAuthError(result)
            elif response.status == 403:
                raise SenderIdMismatchError(result)
            elif response.status == 404:
                raise UnregisteredError(result)
            elif response.status == 429:
                raise QuotaExceededError(result)
            elif response.status == 500:
                raise InternalServerError(result)
            elif response.status == 503:
                raise UnavailableError(result)
            else:
                raise UnspecifiedError(result)
