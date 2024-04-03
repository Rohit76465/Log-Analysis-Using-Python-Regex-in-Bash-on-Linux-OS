#!/usr/bin/env python3

import re
import operator
import csv

error_counter = {}
error_user = {}
info_user = {}

#This function will read each line of the syslog.log file and check if it is an error or an info message.
def search_file():
    with open('syslog.log', "r") as myfile:
     for line in myfile:
        if " ERROR " in line:
            find_error(line)
            add_user_list(line, 1)
        elif " INFO " in line:
            add_user_list(line, 2)
    return


#If it is an error it will read the error from the line and increment into the dictionary
def find_error(str):
    match = re.search(r"(ERROR [\w\' ]*) ", str)
    if match is not None:
        aux = match.group(0).replace("ERROR ", "").strip()
        if not aux in error_counter:
            error_counter[aux] = 1
        else:
            error_counter[aux] += 1
    return 

#Depending on the flag variable's value, this function will read the user name from the str (line) and add to the error_user or info_user dictionaries to count the error or info messages by users.
def add_user_list(str, flag):
    match = re.search(r'(\([\w\.]*\))', str)
    user = match[1]
    userA = user.strip("()")
    if flag == 1:
        if not userA in error_user:
            error_user[userA] = 1
        else:
            error_user[userA] += 1
    elif flag == 2:
        if not userA in info_user:
            info_user[userA] = 1
        else:
            info_user[userA] += 1
    return

#This function will read the dictionary and sort it. 
def sort_list(flag, dictio):
    if flag == 1:
        s = sorted(dictio.items(), key=operator.itemgetter(1), reverse=True)
    elif flag == 2:
        s = sorted(dictio.items(), key=operator.itemgetter(0))
    return s

#This function takes the key of info_user dictionary as keyV. Then this keyV is checked if it is the same one as their in error_user. If so, then value of this key from error_user dictionary is returned.
def getErrValue(keyV):
    for key, value in error_user:
        if key is keyV:
            return value
    return 0

#This function writes both csv files.
def write_csv(flag):
    if flag == 1:
        with open('error_message.csv', 'w', newline='') as output:
            fieldnames = ['Error', 'Count']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in error_counter:
                csvw.writerow({'Error': key, 'Count': value})
                
    if flag == 2:
        with open('user_statistics.csv', 'w', newline='') as output:
            fieldnames = ['Username', 'INFO', 'ERROR']
            csvw = csv.DictWriter(output, fieldnames=fieldnames)
            csvw.writeheader()
            for key, value in info_user:
                valError = getErrValue(key)
                csvw.writerow({'Username': key, 'INFO': value, 'ERROR': valError})
    
    return

#This function adds a key with value as 0 , if the key is present in only either of error_user or info_user dictionary.
def add_zeros():
    for user in error_user.keys():
        if user not in info_user:
            info_user[user] = 0
    for user in info_user.keys():
        if user not in error_user:
            error_user[user] = 0
    return


#Program starts from here.
search_file()
add_zeros()
error_counter = sort_list(1, error_counter)
error_user = sort_list(2, error_user)
info_user = sort_list(2, info_user)
write_csv(1)
write_csv(2)