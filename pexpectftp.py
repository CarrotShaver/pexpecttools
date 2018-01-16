# Author: Ross Moriwaki
# Version: 1.0 1/13/2018
# Program: pexpectftp.py
# This program will automatically log in to an ftp server and open a terminal to be used

#testing args: -d speedtest.tele2.net -u anonymous -v

import argparse
import pexpect

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", help="The domain of the host you want to ftp to.")
    parser.add_argument("-u", "--username", help="Set username for logging  in to ftp")
    parser.add_argument("-p", "--password", help="Set password for logging in to ftp")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity.", action="store_true")

    args = parser.parse_args()

    if args.verbose:
        print("Starting pexpectftp in verbose mode.")
        if args.username == None:
            print("No username detected, defaulting to \"anonymous\".")
            print("Attempting to ftp to " + str(args.domain) + " as anonymous.")

        else:
            print("Attempting to ftp to " + str(args.domain) + " as " + str(args.username))
            if args.password == None:
                print("No password detected, defaulting to empty string.")

        print("Use [esc] to exit interaction.")
        print("\n")

    if args.username == None:
        args.username = "anonymous"
    if args.password == None:
        args.password = " "

    if args.verbose:
        print("Spawning ftp connection...")
    child = pexpect.spawn("ftp " + (str(args.domain)))
    if args.verbose:
        print("Successfully spawned ftp child.")
    child.delaybeforesend = .5

    if args.verbose:
        print("Expecting Name prompt....")
    child.expect("[Nn]ame .*: ")
    if args.verbose:
        print("Received name prompt: inputting username...")
    child.sendline(str(args.username))
    if args.verbose:
        print("Expecting Password prompt...")
    child.expect("[Pp]assword")
    if args.verbose:
        print("Received password prompt: inputting password...")
    child.sendline(str(args.password))
    child.expect("ftp")
    if args.verbose:
        print("Opening interact mode...")
    child.interact()

    if args.verbose:
        print("Left interact mode.")


if __name__=='__main__':
    Main()
