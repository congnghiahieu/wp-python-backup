""" 
https://fastapi.tiangolo.com/tutorial/cookie-params/

https://fastapi.tiangolo.com/tutorial/header-params/
"""

from typing import Annotated
from fastapi import APIRouter, Cookie, Header

header_router = APIRouter(prefix="/header", tags=["Header & Cookie"])


""" Cookie Parameters """


@header_router.get("/items/headers/with_cookie")
def read_items_with_cookie(ssid: Annotated[str, Cookie()]):
    return {"ssid": ssid}


""" Header Parameters """


@header_router.get("/items/headers/user_agent")
def read_items_with_user_agent(accept_encoding: Annotated[str, Header()]):
    """
    Automatic conversion: Các trường viết hoa và phân cách bằng dấu gạch ngang của Brower sẽ tương ứng với viết thường và dấu gạch ngang thay thế bởi dấu gạch dưới

    Ex:
    Accept ~ accept
    Accept-Encoding ~ accept_encoding
    Accept-Language ~ accept_language
    Cache-Control ~ cache_control
    Connection ~ connection
    Cookie ~ cookie
    Host ~ host
    Sec-Ch-Ua ~ sec_ch_ua
    Sec-Ch-Ua-Mobile ~ sec_ch_ua_mobile
    Sec-Ch-Ua-Platform ~ sec_ch_ua_platform
    Sec-Fetch-Dest ~ sec_fetch_dest
    Sec-Fetch-Mode ~ sec_fetch_mode
    Sec-Fetch-Site ~ sec_fetch_site
    Sec-Fetch-User ~ sec_fetch_user
    Upgrade-Insecure-Requests ~ upgrade_insecure_requests
    User-Agent ~ user_agent
    """

    return {"Accepct-Encoding": accept_encoding}
