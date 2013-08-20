import logging

def check_value(data_dict, value):
    try:
        return data_dict[value] > 10
    except KeyError:
        logging.error("data does not contain '%s'", value)
    return False
