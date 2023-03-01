import requests as requests

URL = "https://www.jsonkeeper.com/b/0MZI"

result = requests.get(URL).json()

for i in range(len(result)):
    if "state" not in result[i]:
        continue
    print(result[i]["state"])




