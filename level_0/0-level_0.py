#!/usr/bin/python3

import requests
import time

payload = {
    'id': 1034,
    'holdthedoor': 'Submit'
}
fails = 0

for items in range(1024):
    r = requests.post('http://158.69.76.135/level0.php', data=payload)
    if r.status_code != 200:
        print(f'Failed to post request number {items}!')
        failed += 1
    else:
        print(f'Succesfully voted {items} times!')

print(f'Failed {fails} number of requests')
