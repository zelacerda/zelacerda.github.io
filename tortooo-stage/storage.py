from browser.local_storage import storage


def update_score(score):
    storage['score'] = str(score)


def update_record(score):
    record = storage.get("record")
    if not record or score > int(record):
        storage["record"] = str(score)


def increment_key(key, amount=1):
    value = storage.get(key)
    if not value:
        storage[key] = str(amount)
    else:
        storage[key] = str(int(value) + amount)


def get_value(key):
    value = storage.get(key)
    if not value:
        return 0
    else:
        return int(value)


def set_value(key, value):
    storage[key] = str(value)


def get_stats():
    result = dict()

    result["record"] = get_value("record")

    games = get_value("games")
    sum_score = get_value("sum")

    if games == 0:
        mean = 0
    else:
        mean = round(sum_score / games)

    result["mean"] = mean
    result["games"] = games

    counts = list()
    for key in ["c3", "c4", "c5", "c6", "c7", "c8"]:
        counts.append(get_value(key))
    result["counts"] = counts

    if sum(counts) == 0:
        pcts = counts
    else:
        pcts = [round(i / sum(counts) * 100) for i in counts]
    result["pcts"] = pcts

    return result
