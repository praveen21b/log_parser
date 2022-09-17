import os


# check for enter path is file or directory
def path_check(path):
    try:
        if os.path.isdir(path):
            return 'directory'
        elif os.path.isfile(path):
            return 'file'
    except Exception as e:
        raise e

def read_file():
    try:
        pass
    except Exception as e:
        pass
    
def read_file(path):
    file_type = path_check(path)
    if file_type == 'file':
        pass
    elif file_type == 'directory':
        pass


def main():
    # ask for path
    path = input('Please enter file or directory path: ')
    #path = f"r'{path}'"
    file_type = path_check(path)
    return file_type

if __name__ == '__main__':
    print(main())