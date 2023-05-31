# import requests
# from dotenv import load_dotenv
# import os
# load_dotenv()



# # Set up the API endpoint and your API key
# api_endpoint = 'https://api.blockchain.com/v3/wallet/new'
# api_key = os.environ.get('API_KEY')

# # Set up the request headers
# headers = {
#     'Content-Type': 'application/json',
#     'X-API-Key': api_key
# }

# # Make the request to get a new address
# response = requests.post(api_endpoint, headers=headers)

# # Check the status code of the response
# if response.status_code == 200:
#     # If the request was successful, extract the address from the response
#     data = response.json()
#     deposit_address = data['address']
#     print(deposit_address)
# else:
#     # If the request was unsuccessful, print the error message
#     print(response.text)