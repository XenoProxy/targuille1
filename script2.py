import random
import string
from datetime import datetime

for i in range(10):
    curr_time = datetime.today()
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for y in range(1000))
    with open(f'test_{curr_time}_{i+1}.txt', 'a+', encoding='utf-8') as file:
        file.write(rand_string)

# To schedule it to run every 6 hours we can use cron.
# Example: 0 */6 * * * python ~/targuille1/script1.py
