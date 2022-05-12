#!/usr/bin/python3

import sys
import os


def complete_ip(ip):
    ip_elems = ip.split('.')
    ip_elems_len = len(ip_elems)
    if ip_elems_len == 1:
        ip = '192.168.214.{}'.format(ip_elems[0])
    elif ip_elems_len == 2:
        ip = '192.168.{}.{}'.format(ip_elems[0], ip_elems[1])
    elif ip_elems_len == 3:
        ip = '192.{}.{}.{}'.format(ip_elems[0], ip_elems[1], ip_elems[2])
    elif ip_elems_len == 4:
        ip = '.'.join(ip_elems)
    else:
        raise
    return ip


def do_ssh_helper(ip, username):
    command = ['ssh']

    # username
    command.append('-l {}'.format(username))

    # ip
    command.append(complete_ip(ip))

    command_string = ' '.join(command)
    print(command_string)
    os.system(command_string)


if __name__ == '__main__':
    # ssh_helper.py ip username
    if len(sys.argv) == 2:
        ip = sys.argv[1]
        username = 'root'
    elif len(sys.argv) == 3:
        ip = sys.argv[1]
        username = sys.argv[2]
    else:
        exit(1)

    do_ssh_helper(ip, username)
