#!/usr/bin/env python3

from arguments import argument_parser
from epassword import Password

def main():
    """
    Entrypoint for the Epassword CLI.
    """
    args = argument_parser().parse_args()
    default_properties = ["a", "d", "p"]
    password_properties = []

    if args.ascii: password_properties.append("a") 
    if args.digits: password_properties.append("d") 
    if args.punctuations: password_properties.append("p") 
    if args.lowercase: password_properties.append("l") 
    if args.uppercase: password_properties.append("u") 

    if not (args.ascii or args.digits or args.punctuations):
        password_properties = list(set(password_properties + default_properties))
    
    password = Password(length=args.size, properties=password_properties) if args.size \
    else Password(properties=password_properties)

    print(password)
    if args.copy: print(password.copy())

    return 0

if __name__ == "__main__":
    main()
