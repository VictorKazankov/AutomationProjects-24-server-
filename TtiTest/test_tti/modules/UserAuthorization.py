# -*- coding: utf-8 -*-

import requests

from config import URL_GIS_MT_AUTH

session = requests.Session()

class UserAuthorization():

    def __init__(self):
        pass

    def session_authorization(self):
        data_auth = {"p_cpwd":"NTQxNkQ3Q0Q2RUYxOTVBMEY3NjIyQTlDNTZCNTVFODQ=",
                     "p_nssid":29510699994,
                     "p_clogin":"lena"}
        auth = session.post(URL_GIS_MT_AUTH,
                            data=data_auth)
        if auth.status_code is 200:
            print ("Session created and authorization")
        else:
            print("Session no authorization")
        pass

    def close_session(self):
        session.close()
