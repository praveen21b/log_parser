import re

def time_stamp_float_type(time_stamp_list:list)->list:
    """Changes list of strings to list of foating"""
    try:
        change_datatype = []
        for time_stamp in time_stamp_list:
            change_datatype.append(float(time_stamp))
        return change_datatype

    except Exception as e:
        raise e

def get_time_stamp_list(line_list:list)->list:
    """Check the string with the regex pattern and get time stamp list
        ##### time stamp r'\d{10}\.\d{3}'
    """
    time_stamp_list = []
    try:
        time_stamp_regex = r'\d{10}\.\d{1,3}'
        for line in line_list:
            time_stamps = re.findall(time_stamp_regex, line)
            time_stamp_list.extend((time_stamps))
        return time_stamp_float_type(time_stamp_list)
    except Exception as e:
        raise (e)
