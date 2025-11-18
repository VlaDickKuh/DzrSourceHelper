from datetime import datetime
from pprint import pprint

import requests

from config import GAME_ID
from config import S_URL
from config import session



def encode_text(text: str) -> str:
    return text.replace("\n", "<br>") \
               .replace("\ufeff", "") \
               .replace("”", "\"") \
               .encode("windows-1251")


def rgb_to_hex(r, g, b) -> str:
    if r == None: r = 0
    if g == None: g = 0
    if b == None: b = 0

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)

    return f'#{r:02x}{g:02x}{b:02x}'


def upload_tech_level() -> None:
    tec_level = {}
    tec_level["category"] = GAME_ID
    tec_level["action"] =  "add_zadanie"
    tec_level["gZone"] = 0
    tec_level["title"] = "Технический уровень".encode("windows-1251")
    tec_level["question"] = """<p>Это техническая заглушка</p>
<script src="../../uploaded/msk/Night/jquery-1.11.2.min.txt"></script>
<script src="../../uploaded/msk/Night/jquery.cookie.txt"></script>
<script type="text/javascript">// <![CDATA[
$(document).ready(function() {
  $.ajax({ url: "https://alt.where.games/initn.js?v=1", dataType: "script", cache: true, });
});
// ]]></script>""".encode("windows-1251")
    tec_level["clue1"] = "-"
    tec_level["clue2"] = "-"
    tec_level["comment"] = "-"
    tec_level["code[0]"] = 456457643867837433636
    tec_level["danger[0]"] = "null"
    tec_level["bonus"] = "on"
    tec_level["skvoz"] = "on"


    headers = {
    "accept-language": "ru,en;q=0.9,de;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=windows-1251",
    }
    session.post(S_URL, data=tec_level, headers=headers)