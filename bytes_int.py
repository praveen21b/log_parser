import re

def get_bytes_int(lists:list):
    """ Converts list of string bytes to int bytes"""
    new = []
    for ele in lists:
        # ele.strip()
        new.append(int(ele))
    return new

def get_bytes_list(line_list):
    """Check the string with the regex pattern and get ip list
        # bytes r'\s\d{1,8}\s'
    """
    bytes_list = []
    try:
        bytes_regex = r'\s\d{1,8}\s'
        time_stamps = re.findall(bytes_regex, line_list)
        bytes_list.extend(time_stamps)
        return get_bytes_int(bytes_list)
    except Exception as e:
        raise e