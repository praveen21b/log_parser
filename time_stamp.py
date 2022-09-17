import re

def get_time_stamp_list(line_list):
    """Check the string with the regex pattern and get ip list
        # time stamp r'\d{10}\.\d{3}'
    """
    time_stamp_list = []
    try:
        time_stamp_regex = r'\d{10}\.\d{1,3}'
        time_stamps = re.findall(time_stamp_regex, line_list)
        time_stamp_list.extend(time_stamps)
        return time_stamp_list
    except Exception as e:
        raise e