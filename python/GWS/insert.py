# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:38:45 2017

@author: Mario
"""

import sshtunnel, mysql.connector

def insert_ok(x) -> None:
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
    
    _SQL = """insert into chido (Formatted_Addres, Status, Latitude, Longitude) values (%s, %s, %s, %s)"""
            
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
        
        for i in x:
            tmp= i.split('|')
            cursor.execute(_SQL, (tmp[0], tmp[1], tmp[2], tmp[3]))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    _SQL = "SELECT * FROM chido;"
    
    

def insert_fail(x) -> None:
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
    
    _SQL = """insert into nochido (Address, Status) values (%s, %s)"""
            
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
        
        for i in x:
            tmp= i.split('|')
            cursor.execute(_SQL, (tmp[0], tmp[1]))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    _SQL = "SELECT * FROM nochido;"
    
    with sshtunnel.SSHTunnelForwarder(
            (_host, _ssh_port),
            ssh_username=_username,
            ssh_password=_password,
            remote_bind_address=(_remote_bind_address, _remote_mysql_port),
            local_bind_address=(_local_bind_address, _local_mysql_port)) as tunnel:
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
    
    
    