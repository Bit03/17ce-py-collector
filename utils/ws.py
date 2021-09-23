import hashlib
import base64
import ssl
import time

from settings import base


def md5(string):
    hl = hashlib.md5()
    hl.update(string.encode(encoding="utf-8"))
    return hl.hexdigest()


def base64_str(string):
    return base64.b64encode(string.encode(encoding="utf-8")).decode("utf-8")


def get_ws_url():
    user = base.USER
    api_pwd = base.API_PWD
    ut = str(int(time.time()))
    code = md5(base64_str((md5(api_pwd)[4:23] + user + ut)))
    ws_url = (
        f"wss://wsapi.17ce.com:8001/socket/?ut={ut}&code={code}&user={user}"
    )
    return ws_url


def get_ssl_context():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context
