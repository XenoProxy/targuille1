import psutil
import os

path = 'temp/investigation'
proc_list = []

for proc in psutil.process_iter():
    try:
        name = proc.name()
        pid = proc.pid
        if 'python' in name:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(
                    os.path.join(path, f'access_{pid}.txt'),
                    'a+', encoding='utf-8') as file:
                file.write('')
            print(name, ' : ', pid)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
