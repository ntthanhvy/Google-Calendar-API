#!/usr/bin/env python3
import check_api
import sys
import argparse
import request as req



def get_argument():
    parser = argparse.ArgumentParser(description='Enter API and Method')
    parser.add_argument('api', help='Name of the resource api', default='calendarList')
    parser.add_argument('-method', default='get', help='Identifi the method in api')
    args = parser.parse_args()
    return args


# ---------the main run function----------------
def main():
    arg = get_argument()
    print(arg)
    check_api.get_api(arg.api, arg.method)


if __name__ == '__main__':
    main()