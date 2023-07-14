import requests, time
start_time = time.time()

endpoints = "https://httpbin.org/anything"

get_response = requests.get(endpoints, json={"show_env": 1})
print(get_response.status_code)
print(get_response.text)
print(get_response.json())

print("--- %s seconds ---" % (time.time() - start_time))