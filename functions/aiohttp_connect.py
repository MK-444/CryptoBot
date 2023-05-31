# import aiohttp 
# from django.db import transaction
# from AdminDjango.api.models import *

# async def send_data_to_server(data):
#     async with aiohttp.ClientSession() as session:
#         async with session.post('http://127.0.0.1:8000', json=data) as resp:
#             if resp.status == 200:
#                 print('Data sent successfully')
#             else:
#                 print('Error sending data')


# # Assuming you have a model called "Person" with fields "name" and "age"


# @transaction.atomic
# def save_person(user_id):
#     person = UserModel(user_id)
#     person.save()

# # Now you can call save_person from your aiogram bot code to save a new Person object to the database
