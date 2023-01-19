import requests
import json

status = 'available'

res = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus?status={status}', headers={'accept':'application/json'})

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))

#Тип запроса POST
#res = requests.post(url, headers=headers, data=data)
#добавление питомца
info = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "string",
  "photoUrls": [
    "Dandy's photo"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_post = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},data=json.dumps(info, ensure_ascii=False))

print(res_post.status_code)
print(res_post.json())


#обновление карточки питомца PUT
new_info = {
  "id": 9223372036854719731,
  "category": {
    "id": 0,
    "name": "Dandy"
  },
  "status": "available"
}

res_put = requests.put(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json', 'Content-Type': 'application/json'},data=json.dumps(info, ensure_ascii=False))

print(res_put.status_code)
print(res_put.json())
