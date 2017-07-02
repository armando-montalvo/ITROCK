# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:41:45 2017

@author: Mario
"""

from flask import Flask, render_template, request, escape
from s4a import search4address
from insert_webapp import *

app= Flask(__name__)

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',the_title="Let's validate some data")


@app.route('/search4',methods=['POST'])
def do_search() -> str:
    adrs = request.form['address']
    rs,rss= search4address(adrs)
    title= 'here are your results:'
    
    temps=open('temp.txt','a')
    print(rs,file=temps)
    temps.close()
    
    if rss[1] == 'OK':
        insert_ok(rss)
    else:
        insert_fail(rss)
    
    f=open('ok_results.txt','a')
    f2=open('zero_results.txt','a')
    if rss[1] == 'OK':
        print(rs,file=f)
    else:
        print(rs,file=f2)
    f.close()
    f2.close()
    return render_template('results.html',
                           the_address=adrs,
                           the_status= rss[1],
                           the_title= title,
                           the_results=' '.join(rss)
                           )


@app.route('/table')
def view_the_log() ->str:
    """Read the file in the browser"""
    contents = []
    sts=[]
    with open('temp.txt','r') as t:
        for i in t:
            sts.append(i)
                
    if sts[-1].split('|')[1] == 'OK':
        with open('ok_results.txt', 'r') as log:
            for line in log:
                contents.append([])
                for item in line.split('|'):
                        contents[-1].append(escape(item))
        titles = ('Formatted Address', 'Status', 'Latitude', 'Longitude')
        
        rt=render_template('ok.html',
                               the_title='View address info',
                               the_head=titles,
                               the_data=contents,)
    else:
        with open('zero_results.txt', 'r') as log:
            for line in log:
                contents.append([])
                for item in line.split('|'):
                    contents[-1].append(escape(item))
        titles = ('Address', 'Status')
        
        rt=render_template('zero_results.html',
                               the_title='View address info',
                               the_head=titles,
                               the_data=contents,)
    return rt
        
    
app.run()
 