import re
import csv

# def finding_delimiter(line):
#     for i in (line):
#     #print(len(i))
#         if len(i) > 1 :
#             #print(type(i))
#             line = i
#             break
#     sniffer = csv.Sniffer()
#     dialect = sniffer.sniff(line)
#     return (dialect.delimiter) # returns delimter


def get_bytes_int(lists:list):
    """ Converts list of string bytes to int bytes"""
    new = []
    try:
        for ele in lists:
            # ele.strip()
            new.append(int(ele))
        return new
    
    except Exception as e:
        raise e


def get_bytes_list(line_list):
    """Check the string with the regex pattern and get ip list
        # bytes r'\s\d{1,8}\s'
        (\s for space: can be changed depending on the delimiter)
    """
    bytes_list = []
    try:
        bytes_regex = r'\s\d{1,8}\s'
        time_stamps = re.findall(bytes_regex, line_list)
        bytes_list.extend(time_stamps)
        return get_bytes_int(bytes_list)

    except Exception as e:
        raise e