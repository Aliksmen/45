import os

for root, dirs, files in os.walk('/home/admin33', topdown=False):
    for name in files:
        f = os.path.join(root, name)
        if os.path.getsize(f) == filesize:
            os.remove(f)

