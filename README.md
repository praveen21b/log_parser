# log_parser
Script to parse log file/s, extract useful data, and save this data in json format

## logs
Sample data of a log file
```
1157689324.156 1372 10.105.21.199 TCP_MISS/200 399 GET http://www[.]google-analytics[.]com/__utm.gif? badeyek DIRECT/66.102.9.147 image/gif
```

where
```
Field 1: 1157689324.156 [Timestamp in seconds since the epoch]
```
```
Field 2: 1372 [Response header size in bytes]
```
```
Field 3: 10.105.21.199 [Client IP address]
```
```
Field 4: TCP_MISS/200 [HTTP response code]
```
```
Field 5: 399 [Response size in bytes]
```
```
Field 6: GET [HTTP request method]
```
```
Field 7: http://www.google-analytics.com/__utm.gif? [URL]
```
```
Field 8: badeyek [Username]
```
```
Field 9: DIRECT/66.102.9.147 [Type of access/destination IP address]
```
```
Field 10: image/gif [Response type]
```

## Parsing operations
1. Input Data
    - Path to one or more plain text files, or a directory
2. Operations
    - Most frequent IP (Parsed all the ips)
    - Least frequent IP (Took only last element of sorted frequencny list)
    - Events per second
    - Total amount of bytes exchanged
3. Output
    - Path to a file to save output in plain text JSON format

## Dockerfile operations
    - Create docker container: 
    ```docker build -t log-parser```
    - Running container image in interactive mode: 
    ```docker run -t -i log-parser```
