import json
import requests
from config import URL


fields = [{'title': 'Love', 'value': 'Ferrets, :beer:, LEGO'},
          {'title': 'From', 'value': 'Philippines :flag-ph:'}]

data = json.dumps({'attachments': [{
    'pretext': 'Nice to meet you!!',
    'author_name': 'Cornellius Dagmang',
    'author_link': 'https://twitter.com/yocorny03/',
    'text': '*THANK YOU* for coming to my talk !:tada:'
            'Please give me *feedback* about this talk :bow:',
    'fields': fields,
}]})
requests.post(URL, data=data)