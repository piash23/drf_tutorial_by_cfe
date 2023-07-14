import requests, time
start_time = time.time()

endpoints = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoints, json={"show_env": 1})
print(get_response.status_code)
print(type(get_response.text))
print(type(get_response.json()))

print("--- %s seconds ---" % (time.time() - start_time))