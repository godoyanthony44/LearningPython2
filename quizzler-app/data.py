import requests
from html import unescape

paramters = {
    'amount': 10,
    'category': 18,
    'type': 'boolean'

}
response = requests.get(url='https://opentdb.com/api.php?', params=paramters)
response.raise_for_status()

question_data = response.json()['results']
word = '&quot;'
for question in question_data:
    question['question'] = unescape(question['question'])
