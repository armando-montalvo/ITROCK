# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 10:41:45 2017

@author: Mario
"""

from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters


app= Flask(__name__)

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


#@app.route('/viewlog')
#def show_log() -> str:
#    with open('vsearch.log','r') as vsearch:
#        ls=vsearch.read()
#        print()
#    return ls


def log_request(req:'flask_request', res:str) -> None:
    with open ('vsearch.log','a') as log:
        print(req.form,file=log, end='|')
        print(req.remote_addr,file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log)


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


#def log_request(req: 'flask_request',res: str) -> None:
#    with open('vsearch.log','a') as log:
#        print(req,res,file=log)


#@app.route('/entry')
#def entry_page() -> 'html':
#    return render_template('entry.html' ,the_title='Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True)
