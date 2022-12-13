def save_lap_time(data):
    file = open("lap_times.txt", "a")
    file.write(str(data) + "\n")
    file.close()


def load_lap_times():
    with open("lap_times.txt", "r") as file:
        lap_list = [x.rstrip() for x in file]

    lap_list.sort()

    return lap_list


def save_match_time(data):
    file = open("match_times.txt", "a")
    file.write(str(data) + "\n")
    file.close()


def load_match_times():
    with open("match_times.txt", "r") as file:
        match_list = [x.rstrip() for x in file]

    match_list.sort()

    return match_list
