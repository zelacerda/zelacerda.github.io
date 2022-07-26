from browser.local_storage import storage


def get_value(key):
    value = storage.get(key)
    if not value:
        return 0
    else:
        return int(value)


def set_value(key, value):
    storage[key] = str(value)


def get_and_update_record(score):
    record = get_value("record")
    if not record or score > int(record):
        storage["record"] = str(score)
    return record


def increment_key(key, amount=1):
    value = storage.get(key)
    if not value:
        storage[key] = str(amount)
    else:
        storage[key] = str(int(value) + amount)


def set_guesses(guesses):
    storage["guesses"] = " ".join(guesses)


def get_guesses():
    return storage["guesses"].split()


def get_area():
    return storage["area"]


def set_word_counts(values):
    keys = ["w3", "w4", "w5", "w6", "w7", "w8"]
    for k, v in zip(keys, values):
        storage[k] = str(v)


def get_word_counts():
    keys = ["w3", "w4", "w5", "w6", "w7", "w8"]
    values = []
    for k in keys:
        values.append(get_value(k))
    return values


def update_stats(counts, score):
    keys = ["t3", "t4", "t5", "t6", "t7", "t8"]
    for i, key in enumerate(keys):
        increment_key(key, amount=counts[i])
    increment_key("games")
    increment_key("sum", amount=score)


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
    for key in ["t3", "t4", "t5", "t6", "t7", "t8"]:
        counts.append(get_value(key))
    result["counts"] = counts

    if sum(counts) == 0:
        pcts = counts
    else:
        pcts = [round(i / sum(counts) * 100) for i in counts]
    result["pcts"] = pcts

    return result
