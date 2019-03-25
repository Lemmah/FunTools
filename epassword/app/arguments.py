#!/usr/bin/env python3

from argparse import ArgumentParser

positional = []

optional_flags = [
    ["-a", "--ascii", "ascii letters explicitly"],
    ["-c", "--copy", "copy to cliboard"],
    ["-d", "--digits", "digits explicitly"],
    ["-p", "--punctuations", "punctuations explicitly"],
]

mutually_exclusive_flags = { 
    "group1": [
        ["-l", "--lowercase", "convert to lowercase"],
        ["-u", "--uppercase", "convert to uppercase"],
    ]
}

optional_ints = [
    ["-s", "--size", "length of the password"]
]

description = """
A CLI Utility to generate passwords on the fly!

By Default, it generates: a 16 character long password
-- using a combination of all characters.
"""

def argument_parser():
    """
    Function to parse the listed arguments.
    """
    parser = ArgumentParser(description=description)
    # optional flags
    for args_info in optional_flags:
        parser.add_argument(
            args_info[0], args_info[1], help=args_info[2],
            action="store_true")
    
    # optional ints
    for args_info in optional_ints:
        parser.add_argument(
            args_info[0], args_info[1], help=args_info[2],
            type=int)
    
    # mutually exclusive flags
    for group, me_arguments in mutually_exclusive_flags.items():
        me_group = parser.add_mutually_exclusive_group()
        for args_info in me_arguments:
            me_group.add_argument(
                args_info[0], args_info[1], help=args_info[2],
                action="store_true")

    return parser