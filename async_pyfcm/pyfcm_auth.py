import time
import json
import google.auth.transport.requests
from google.oauth2 import service_account
from typing import Union
from .errors import InvalidCredentialsError


class PyFCMAuth:
    def __init__(
        self,
        google_application_credentials: Union[str, dict],
        token_auto_refresh: bool = True,
    ):
        """
        PyFCMAuth Initialization

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
        self.token_auto_refresh = token_auto_refresh
        self.latest_refresh_time = 0
        self._init_credentials(google_application_credentials)

    @property
    def project_id(self):
        """Get project id from credentials"""
        return self._credentials.project_id

    @property
    def access_token(self):
        """Get access token from credentials"""
        self._auto_refresh_credentials()
        return self._credentials.token

    def _auto_refresh_credentials(self):
        """Auto refresh credentials"""
        now_time = time.time()
        if self.token_auto_refresh and now_time - self.latest_refresh_time > 1800:
            self.latest_refresh_time = now_time
            self._refresh_credentials()

    def _refresh_credentials(self):
        """Refresh credentials"""
        request = google.auth.transport.requests.Request()
        self._credentials.refresh(request)

    def _init_credentials(
        self,
        google_application_credentials: Union[str, dict],
        scopes: list[str] = ('https://www.googleapis.com/auth/firebase.messaging',)
    ):
        """Initialize credentials"""
        try:
            if isinstance(google_application_credentials, str):
                # If the credentials is a file path
                if google_application_credentials.lower().endswith('.json'):
                    self._credentials = service_account.Credentials.from_service_account_file(
                        filename=google_application_credentials,
                        scopes=scopes
                    )
                # If the credentials is a json string
                else:
                    self._credentials = service_account.Credentials.from_service_account_info(
                        info=json.loads(google_application_credentials),
                        scopes=scopes
                    )
            # If the credentials is a dictionary
            elif isinstance(google_application_credentials, dict):
                self._credentials = service_account.Credentials.from_service_account_info(
                    info=google_application_credentials,
                    scopes=scopes
                )
            else:
                raise TypeError("")

        except Exception as e:
            raise InvalidCredentialsError(str(e))

        self._refresh_credentials()
