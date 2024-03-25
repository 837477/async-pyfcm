<br><br><br>
<p align="center">
  <a href="https://github.com/837477/async-pyfcm"><img src="https://github.com/837477/async-pyfcm/assets/37999795/249c6b6f-5f82-4b80-8c4f-e2c3311f1f15"></a>
</p>
<p align="center">
    <em>From now on, easily send FCM (Firebase Cloud Messages) through Python asyncio!</em>
</p>
<p align="center">
<a href="https://github.com/837477/async-pyfcm/blob/main/LICENSE" target="_blank">
    <img src="https://img.shields.io/pypi/l/async-pyfcm?color=FEC301" alt="License">
</a>
<a href="https://pypi.org/project/async-pyfcm" target="_blank">
    <img src="https://img.shields.io/pypi/v/async-pyfcm?color=FEC301" alt="Package version">
</a>
<a href="https://pypi.org/project/async-pyfcm" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/async-pyfcm?color=FEC301" alt="Supported Python versions">
</a>
</p>
<br><br><br>

---

**Documnets**: <a href="https://github.com/837477/async-pyfcm" target="_blank">https://github.com/837477/async-pyfcm </a>

---

You can now easily send asynchronous FCM messages.<br>
`AsyncPyfcm` has the following features:

- Support for sending Python Asyncio FCM messages
- Supports all types of messages handled by FCM
- Very convenient message sending interface
- Easily handle Firebase credentials (Json File / Json String / Json Object[Dict])
- Supports automatic access token refresh.
- Increase performance efficiency by maintaining asynchronous sessions depending on the situation.
- All exception situations in FCM can be controlled.


## Requirements

If you are planning to use FCM now, I think you have already studied FCM.<br>
As you know, `google_application_credentials` is required to use FCM.<br>
**The existing Cloud Messaging API server key will be deprecated on June 20, 2024, so it is recommended to obtain a `google_application_credentials` key in the future.**

To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.

To generate a private key file for your service account: <br>
1. In the Firebase console, open Settings > <a href="https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk?_gl=1*pput8o*_up*MQ..*_ga*MTQ0NTkyMjIzOC4xNzExMTMyOTM2*_ga_CW55HF8NVT*MTcxMTEzMjkzNi4xLjAuMTcxMTEzMjkzNi4wLjAuMA.." target="_blank">Service Accounts. </a>
2. Click Generate New Private Key, then confirm by clicking Generate Key.
3. Securely store the JSON file containing the key.

For a more detailed explanation, please refer to the following official document.<br>
https://firebase.google.com/docs/cloud-messaging/migrate-v1#provide-credentials-using-adc


## Installation

```console
$ pip install async-pyfcm
```

## Example

### AsyncPyFCM Initialization

```Python
from async_pyfcm import AsyncPyFCM

# AsyncPyFCM requires one required parameter and one optional parameter.

# [param] google_application_credentials:
# Private key issued from Firebase's project service account
# (Json File Path / Json String inside File / Json Object(dict) inside File)

# [param] token_auto_refresh:
# Google API's Access Token expires after a certain period of time.
# Decide whether to automatically refresh the Access Token.

# True (Default): The Access Token is checked immediately before sending the message, and is automatically renewed 30 minutes before expiration.
# False: Access Token is not refreshed automatically.
#   - In this case, the AsyncPyFCM object must be created again.
#   - Suitable for short-term use.

# Case 1: Json File Path
async_pyfcm = AsyncPyFCM(
    google_application_credentials="google-application-credentials.json",
    token_auto_refresh=True
)

# Case 2: Json String inside File
async_pyfcm = AsyncPyFCM(
    google_application_credentials='{"type": "service_account", ...}',
    token_auto_refresh=True
)

# Case 3: Json Object(dict) inside File
async_pyfcm = AsyncPyFCM(
    google_application_credentials={
        "type": "service_account",
        ...
    },
    token_auto_refresh=True
)
```

You can use it flexibly according to your development situation.


### Asynchronous FCM message sending

* You can check it in the `example.py` file.

```Python
from async_pyfcm import AsyncPyFCM

async def stateful_session():
    # This sample is used when you want to maintain an asynchronous session of aiohttp.
    # You can use resources efficiently by not opening a session every time you send.
    async with AsyncPyFCM(google_application_credentials="path/to/your/credentials.json") as async_fcm:
        responses = await asyncio.gather(
            async_fcm.send(message),
            async_fcm.send(message),
            async_fcm.send(message),
        )
        return responses

async def stateless_session():
    # This sample uses the AsyncPyFCM object by declaring it.
    # This method does not maintain the aiohttp asynchronous session, so it connects the session every time you send.
    async_pyfcm = AsyncPyFCM(
        google_application_credentials="path/to/your/credentials.json"
    )
    responses = await asyncio.gather(
        async_pyfcm.send(message),
        async_pyfcm.send(message),
        async_pyfcm.send(message),
    )
    return responses
```


### Message Resource

* You can check it in the `message.py` file.

```Python
# All message formats provided by FCM documents are supported.
class Message(TypedDict):
    """
    FCM Message Resource
    https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages
    """
    name: str
    data: dict[str, str]
    notification: Notification
    android: AndroidConfig
    webpush: WebpushConfig
    apns: ApnsConfig
    fcm_options: FcmOptions
    token: str
    topic: str
    condition: str
```

## Contributing
The following is a set of guidelines for contributing to sejong-univ-auth. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

1. Please create a branch in this format, **`<Issue Number>-<Some name>`**
2. Open a terminal and navigate to your project path. And enter this.
   **`git config --global commit.template .gitmessage.txt`**
3. You can use the template, with `git commit` through vi. **Not** `git commit -m`
4. If you want to merge your work, please pull request to the `dev` branch.
5. Enjoy contributing!

If you have any other opinions, please feel free to suggest 😀

## License

This project is licensed under the terms of the MIT license.
