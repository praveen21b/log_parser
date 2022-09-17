import os
import re

def path_check(file_path):

    """Check for enter path is file or directory"""

    try:
        if os.path.isdir(file_path):
            return 'directory'
        elif os.path.isfile(file_path):
            return 'file'
    except Exception as e:
        raise e


def read_file(file_path):
    """ Reads file of a given path or address"""
    try:
        with open(file_path,encoding='utf-8') as f:
            return (f.readlines())
    except Exception as e:
        raise e


def read_directory(file_path):
    """list of files in a directory"""
    try:
        return os.listdir(file_path)
    except Exception as e:
        raise e

def create_file_path(base_path,file_list):
    """Takes file list and creates 
        list of file addresses for each file in the directory"""
    address_list = []
    try:
        for file in file_list:
            address_list.append(os.path.join(base_path, file))
            return address_list
    except Exception as e:
        raise e


def get_ip_list(line_list):
    """Check the string with the regex pattern and get ip list
        # ip address r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    """
    ip_list = []
    try:
        ip_regex = r'\d{10}\.\d{1,3}'
        ips = re.findall(ip_regex, line_list)
        ip_list.extend(ips)
        return ip_list
    except Exception as e:
        raise e

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

# def read_file(path):
#     file_type = path_check(path)
#     if file_type == 'file':
#         pass
#     elif file_type == 'directory':
#         pass


def main():
    # ask for path
    file_path = input('Please enter file or directory path: ')
    #path = f"r'{path}'"

    # file_type = path_check(file_path)
    # if file_type == 'file':
    #     pass
    # elif file_type == 'directory':
    #     pass



if __name__ == '__main__':
    print(main())