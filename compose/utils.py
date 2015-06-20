import json
import hashlib
import threading


def json_hash(obj):
    dump = json.dumps(obj, sort_keys=True, separators=(',', ':'))
    h = hashlib.sha256()
    h.update(dump)
    return h.hexdigest()


def parallel(jobs):
    threads = []

    for job in jobs:
        threads.append(threading.Thread(target=job))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

