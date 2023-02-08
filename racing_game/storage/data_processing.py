class DataProcessing:

    @staticmethod
    def save_time(data, filename):
        file = open(filename, "a")
        file.write(str(data) + "\n")
        file.close()

    @staticmethod
    def load_time(filename):
        with open(filename, "r") as file:
            time_list = [x.rstrip() for x in file]

        time_list.sort()

        return time_list

    # WINS ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def save_wins(data, filename):
        file = open(filename, "a")
        file.write(data + "\n")
        file.close()

    @staticmethod
    def load_wins(filename):
        with open(filename, "r") as file:
            win_list = [x.rstrip() for x in file]

        return win_list
