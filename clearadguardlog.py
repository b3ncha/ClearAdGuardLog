"""
App Name: Clear Adguard Log
Project Folder: https://github.com/b3ncha/ClearAdGuardLog
Version: 1.0.0 BETA
"""
import os
import re
import argparse


def exist_input_file(inputfile = "", current_path = ""):
    """
    Checks if the input file exists and if so, the function
    returns the path with the file name. If not, an empty string is returned.
    1st check: Was a complete path with filename passed?
    2nd check: Only if first check fails. File is searched in the current directory.
    """

    file_exists = os.path.exists(inputfile)
    if file_exists is True:
        return inputfile

    inputfile = current_path + inputfile
    file_exists = os.path.exists(inputfile)
    if file_exists is True:
        return inputfile

    # Input file not exist
    return ""

def rm_double_entries(liste):
    """
    Remove Duplicate domain entries and return a new list
    """
    result_list = []

    for element in liste:
        if element not in result_list:
            result_list.append(element)

    return result_list

def clear_log(inputfile, domain_pattern):
    """
    clear_log
    searches the AdGuard tunnel log file for domains and stores them
    in a list that is returned to the calling function.
    inputfile: complete verified filename with path
    domain_pattern: re pattern for urls, is used to copy the respective
                    domain and transfer it to the new list.
    """
    new_domain_list = []

    with open(inputfile, mode='r', encoding='utf-8') as file:

        for line in file:
            pattern_value = re.search(domain_pattern, str(line))

            if pattern_value:
                new_domain_list.append(pattern_value.group()[:-1])

    file.close()
    # Remove Duplicate domain entries
    new_domain_list = rm_double_entries(new_domain_list)

    return new_domain_list


def main():
    """ Managed the small Tool """
    current_path = os.path.dirname(os.path.realpath(__name__)) + "/"
    domain_pattern = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    new_domain_list = []

    # Generate CLI arguments/help
    parser = argparse.ArgumentParser(
        description="This program cleans up AdGuard's tunnel log file so\
          that you end up with a list of all domains that AdGuard has documented.",
        epilog="")

    parser.add_argument(
        '-i', '--input',\
        default="",\
        metavar='<input>',\
        help='AdGuard Tunnel Log File')

    parser.add_argument(
        '-o', '--output',\
        default="",\
        metavar='<output>',\
        help='The path and the name for the cleared Log File.\
          Default: Current folder/clearAdGuardLog.txt')

    # Read the Arguments from Input
    args = parser.parse_args()

    args.input = exist_input_file(args.input, current_path)
    if args.input == "":
        print("I have not found an AdGuard Tunnel Log file, use the input argument to select one.")

    if args.output == "":
        args.output = current_path + "clearAdGuardLog.txt"

    new_domain_list = clear_log(args.input, domain_pattern)

    try:
        with open(args.output, mode='w+', encoding='utf-8') as file:
            file.write("\n".join(new_domain_list))
            print("The cleared Log File (clearAdGuardLog.txt) was writen.")
    except AssertionError as error:
        print("The cleared Log File cound not be write. Error: " + error)
    finally:
        file.close()

if __name__ == "__main__":
    main()
