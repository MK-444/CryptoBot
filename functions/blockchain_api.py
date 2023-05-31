# import requests
# import json

# # Set your API Key and Secret Key
# api_key = "b266f461-ba4a-4626-9f15-00095f243481"
# secret_key = "eyJhbGciOiJFUzI1NiIsInR5cCI6IkFQSSJ9.eyJhdWQiOiJtZXJjdXJ5IiwidWlkIjoiMTFjZWI5YWMtNmMxMC00ZWU4LThkNTEtNTEyODcyMjY5MTVlIiwiaXNzIjoiYmxvY2tjaGFpbiIsInJkbyI6ZmFsc2UsImlhdCI6MTY3MjQxMDkzOSwianRpIjoiYjI2NmY0NjEtYmE0YS00NjI2LTlmMTUtMDAwOTVmMjQzNDgxIiwic2VxIjo1OTg5OTQzLCJ3ZGwiOnRydWV9.IL38BblUYKZjt+U8JwEyr0YnuZDpdDzePCrVTPitr3jrB1LgJXHMKjmz1sOIUpf1TfNZP6rXbYYanj4n8WYNMs8="

# # Set the endpoint for the API
# endpoint = "https://api.blockchain.com/v3/wallet/new"

# # Set the headers for the request
# headers = {
#     "Content-Type": "application/json",
#     "x-api-key": api_key,
#     "x-api-secret": secret_key,
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    
# }

# # Set the request data
# data = {
#     "password": "15091998dasha"
# }

# # Send the request to the API
# response = requests.post(endpoint, headers=headers, data=json.dumps(data))

# # Print the response
# print(response.text)
