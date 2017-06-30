# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:19:44 2017

@author: Mario
"""

import sshtunnel
import mysql.connector
_host = 'irock.enroute.xyz'
_ssh_port = 22
_username = 'mbriseno'
_password = 'm4r10Br1s3n0!'
_remote_bind_address = 'localhost'
_local_mysql_port = 9990
_local_bind_address = '127.0.0.1'
_remote_mysql_port = 3306
_db_user = 'mbriseno'
_db_password = 'm4r10Br1s3n0!'
_db_name = 'Mario'

#_SQL = "SELECT * FROM log;"

_SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
        
with sshtunnel.SSHTunnelForwarder(
        (_host, _ssh_port),
        ssh_username=_username,
        ssh_password=_password,
        remote_bind_address=(_remote_bind_address, _remote_mysql_port),
        local_bind_address=(_local_bind_address, _local_mysql_port)
) as tunnel:
    conn = mysql.connector.connect(
        user=_db_user,
        password=_db_password,
        host=_local_bind_address,
        database=_db_name,
        port=_local_mysql_port)
    
    cursor = conn.cursor()
    cursor.execute(_SQL,('hithch_hiker','xyz','127.0.0.1','Safari','set()'))
    conn.commit()
    cursor.close()
    conn.close()

        
_SQL = "SELECT * FROM log;"


with sshtunnel.SSHTunnelForwarder(
        (_host, _ssh_port),
        ssh_username=_username,
        ssh_password=_password,
        remote_bind_address=(_remote_bind_address, _remote_mysql_port),
        local_bind_address=(_local_bind_address, _local_mysql_port)
) as tunnel:
    conn = mysql.connector.connect(
        user=_db_user,
        password=_db_password,
        host=_local_bind_address,
        database=_db_name,
        port=_local_mysql_port)
    cursor = conn.cursor()
    cursor.execute(_SQL)
    res = cursor.fetchall()
    for row in res:
        print(row)