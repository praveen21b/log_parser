import os

def path_check(file_path:str)->str:
    """Check for enter path is file or directory"""
    try:
        if os.path.isdir(file_path):
            return 'directory'
        elif os.path.isfile(file_path):
            return 'file'

    except Exception as e:
        raise e


def read_file(file_path:str)->list:
    """ Reads file of a given path or address"""
    try:
        with open(file_path,encoding='utf-8') as f:
            return (f.readlines())
    except Exception as e:
        raise e


def read_directory(file_path:str)->list:
    """list of files in a directory"""
    try:
        return os.listdir(file_path)
    except Exception as e:
        raise e

def create_file_path(base_path:str,file_list:list)->list:
    """Takes file list and creates 
        list of file addresses for each file in the directory"""
    address_list = []
    try:
        for file in file_list:
            address_list.append(os.path.join(base_path, file))
            return address_list
    except Exception as e:
        raise e

def directoty_read(file_path:str)->list:
    """ Reads file or files of a directory """
    file_lines_list = []

    try:
        file_type = path_check(file_path)
        if file_type == 'file':
            file_lines_list.extend(read_file(file_path))
        elif file_type == 'directory':
            # file list in a directory
            file_list = read_directory(file_path)
            # get the list of addresses for each file
            file_address_list = create_file_path(file_path,file_list)
            for address in file_address_list:
                file_lines_list.extend(read_file(file_path))
        return file_lines_list

    except Exception as e:
        raise e