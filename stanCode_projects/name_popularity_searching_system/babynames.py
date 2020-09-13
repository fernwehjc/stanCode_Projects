"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

File: babynames.py
Name: Jade Yeh
1. This file extracts data from txt files(by year) which contains year, rank, and baby name.
2. This file creates a nested data structure as name_data
        and organizes all the data into a dictionary in a form of {name: {year: rank}}.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    # 1. Name doesn't exist in name_data -> Add associated year & rank in a form of dictionary
    if name not in name_data:
        name_data[name] = {year: rank}
    # 2. Name exists but has different rank in a certain year -> Keep the lower rank
    elif name in name_data and year in name_data[name] and int(rank) > int(name_data[name][year]):
        name_data[name][year] = name_data[name][year]
    else:
        name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    year = ''
    line_num = 0
    with open(filename, 'r') as f:
        for line in f:
            # Get the year at first line in the open file.
            if line_num == 0:
                year = line.strip()
                line_num += 1
            # Separate each line into 3 independent data(rank, boy name, and girl name) and add data into name_data.
            else:
                rank_lst = line.split(',')
                # Use strip() to remove spaces in each data.
                rank = rank_lst[0].strip()
                name_1 = rank_lst[1].strip()
                name_2 = rank_lst[2].strip()
                # This function helps add year, rank, and the associated name into name_data.
                add_data_for_name(name_data, year, rank, name_1)
                add_data_for_name(name_data, year, rank, name_2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    # Add all available files into name_data by using add_file function.
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    # Lowercase the target string and the names contained within name_data for a comprehensive matching.
    target = target.lower()
    names = []
    for key in name_data:
        key = key.lower()
        # Capitalize the first letter of the name if the name contains the target string that the user searches for.
        if target in key:
            name = ''
            for i in range(len(key)):
                if i == 0:
                    name += key[i].upper()
                else:
                    name += key[i]
            # Add the founded name into names(list).
            names.append(name)
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
