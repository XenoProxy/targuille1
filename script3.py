import psutil
import os

path = 'temp/investigation'
proc_list = []

for proc in psutil.process_iter():
    try:
        name = proc.name()
        pid = proc.pid
        if not os.path.exists(path):
            os.makedirs(path)
        if 'java' in name:
            with open(
                    os.path.join(path, 'java_pid_list.txt'),
                    'a+', encoding='utf-8') as file:
                file.write(f'PID: {pid}   NAME: {name}' + '\n')
        with open(
                os.path.join(path, 'pid_list.txt'),
                'a+', encoding='utf-8') as file:
            file.write(f'PID: {pid}   NAME: {name}' + '\n')
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
