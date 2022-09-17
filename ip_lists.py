import re

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