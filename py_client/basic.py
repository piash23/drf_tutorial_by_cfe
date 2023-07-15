import requests, time
start_time = time.time()

endpoints = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoints, params={"query": "hello world"} ,json={"comment": "api product title"})
print(get_response.status_code)
print(get_response.text)
print(get_response.json())

print("--- %s seconds ---" % (time.time() - start_time))