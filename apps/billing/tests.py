from pprint import pprint

import requests
from django.test import TestCase


# Create your tests here.
def get_payme_card():
    ID = '64d63b7d7d8d42482ae691d6'
    SEC_KEY = 'miCQXGT4sYmc1%v5WrBxt8Coo?42P6QiCJih'
    AUTHORIZATION = {'X-Auth': '{}:{}'.format(ID, SEC_KEY)}
    data = {
        "id": 123,
        "method": "cards.create",
        "params": {
            "card": {
                "number": "8600060921090842",
                "expire": "0399"
            },
            "save": True
        }
    }
    res = requests.post('https://checkout.test.paycom.uz/api', data=data, headers=AUTHORIZATION)
    return res.json()


if __name__ == '__main__':
    res = get_payme_card()
    pprint(res)
