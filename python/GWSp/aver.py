# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:47:29 2017

@author: Mario
"""

import sshtunnel
import mysql.connector        
from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app= Flask(__name__)

def log_request(req:'flask_request', res:str) -> None:
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
        cursor.execute(_SQL,(req.form['phrase'],
                             req.form['letters'],
                                     req.remote_addr,
                                     req.user_agent.browser,
                                     res,))
        conn.commit()
        cursor.close()
        conn.close()
    
            
    _SQL = "SELECT * FROM log;"
    
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
            
            

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web')


@app.route('/search4',methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters= request.form['letters']
    title= 'here are your results:'
    results= str(search4letters(phrase,letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title= title,
                           the_results= results,
                           )

@app.route('/viewlog')
def view_the_log() ->str:
    """Read the log in the browser."""
    contents = []
    with open('vsearch.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


app.run()