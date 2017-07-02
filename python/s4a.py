# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:59:36 2017

@author: Mario
"""

from urllib.request import urlopen
from urllib.parse import quote
import json
#from insert import *


#a=quote('mario alberto briseño zamarripa')


def search4address(address):

    url='https://maps.googleapis.com/maps/api/geocode/json?address='
    add=url+quote(address)
    response=json.JSONDecoder().decode(urlopen(add).read().decode('utf-8'))
    
    if response['status'] == 'OK':
        form_add= response['results'][0]['formatted_address']+'|'+response['status']+'|'+str(response['results'][0]['geometry']['location']['lat'])+'|'+str(response['results'][0]['geometry']['location']['lng'])
    else:
        form_add= address + '|' + response['status']
        
    return form_add.split('|')