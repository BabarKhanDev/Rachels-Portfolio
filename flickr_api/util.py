import configparser


def load_config():
    config_object = configparser.ConfigParser()
    with open("config.ini", "r") as file_object:
        config_object.read_file(file_object)
        return config_object