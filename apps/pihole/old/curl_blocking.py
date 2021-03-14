#! /usr/local/bin/python

import requests
import json

URL = "http://10.42.0.126/admin/api.php"
#
# Password-hash retrieved from /etc/pihole/setupVars.conf on the  pi.hole server
#
WEBPASSWORD = "998ed4d621742d0c2d85ed84173db569afa194d4597686cae947324aa58ab4bb"
AUTH = "&auth=" + WEBPASSWORD

def get_pihole(url, query, auth=""):
    if auth == "":
        phpData = requests.get(url + query)
    else:
        phpData = requests.get(url + query + auth)

    jsonData = phpData.json()
    print (query + '=')
    print (str(jsonData) + '\n')
    return;

if __name__ == '__main__':
    #
    # No Authorisation required
    #
    get_pihole(URL, '?summary')

    #
    # Authorisation required
    #
    get_pihole(URL, '?topItems', AUTH )
    # get_pihole(URL, '?topClients', AUTH )
    # get_pihole(URL, '?getForwardDestinations', AUTH )
    # get_pihole(URL, '?getQueryTypes', AUTH )
    # get_pihole(URL, '?getAllQueries', AUTH )