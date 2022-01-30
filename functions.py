import math
import json
from datetime import datetime

data_file = "data.json"

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def getDate():
    now = datetime.today()
    date_time = now.strftime("%d.%m.%Y")
    return date_time

def getData(key: str):
    file = open(data_file)
    data = json.load(file)
    file.close()
    res = data[key]
    return res