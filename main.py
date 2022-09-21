from log_parser import directoty_read
from bytes_int import get_bytes_list
from ip_lists import get_ip_list
from time_stamp import get_time_stamp_list
from collections import Counter
import json
import os
from save_result import save_file

def main():
    """ Function ask inputs from user and save result in the specified location"""
    try:
        # ask for path
        file_path = (input('Please enter file or directory path: '))
        #os.chdir(file_path)
        #path = f"r'{path}'"
        output_path = input('Enter the address to save the result: ')

        file_lines_list = directoty_read(file_path)

        # getting bytes
        total_bytes = sum(get_bytes_list(file_lines_list))

        # getting ip_list, max, and min freq ip address
        dicts = Counter(get_ip_list(file_lines_list))
        most_frequent_ip = dicts.most_common(1)[0][0]
        # only taking last least_frequent_ip
        least_frequent_ip = dicts.most_common()[-1][0]
        
        # ip_list = get_ip_list(file_lines_list)
        # most_frequent_ip = max(ip_list, key=ip_list.count)
        # least_frequent_ip = min(ip_list, key=ip_list.count)

        # total events per seconds
        time_lists = get_time_stamp_list(file_lines_list)
        total_events = len(time_lists)
        time_duration = max(time_lists) - min(time_lists)
        events_per_second = total_events / time_duration

        # # final result
        res = {}
        res['most_frequent_ip'] = most_frequent_ip
        res['least_frequent_ip'] = least_frequent_ip
        res['events_per_second'] = events_per_second
        res['total_bytes'] = total_bytes
        
        #return json.dumps(res, indent = 4)
        return save_file(output_path,res)
        
    except Exception as e:
        raise (e)



if __name__ == '__main__':
    print(main())