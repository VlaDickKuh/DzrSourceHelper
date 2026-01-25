def check_codes_repeat(g_doc_datas: dict):
    for g_doc_data in g_doc_datas:
        for title in g_doc_data:
            for i, code in enumerate(g_doc_data.get(title).get("Основные коды уровня:").get("tables")[0][1:]):
                pass


def test_doc(g_doc_datas: dict, add: bool) -> bool:
    has_error = False
    print("Проверяю гугл док")
    for g_doc_data in g_doc_datas:
        for title in g_doc_data:
            print(f"Проверяю '{title}'")
            if not add:
                if g_doc_data.get(title).get("ID Уровня:") is None:
                    print(f"Нет айди задания {title}")
                    has_error = True
                elif g_doc_data.get(title).get("ID Уровня:").get("content") is None: 
                    print(f"Нет айди задания {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("ID Уровня:").get("content"))
                        print(f"ID: {g_doc_data.get(title).get("ID Уровня:").get("content")}")
                    except:
                        print(f"Неверно прописан айди задания {title}. Впиши только число")
                        has_error = True
            if g_doc_data.get(title).get("Сквозной:").get("content") is None: 
                print(f"Не прописаны настройки основной/сквозной в уровне {title}")
                has_error = True

            if g_doc_data.get(title).get("Текст уровня:").get("Текст:").get("content") is None: 
                print(f"Нет текста задания {title}")
                has_error = True
            
            if g_doc_data.get(title).get("Текст уровня:").get("Примечания:").get("content") is None:
                print(f"Нет текста примечаний задания {title}")
                has_error = True
            
            if g_doc_data.get(title).get("Подсказка 1:").get("Текст:").get("content") is None:
                print(f"Нет текста первой подсказки в задании {title}")
                has_error = True
            
            if g_doc_data.get(title).get("Подсказка 2:").get("Текст:").get("content") is None:
                print(f"Нет текста второй подсказки в задании {title}")
                has_error = True
            
            if g_doc_data.get(title).get("Сквозной:").get("content").lower() == "да":
                if g_doc_data.get(title).get("Подсказка 1:").get("Выдавать по запросу:").get("content") is None:
                    print(f"Не прописана выдача первой подсказки по запросу в задании {title}")
                    has_error = True
                if g_doc_data.get(title).get("Подсказка 1:").get("Штраф за использование:").get("content") is None:
                    print(f"Не прописан штраф за использование первой подсказки в задании {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("Подсказка 1:").get("Штраф за использование:").get("content"))
                    except:
                        print(f"Неверно прописан штраф за использование первой подсказки в задании {title}. Впиши только число")
                        has_error = True

                if g_doc_data.get(title).get("Подсказка 2:").get("Выдавать по запросу:").get("content") is None:
                    print(f"Не прописана выдача второй подсказки по запросу в задании {title}")
                    has_error = True
                if g_doc_data.get(title).get("Подсказка 2:").get("Штраф за использование:").get("content") is None:
                    print(f"Не прописан штраф за использование второй подсказки в задании {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("Подсказка 2:").get("Штраф за использование:").get("content"))
                    except:
                        print(f"Неверно прописан штраф за использование второй подсказки в задании {title}. Впиши только число")
                        has_error = True                
            
            else:
                if g_doc_data.get(title).get("Подсказка 1:").get("Время до подсказки:").get("content") is None:
                    print(f"Нет тайминга первой подсказки в задании {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("Подсказка 1:").get("Время до подсказки:").get("content"))
                    except:
                        print(f"Неверно прописан тайминг первой подсказки в задании {title}. Впиши только число")
                        has_error = True
            
                if g_doc_data.get(title).get("Подсказка 2:").get("Время до подсказки:").get("content") is None:
                    print(f"Нет тайминга второй подсказки в задании {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("Подсказка 2:").get("Время до подсказки:").get("content"))
                    except:    
                        print(f"Неверно прописан тайминг второй подсказки в задании {title}. Впиши только число")
                        has_error = True

            if g_doc_data.get(title).get("Время до окончания уровня:").get("content") is None:
                print(f"Нет тайминга до автоперехода в задании {title}")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get("Время до окончания уровня:").get("content"))
                except:
                    print(f"Неверно прописан тайминг до автоперехода в задании {title}. Впиши только число")
                    has_error = True

            if g_doc_data.get(title).get("Комментарий и фото кодов:").get("content") is None:
                print(f"Нет комментариев к заданию {title}")
                has_error = True

            if g_doc_data.get(title).get("Основные коды уровня:") is None:
                print(f"Нет таблицы основных кодов уровня {title}")
                has_error = True
            else:
                for i, code in enumerate(g_doc_data.get(title).get("Основные коды уровня:").get("tables")[0][1:]):
                    if code[1] == "":
                        print(f"Нет кода {i+1} в задании {title}")
                        has_error = True
                    if code[2] not in ["1", "1+", "2", "2+", "3", "3+", "null"]:
                        print(f"Неверно прописан кс кода {i+1} в задании {title}")
                        has_error = True
            if g_doc_data.get(title).get("Сектора на уровне:"):
                for i, sec in enumerate(g_doc_data.get(title).get("Сектора на уровне:").get("tables")[0][1:]):
                    if sec[1] == "":
                        print(f"Нет названия сектора {i+1} в задании {title}")
                        has_error = True

            if g_doc_data.get(title).get("Количество кодов для взятия:").get("Вышка:").get("content") is None:
                print(f"Нет количества кодов для взятия уровня {title}")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get("Количество кодов для взятия:").get("Вышка:").get("content"))
                except:
                    print(f"Неверно прописано количество кодов для взятия в задании {title}. Впиши только число")
                    has_error = True
            
            if g_doc_data.get(title).get("Спойлеры:"):
                for i, spoiler in enumerate(g_doc_data.get(title).get("Спойлеры:")):
                    if g_doc_data.get(title).get("Спойлеры:").get(f"Спойлер {i+1}:").get("Текст:").get("content") is None:
                        print(f"Нет текста спойлера {i+1} в задании {title}")
                        has_error = True
                    if g_doc_data.get(title).get("Спойлеры:").get(f"Спойлер {i+1}:").get("Ответы на спойлер:").get("content") is None:
                        print(f"Нет ответа спойлера {i+1} в задании {title}")  
                        has_error = True
            
            if g_doc_data.get(title).get("Бонусные коды уровня:"):
                for i, bonus in enumerate(g_doc_data.get(title).get("Бонусные коды уровня:").get("tables")[0][1:]):    
                    if bonus[1] == "":
                        print(f"Нет бонусного кода {i+1} в задании {title}")
                    if bonus[2] not in ["1", "1+", "2", "2+", "3", "3+", "null"]:
                        print(f"Неверно прописан кс бонусного кода {i+1} в задании {title}")
                    try:
                        int(bonus[3])
                    except:
                        print(f"Неверно прописан бонус к коду {i+1} к заданию {title}. Впиши только число")
                if not g_doc_data.get(title).get("Бонус за полное взятие:"):
                    print(f"Нет бонуса на полное взятие бонусов к заданию {title}")
                    has_error = True
                elif g_doc_data.get(title).get("Бонус за полное взятие:").get("content") is None:
                    print(f"Не прописан бонус на полное взятие бонусов к заданию {title}")
                    has_error = True
                else:
                    try:
                        int(g_doc_data.get(title).get("Бонус за полное взятие:").get("content"))
                    except:
                        print(f"Неверно прописан бонус на полное взятие бонусов к заданию {title}. Впиши только число")
                        has_error = True
            if g_doc_data.get(title).get("Штрафные коды уровня:"):
                for i, bonus in enumerate(g_doc_data.get(title).get("Штрафные коды уровня:").get("tables")[0][1:]):    
                    if bonus[1] == "":
                        print(f"Нет штрафного кода {i+1} в задании {title}")
                    try:
                        int(bonus[2])
                    except:
                        print(f"Неверно прописан штраф к коду {i+1} к заданию {title}. Впиши только число")
            if g_doc_data.get(title).get("Штраф за слив:").get("content") is None:
                print(f"Не прописан штраф за слив в задании {title}")
                has_error = True
            else:
                try:
                    int(g_doc_data.get(title).get("Штраф за слив:").get("content"))
                except:
                    print(f"Неверно прописан штраф за слив в задании {title}. Впиши только число") 
                    has_error = True

            if g_doc_data.get(title).get("Бонусный:").get("content") is None: 
                print(f"Не прописаны настройки основной/бонусный в уровне {title}")
                has_error = True

    return has_error