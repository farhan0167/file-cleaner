#!/usr/bin/env python3
import os
import time
import datetime
import argparse
import re

parser = argparse.ArgumentParser(description='Process arguments for file removal Manual')
parser.add_argument('--days', type=int, default=365,
                    help='Number of days to look behind to consider a file outdated. Default value is 365 days')
parser.add_argument('--target', type=str, default=None,
                    help='The directory to clean up. By default it will mount on current directory')
parser.add_argument('--search', type=str, default=None,
                    help='The search term to clean up. By default it will be None')
args = parser.parse_args()

def process_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            # Perform an action on the file (e.g., print its name)
            file_extension = os.path.splitext(filepath)[1]
            if file_extension.lower() == '.pdf':
                #print("The file is a PDF.")
                # Get the creation time of the file
                #It represents the time of most recent content modification. It is expressed in seconds.
                creation_time = os.stat(filepath).st_mtime
                time_machine = args.days
                unix_tm = time_machine*24*60*60
                time_now = datetime.datetime.now().timetuple()
                time_now_unix = time.mktime(time_now)
                if creation_time < time_now_unix-unix_tm:
                    formatted_time = time.ctime(creation_time)
                    #if search term provided, then only look for search term files, else just remove based on time
                    if args.search:
                        search_term = re.search(args.search, filename) #use filename instead of filepath
                        if search_term:
                            print("-----------------------")
                            print(f"Outdated File: {filepath} creation time:", formatted_time)
                            #delete operation
                            os.remove(filepath)
                            print(f"Deleted File: {filepath}")
                            print("-----------------------")
                    else:    
                        print("-----------------------")
                        print(f"Outdated File: {filepath} creation time:", formatted_time)
                        #delete operation
                        os.remove(filepath)
                        print(f"Deleted File: {filepath}")
                        print("-----------------------")

        elif os.path.isdir(filepath):
            # Recursively process files in the subdirectory
            process_files(filepath)

# Provide the root directory to start the recursion
target = args.target
root = os.getcwd()
if target:
    root_directory = root+ f'/{target}/'
else:
    root_directory = root+ '/'

print(f"PDF files in path: {root_directory} older than {args.days} will be deleted")
prompt = input("This is a destructive action. Are you sure you want to proceed? Type yes/no to proceed: ")
if prompt.lower() == 'yes':
    process_files(root_directory)
else:
    print("Process Exited")