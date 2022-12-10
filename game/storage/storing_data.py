
def save_lap_time(data):
    file = open("lap_times.txt", "a")
    file.write(str(data) + ", ")
    file.close()


def load_lap_times():
    file = open("lap_times.txt", "r")
    data = file.read()
    split_data = data.split()

    return split_data


def save_match_time(data):
    file = open("match_times.txt", "a")
    file.write(str(data) + ", ")
    file.close()


def load_match_times():
    file = open("match_times.txt", "r")
    data = file.read()
    split_data = data.split()

    return split_data
