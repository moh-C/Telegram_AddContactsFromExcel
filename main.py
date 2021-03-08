from telethon.sync import TelegramClient
from telethon import functions, types
import pandas as pd
import numpy as np
from time import sleep
from credentials import api_id, api_hash


data = pd.read_excel('./420103020.xlsx')
name = 'h'

async with TelegramClient(name, api_id, api_hash) as client:
    for index, row in data.iterrows():
        if row['ID'] is not np.nan:
            
            print(f"ID: {row['ID']}")
            print(f"First Name: {row['FirstName']}")
            print(f"Last Name: {row['LastName']}")
            
            result = await client(functions.contacts.AddContactRequest(
                id=str(row['ID']),
                first_name=str(row['FirstName']),
                last_name=str(row['LastName']),
                phone='',
                add_phone_privacy_exception=True
            ))
