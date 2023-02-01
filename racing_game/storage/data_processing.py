
class DataProcessing:

    @staticmethod
    def save_lap_time(data, filename):
        file = open(filename, "a")
        file.write(str(data) + "\n")
        file.close()

    @staticmethod
    def save_match_time(data, filename):
        file = open(filename, "a")
        file.write(str(data) + "\n")
        file.close()

    @staticmethod
    def load_lap_times(filename):
        with open(filename, "r") as file:
            lap_list = [x.rstrip() for x in file]

        lap_list.sort()

        return lap_list

    @staticmethod
    def load_match_times(filename):
        with open(filename, "r") as file:
            match_list = [x.rstrip() for x in file]

        match_list.sort()

        return match_list
