from loguru import logger
import questionary

from config import S_URL
from config import GAME_ID
from config import get_session
from gdoc import get_gdoc
from utils import encode_text
from test_doc import test_doc
from upload_files import upload_files_to_source



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


    logger.info("Заливаю технический уровень")
    headers = {
    "accept-language": "ru,en;q=0.9,de;q=0.8",
    "content-type": "application/x-www-form-urlencoded; charset=windows-1251",
    }
    session = get_session()
    s_resp = session.post(S_URL, data=tec_level, headers=headers)
    if s_resp.status_code != 200:
        logger.warning(f"Технический уровень не залит")
        logger.warning(f"Код ошибки {s_resp.status_code}")
    else:
        logger.info(f"Технический уровень залит")


def upload_levels(add = True) -> None:
    if questionary.confirm("Загрузить файлы из гугл диска в движок?", default=False).ask():
        upload_files_to_source()

    logger.info("Получаю данные из гугл дока")
    g_doc_datas = get_gdoc()
    if g_doc_datas == None:
        logger.warning("Данные из гуглдока не получены\nНажми любую клавишу для выхода")
    logger.info("Данные из гугл дока получены")

    if test_doc(g_doc_datas, add): 
        logger.warning("Есть ошибки в доке. Заливка невозможна\nНажми любую клавишу для продолжения")
        return None
    
    logger.info("Ошибок нет\n")
    if questionary.confirm("Продолжить?", default=False).ask():
        for g_doc_data in g_doc_datas:
            level_data = {}

            level_data["category"] = GAME_ID
            if add: level_data["action"] = "add_zadanie" 
            else: level_data["action"] = "update_zadanie"
            level_data["gZone"] = 0

            for title in g_doc_data:
                if not add: level_data["id"] = g_doc_data.get(title).get("ID Уровня:").get("content")
                level_data["title"] = encode_text(title)
                level_data["question"] = encode_text(g_doc_data.get(title).get("Текст уровня:").get("Текст:").get("content"))
                level_data["locationComment"] = encode_text(g_doc_data.get(title).get("Текст уровня:").get("Примечания:").get("content"))
                level_data["clue1"] = encode_text(g_doc_data.get(title).get("Подсказка 1:").get("Текст:").get("content"))
                level_data["clue2"] = encode_text(g_doc_data.get(title).get("Подсказка 2:").get("Текст:").get("content"))
                if g_doc_data.get(title).get("Сквозной:").get("content").lower() == "да": 
                    level_data["skvoz"] = "on"
                    if g_doc_data.get(title).get("Подсказка 1:").get("Выдавать по запросу:").get("content").lower() == "да":
                        level_data["zapros1"] = "on"
                        level_data["shtraf1"] = g_doc_data.get(title).get("Подсказка 1:").get("Штраф за использование:").get("content")
                    if g_doc_data.get(title).get("Подсказка 2:").get("Выдавать по запросу:").get("content").lower() == "да":
                        level_data["zapros2"] = "on"
                        level_data["shtraf2"] = g_doc_data.get(title).get("Подсказка 2:").get("Штраф за использование:").get("content")                 
                else:
                    level_data["ClueMin"] = g_doc_data.get(title).get("Подсказка 1:").get("Время до подсказки:").get("content")
                    level_data["ClueMin2"] = g_doc_data.get(title).get("Подсказка 2:").get("Время до подсказки:").get("content")
                    level_data["ClueMin3"] = g_doc_data.get(title).get("Время до окончания уровня:").get("content")
                level_data["comment"] = encode_text(g_doc_data.get(title).get("Комментарий и фото кодов:").get("content"))
                
                for i, code in enumerate(g_doc_data.get(title).get("Основные коды уровня:").get("tables")[0][1:]):
                    level_data[f"code[{i}]"] = encode_text(code[1])
                    level_data[f"danger[{i}]"] = code[2]
                    level_data[f"sector[{i}]"] = code[3]
                level_data["codeCount"] = g_doc_data.get(title).get("Количество кодов для взятия:").get("Вышка:").get("content")
                if g_doc_data.get(title).get("Сектора на уровне:"):
                    for i, sec in enumerate(g_doc_data.get(title).get("Сектора на уровне:").get("tables")[0][1:]):
                        level_data[f"secName[{i}]"] = encode_text(sec[1])
                if g_doc_data.get(title).get("Бонусные коды уровня:"):
                    for i, bonus in enumerate(g_doc_data.get(title).get("Бонусные коды уровня:").get("tables")[0][1:]):    
                        level_data[f"codeB[{i}]"] = encode_text(bonus[1])
                        level_data[f"dangerB[{i}]"] = bonus[2]
                        level_data[f"timeB[{i}]"] = bonus[3]
                    level_data["timeAddBonusAll"] = g_doc_data.get(title).get("Бонус за полное взятие:").get("content")
                if g_doc_data.get(title).get("Штрафные коды уровня:"):
                    for i, shtraf in enumerate(g_doc_data.get(title).get("Штрафные коды уровня:").get("tables")[0][1:]):    
                        level_data[f"codeF[{i}]"] = encode_text(shtraf[1])
                        level_data[f"fakeShtraf[{i}]"] = shtraf[2]
                
                if g_doc_data.get(title).get("Спойлеры:"):
                    for i, spoiler in enumerate(g_doc_data.get(title).get("Спойлеры:")):
                        if spoiler == "content": continue
                        level_data[f"spoiler[{i}]"] = encode_text(g_doc_data.get(title).get("Спойлеры:").get(f"Спойлер {i}:").get("Текст:").get("content"))
                        level_data[f"spoilerCode[{i}]"] = encode_text(g_doc_data.get(title).get("Спойлеры:").get(f"Спойлер {i}:").get("Ответы на спойлер:").get("content"))   
                
                level_data["penalty"] = g_doc_data.get(title).get("Штраф за слив:").get("content")
                
                if g_doc_data.get(title).get("Бонусный:").get("content").lower() == "да": 
                    level_data["bonus"] = "on"
                    level_data["bonusTime"] = g_doc_data.get(title).get("Бонусный:").get("Время бонуса:").get("content")

            if not add and int(level_data["id"]) == 0:
                continue
            logger.info(f"Заливаю уровень '{level_data["title"].decode('cp1251')}'")
            headers = {
                "accept-language": "ru,en;q=0.9,de;q=0.8",
                "content-type": "application/x-www-form-urlencoded; charset=windows-1251",
            }
            session = get_session()
            s_resp = session.post(S_URL, headers=headers, data=level_data)
            if s_resp.status_code != 200:
                logger.warning(f"Уровень '{level_data["title"].decode('cp1251')}' не залит")
                logger.warning(f"Код ошибки {s_resp.status_code}")
            else:
                logger.info(f"Уровень '{level_data["title"].decode('cp1251')}' залит")
        if add:
            upload_tech_level()

        questionary.text("Загрузка завершена\nНажми любую клавишу для продолжения").ask()
    else:
        return None