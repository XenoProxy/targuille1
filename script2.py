from datetime import datetime

for i in range(10):
    curr_time = datetime.today()
    with open(f'test_{curr_time}_{i+1}.txt', 'a+', encoding='utf-8') as file:
        file.write(curr_time.strftime('%Y-%m-%d-%H-%M-%S') + '\n')
