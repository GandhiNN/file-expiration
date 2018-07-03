#!/usr/local/bin/python3
#
# A simple housekeeping tool
# author = __gandhi__
# ngakan.gandhi@packet-systems.com

import json
import subprocess
import sys
import getopt

# Load expire configuration file
def load_config(config_file):

    with open(config_file) as confile:
        return json.load(confile)

# Get config params
def get_expire_params(config_list):

    path = []
    retention_hour = []
    for config in config_list:
        path.append(config['path'])
        retention_hour.append(config['retention_hour'])

    return path, retention_hour

# Delete function
def deletion(path, retention_hour):

    if len(path) == len(retention_hour):
        retention_minute = [(int(i) * 60) for i in retention_hour]
        count = 0
        while (count < len(path)):
            print("Deleting files older than %s inside directory '%s'..." % ((retention_hour[count]) + "h" , path[count]))
            del_command = ["find '%s' -mmin '%s' -type f -print -delete" % (path[count], "+" + str(retention_minute[count]))]
            subprocess.call(del_command, shell=True)
            count += 1
    else:
        print("Please check your expiration configuration file")

# Main function
def main(argv):

    config_file = ''
    path = []
    retention_hour = []
    try:
        opts, args = getopt.getopt(argv, "hc:", ["config="])
    except getopt.GetoptError:
        print("expire.py -c <path_to_expiration_config_file>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("expire.py -c <path_to_expiration_config_file>")
            sys.exit()
        elif opt in ("-c", "--config"):
            config_file = arg

    configs = load_config(config_file)
    path, retention_hour = get_expire_params(configs)
    deletion(path, retention_hour)

if __name__ == "__main__":
    main(sys.argv[1:])
