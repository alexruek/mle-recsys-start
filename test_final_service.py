import requests

# URL сервисов
recommendations_url = "http://127.0.0.1:8000"
events_store_url = "http://127.0.0.1:8020"

# Заголовки запроса
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# 1. Проверяем онлайн-рекомендации до добавления событий
params = {"user_id": 1291248, "k": 3}
resp = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
online_recs_before = resp.json()

# 2. Добавляем событие (item_id = 17245) для пользователя 1291248 в Event Store
params = {"user_id": 1291248, "item_id": 17245}
requests.post(events_store_url + "/put", headers=headers, params=params)

# 3. Проверяем онлайн-рекомендации после добавления события
params = {"user_id": 1291248, "k": 3}
resp = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
online_recs_after = resp.json()

# Выводим результаты
print("Рекомендации до добавления события:", online_recs_before)
print("Рекомендации после добавления события:", online_recs_after)