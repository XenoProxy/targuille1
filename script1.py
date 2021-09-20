import sys
import os

dir_name = sys.argv[1]
size = float(sys.argv[2])
mb_size = size * (2 ** 20)
total_size = 0
for path, dirs, files in os.walk(dir_name):
    for file in files:
        fp = os.path.join(path, file)
        total_size += os.path.getsize(fp)
        if total_size >= mb_size:
            print(file)
