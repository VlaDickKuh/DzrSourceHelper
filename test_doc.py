from gdoc_const import *

from loguru import logger



def check_codes_repeat(g_doc_datas: dict):
    for g_doc_data in g_doc_datas:
        for title in g_doc_data:
            for i, code in enumerate(g_doc_data.get(title).get("Основные коды уровня:").get("tables")[0][1:]):
                pass


def test_doc_headers(g_doc_datas: dict) -> bool:
    logger.info("Проверяю заголовки дока")

    has_error = False
    for g_doc_data in g_doc_datas:
        for title in g_doc_data:
            logger.info(f"Проверяю заголовки в '{title}'")
            if g_doc_data.get(title).get(LEVEL_ID) is None:
                logger.warning(f"Нет заголовка айди '{title}'")
                has_error = True
            if g_doc_data.get(title).get(BONUS) is None:
                logger.warning(f"Нет заголовка '{BONUS}' в '{title}'")
                has_error = True
            if g_doc_data.get(title).get(SKVOZ) is None:
                logger.warning(f"Нет заголовка '{SKVOZ}' в '{title}'")
                has_error = True

            if g_doc_data.get(title).get(LEVEL_TEXT) is None:
                logger.warning(f"Нет заголовка '{LEVEL_TEXT}' в '{title}'")
                has_error = True
            else:
                if g_doc_data.get(title).get(LEVEL_TEXT).get(TEXT) is None:
                    logger.warning(f"Нет подзаголовка '{TEXT}' в заголовке '{LEVEL_TEXT}' в '{title}'")
                    has_error = True
                if g_doc_data.get(title).get(LEVEL_TEXT).get(NOTES) is None:
                    logger.warning(f"Нет подзаголовка '{NOTES}' в заголовке '{LEVEL_TEXT}' в '{title}'")
                    has_error = True
            
            if g_doc_data.get(title).get(HINT1) is None:
                logger.warning(f"Нет заголовка '{HINT1}' в '{title}'")
                has_error = True
            else:
                if g_doc_data.get(title).get(HINT1).get(TEXT) is None:
                    logger.warning(f"Нет подзаголовка '{TEXT}' в заголовке '{HINT1}' в '{title}'")
                    has_error = True
                if g_doc_data.get(title).get(SKVOZ).get(CONTENT).lower() == "да":
                    if g_doc_data.get(title).get(HINT1).get(HINT_CONFIRM) is None:
                        logger.warning(f"Нет подзаголовка '{HINT_CONFIRM}' в заголовке '{HINT1}' в '{title}'")
                        has_error = True
                    if g_doc_data.get(title).get(HINT1).get(PENALTY_FOR_USE) is None:
                        logger.warning(f"Нет подзаголовка '{PENALTY_FOR_USE}' в заголовке '{HINT1}' в '{title}'")
                        has_error = True
                else:
                    if g_doc_data.get(title).get(HINT1).get(HINT_TIME) is None:
                        logger.warning(f"Нет подзаголовка '{HINT_TIME}' в заголовке '{HINT1}' в '{title}'")
                        has_error = True
            
            if g_doc_data.get(title).get(HINT2) is None:
                logger.warning(f"Нет заголовка '{HINT2}' в '{title}'")
                has_error = True
            else:
                if g_doc_data.get(title).get(HINT2).get(TEXT) is None:
                    logger.warning(f"Нет подзаголовка '{TEXT}' в заголовке '{HINT2}' в '{title}'")
                    has_error = True
                if g_doc_data.get(title).get(SKVOZ).get(CONTENT).lower() == "да":
                    if g_doc_data.get(title).get(HINT2).get(HINT_CONFIRM) is None:
                        logger.warning(f"Нет подзаголовка '{HINT_CONFIRM}' в заголовке '{HINT2}' в '{title}'")
                        has_error = True
                    if g_doc_data.get(title).get(HINT2).get(PENALTY_FOR_USE) is None:
                        logger.warning(f"Нет подзаголовка '{PENALTY_FOR_USE}' в заголовке '{HINT2}' в '{title}'")
                        has_error = True
                else:
                    if g_doc_data.get(title).get(HINT2).get(HINT_TIME) is None:
                        logger.warning(f"Нет подзаголовка '{HINT_TIME}' в заголовке '{HINT2}' в '{title}'")
                        has_error = True
            
            if g_doc_data.get(title).get(TIME_TO_AP) is None:
                logger.warning(f"Нет заголовка '{TIME_TO_AP}' в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(MAIN_CODES) is None:
                logger.warning(f"Нет заголовка '{MAIN_CODES}' в '{title}'")
                has_error = True
            if g_doc_data.get(title).get(MAIN_CODES).get(TABLES) is None:
                logger.warning(f"Нет таблицы кодов в заголовке '{MAIN_CODES}' в '{title}'")
                has_error = True
            elif g_doc_data.get(title).get(MAIN_CODES).get(TABLES)[0][0] != ['№', 'Код', 'Кс', 'Сектор']:
                logger.warning(f"Таблица кодов в заголовке '{MAIN_CODES}' не соответсвует формату |№|Код|Кс|Сектор| в '{title}'")

            if g_doc_data.get(title).get(CODES_NEEDED) is None:
                logger.warning(f"Нет заголовка '{CODES_NEEDED}' в '{title}'")
                has_error = True
            if g_doc_data.get(title).get(CODES_NEEDED).get(MAJOR) is None:
                logger.warning(f"Нет подзаголовка '{MAJOR}' в заголовке '{CODES_NEEDED}' в '{title}'")
                has_error = True

            if g_doc_data.get(title).get(PENALTY) is None:
                logger.warning(f"Нет заголовка '{PENALTY}' в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(COMMENTS_AND_PHOTOS) is None:
                logger.warning(f"Нет заголовка '{COMMENTS_AND_PHOTOS}' в '{title}'")
                has_error = True

    return has_error


def test_doc(g_doc_datas: dict, add: bool) -> bool:
    logger.info("Проверяю данные дока")
    
    has_error = False
    for g_doc_data in g_doc_datas:
        for title in g_doc_data:
            logger.info(f"Проверяю данные в '{title}'")
            if not add:
                if g_doc_data.get(title).get(LEVEL_ID).get(CONTENT) is None: 
                    logger.warning(f"Нет айди '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(LEVEL_ID).get(CONTENT))
                        logger.info(f"ID: {g_doc_data.get(title).get(LEVEL_ID).get(CONTENT)}")
                    except:
                        logger.warning(f"Неверно прописан айди '{title}'. Впиши только число")
                        has_error = True
            
            if g_doc_data.get(title).get(SKVOZ).get(CONTENT) is None: 
                logger.warning(f"Не прописаны настройки основной/сквозной в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(BONUS).get(CONTENT) is None: 
                logger.warning(f"Не прописаны настройки основной/бонусный в '{title}'")
                has_error = True

            if g_doc_data.get(title).get(LEVEL_TEXT).get(TEXT).get(CONTENT) is None: 
                logger.warning(f"Нет текста задания в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(LEVEL_TEXT).get(NOTES).get(CONTENT) is None:
                logger.warning(f"Нет текста примечаний в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(HINT1).get(TEXT).get(CONTENT) is None:
                logger.warning(f"Нет текста первой подсказки в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(HINT2).get(TEXT).get(CONTENT) is None:
                logger.warning(f"Нет текста второй подсказки в '{title}'")
                has_error = True
            
            if g_doc_data.get(title).get(SKVOZ).get(CONTENT) and g_doc_data.get(title).get(SKVOZ).get(CONTENT).lower() == "да":
                if g_doc_data.get(title).get(HINT1).get(HINT_CONFIRM).get(CONTENT) is None:
                    logger.warning(f"Не прописана выдача первой подсказки по запросу в '{title}'")
                    has_error = True
                if g_doc_data.get(title).get(HINT1).get(PENALTY_FOR_USE).get(CONTENT) is None:
                    logger.warning(f"Не прописан штраф за использование первой подсказки в '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(HINT1).get(PENALTY_FOR_USE).get(CONTENT))
                    except:
                        logger.warning(f"Неверно прописан штраф за использование первой подсказки в '{title}'. Впиши только число")
                        has_error = True

                if g_doc_data.get(title).get(HINT2).get(HINT_CONFIRM).get(CONTENT) is None:
                    logger.warning(f"Не прописана выдача второй подсказки по запросу в '{title}'")
                    has_error = True
                if g_doc_data.get(title).get(HINT2).get(PENALTY_FOR_USE).get(CONTENT) is None:
                    logger.warning(f"Не прописан штраф за использование второй подсказки в '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(HINT2).get(PENALTY_FOR_USE).get(CONTENT))
                    except:
                        logger.warning(f"Неверно прописан штраф за использование второй подсказки в '{title}'. Впиши только число")
                        has_error = True                
            
            else:
                if g_doc_data.get(title).get(HINT1).get(HINT_TIME).get(CONTENT) is None:
                    logger.warning(f"Нет тайминга первой подсказки в '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(HINT1).get(HINT_TIME).get(CONTENT))
                    except:
                        logger.warning(f"Неверно прописан тайминг первой подсказки в '{title}'. Впиши только число")
                        has_error = True
            
                if g_doc_data.get(title).get(HINT2).get(HINT_TIME).get(CONTENT) is None:
                    logger.warning(f"Нет тайминга второй подсказки в '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(HINT2).get(HINT_TIME).get(CONTENT))
                    except:    
                        logger.warning(f"Неверно прописан тайминг второй подсказки в '{title}'. Впиши только число")
                        has_error = True

            if g_doc_data.get(title).get(TIME_TO_AP).get(CONTENT) is None:
                logger.warning(f"Нет тайминга до автоперехода в '{title}'")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get(TIME_TO_AP).get(CONTENT))
                except:
                    logger.warning(f"Неверно прописан тайминг до автоперехода в '{title}'. Впиши только число")
                    has_error = True

            for i, code in enumerate(g_doc_data.get(title).get(MAIN_CODES).get(TABLES)[0][1:]):
                if code[1] == "":
                    logger.warning(f"Нет кода {i+1} в '{title}'")
                    has_error = True
                if code[2] not in ["1", "1+", "2", "2+", "3", "3+", "null"]:
                    logger.warning(f"Неверно прописан кс кода {i+1} в '{title}'")
                    has_error = True
            if g_doc_data.get(title).get(SECTORS):
                for i, sec in enumerate(g_doc_data.get(title).get(SECTORS).get(TABLES)[0][1:]):
                    if sec[1] == "":
                        logger.warning(f"Нет названия сектора {i+1} в '{title}'")
                        has_error = True

            if g_doc_data.get(title).get(CODES_NEEDED).get(MAJOR).get(CONTENT) is None:
                logger.warning(f"Нет количества кодов для взятия в '{title}'")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get(CODES_NEEDED).get(MAJOR).get(CONTENT))
                except:
                    logger.warning(f"Неверно прописано количество кодов для взятия в '{title}'. Впиши только число")
                    has_error = True
            
            if g_doc_data.get(title).get(SPOILER):
                for i, spoiler in enumerate(g_doc_data.get(title).get(SPOILERS)):
                    if i == 0: continue
                    if g_doc_data.get(title).get(SPOILERS).get(f"{SPOILER} {i}:").get(TEXT).get(CONTENT) is None:
                        logger.warning(f"Нет текста спойлера {i} в '{title}'")
                        has_error = True
                    if g_doc_data.get(title).get(SPOILERS).get(f"{SPOILER} {i}:").get(SPOILER_ANSWERS).get(CONTENT) is None:
                        logger.warning(f"Нет ответа спойлера {i} в '{title}'")  
                        has_error = True
            
            if g_doc_data.get(title).get(BONUS_CODES):
                for i, bonus in enumerate(g_doc_data.get(title).get(BONUS_CODES).get(TABLES)[0][1:]):    
                    if bonus[1] == "":
                        logger.warning(f"Нет бонусного кода {i+1} в '{title}'")
                    if bonus[2] not in ["1", "1+", "2", "2+", "3", "3+", "null"]:
                        logger.warning(f"Неверно прописан кс бонусного кода {i+1} в '{title}'")
                    try:
                        int(bonus[3])
                    except:
                        logger.warning(f"Неверно прописан бонус к коду {i+1} в '{title}'. Впиши только число")
                if not g_doc_data.get(title).get(FULL_CAPT_BONUS):
                    logger.warning(f"Нет бонуса на полное взятие бонусов в '{title}'")
                    has_error = True
                elif g_doc_data.get(title).get(FULL_CAPT_BONUS).get(CONTENT) is None:
                    logger.warning(f"Не прописан бонус на полное взятие бонусов в '{title}'")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get(FULL_CAPT_BONUS).get(CONTENT))
                    except:
                        logger.warning(f"Неверно прописан бонус на полное взятие бонусов в '{title}'. Впиши только число")
                        has_error = True

            if g_doc_data.get(title).get(FAKE_CODES):
                for i, bonus in enumerate(g_doc_data.get(title).get(FAKE_CODES).get(TABLES)[0][1:]):    
                    if bonus[1] == "":
                        logger.warning(f"Нет штрафного кода {i+1} в '{title}'")
                    try:
                        int(bonus[2])
                    except:
                        logger.warning(f"Неверно прописан штраф к коду {i+1} в '{title}'. Впиши только число")
            
            if g_doc_data.get(title).get(PENALTY).get(CONTENT) is None:
                logger.warning(f"Не прописан штраф за слив в '{title}'")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get(PENALTY).get(CONTENT))
                except:
                    logger.warning(f"Неверно прописан штраф за слив в '{title}'. Впиши только число") 
                    has_error = True

            if g_doc_data.get(title).get(COMMENTS_AND_PHOTOS).get(CONTENT) is None:
                logger.warning(f"Нет комментариев к '{title}'")

    return has_error