import json
import codecs
from phones.models import Phone

data = json.load(codecs.open('msk_users.json', 'r', 'utf-8-sig'))

for i in data:
    try:
        Phone.objects.create(
            phone_int=int(i['phone']),
            name=i['name'],
            email=i['mail'],
            note='moscow'
        )
        print(i, 'added')
    except:
        print(i, 'error')
        pass
