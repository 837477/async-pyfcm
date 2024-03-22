import json
import asyncio
import async_pyfcm


async def credentials_sample_1():
    """
    This sample is an authorization method through a json file.
    """
    async_pyfcm = async_pyfcm.AsyncPyFCM(
        google_application_credentials="path/to/your/credentials.json",
        token_auto_refresh=True
    )


async def credentials_sample_2():
    """
    This sample authenticates by importing the json information inside the json file as a string.
    """
    json_string = json.dumps({
        "type": "service_account",
        "project_id": "837477-Sample",
        "private_key_id": "XXXX...",
        "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-XXXX...",
        "client_id": "XXXX...",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-XXXX...",
        "universe_domain": "googleapis.com"
    })
    async_pyfcm = async_pyfcm.AsyncPyFCM(
        google_application_credentials=json_string,
        token_auto_refresh=True
    )


async def credentials_sample_3():
    """
    This sample authenticates by importing the json information inside the json file as a dictionary.
    """
    json_dict = {
        "type": "service_account",
        "project_id": "837477-Sample",
        "private_key_id": "XXXX...",
        "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-XXXX...",
        "client_id": "XXXX...",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-XXXX...",
        "universe_domain": "googleapis.com"
    }
    async_pyfcm = async_pyfcm.AsyncPyFCM(
        google_application_credentials=json_dict,
        token_auto_refresh=True
    )


async def send_sample_1():
    """
    This sample is used when you want to maintain an asynchronous session of aiohttp.
    You can use resources efficiently by not opening a session every time you send.
    """
    async with async_pyfcm.AsyncPyFCM(google_application_credentials="path/to/your/credentials.json", token_auto_refresh=True) as async_fcm:
        responses = await asyncio.gather(
            async_fcm.send(message),
            async_fcm.send(message),
            async_fcm.send(message),
        )
        print(responses)


async def send_sample_2():
    """
    This sample uses the AsyncPyFCM object by declaring it.
    This method does not maintain the aiohttp asynchronous session, so it connects the session every time you send.
    """
    async_pyfcm = async_pyfcm.AsyncPyFCM(
        google_application_credentials="path/to/your/credentials.json"
    )
    responses = await asyncio.gather(
        async_pyfcm.send(message),
        async_pyfcm.send(message),
        async_pyfcm.send(message),
    )
    print(responses)
