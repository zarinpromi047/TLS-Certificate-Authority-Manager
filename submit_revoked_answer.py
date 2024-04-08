import requests
import json
 
# The dictionary you want to send to the API
data = {
    6: 'N',
    9: 'N',
    28:'Y'
}
 
# Convert the dictionary to a JSON string
json_data = json.dumps(data)
 
# The endpoint URL
url = 'http://129.82.44.147:10300/submit-answer/revoked-status?sid=1'
 


# Make the POST request with the JSON payload
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
 
# Check if the request was successful
if response.status_code == 200:
    print(response.content)
else:
    print('An error occurred.', response.text)
