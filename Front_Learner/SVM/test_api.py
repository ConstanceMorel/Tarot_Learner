#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Test API """

from json import loads
# Related third party imports
from requests import Session
from requests.exceptions import ConnectionError
URL = 'http://localhost:12345'
SESSION = Session()

def get_path(path):
    """ GET path """
    print path
    try:
        loads(SESSION.get(path).text)
    except ConnectionError, log:
        return log
    except ValueError, log:
        return log
    return 'OK'

def post_path(path, payload=None):
    """ POST path """
    print path
    try:
        loads(SESSION.post(path, data=payload).text)
    except ConnectionError, log:
        return log
    except ValueError, log:
        return log
    return 'OK'

if __name__ == '__main__':
    print get_path(URL + '/hand/0')


    print get_path(URL + '/newparty/status')

    print get_path(URL + '/newparty/available_seats')

    print get_path(URL + '/newparty')

    print post_path(URL + '/newparty/available_seats/0')


    print get_path(URL + '/table/1/0')

    print post_path(URL + '/table/0/2/10')

    print get_path(URL + '/table/trick')

    print get_path(URL + '/table')
