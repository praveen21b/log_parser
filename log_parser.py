import os

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

    file_type = path_check(file_path)
    if file_type == 'file':
        pass
    elif file_type == 'directory':
        pass

if __name__ == '__main__':
    print(main())