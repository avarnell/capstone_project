from flask import Flask, request, render_template
import pandas as pd
import cPickle as pickle
import random
import numpy as np

app = Flask(__name__)

def getBooks(userId):
	books = []
	formattedBooks = formatBooks(books)
	return formattedBooks

def formatBooks(books):
	return []




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/userId', methods=['GET', 'POST'])
def userId():
	userId = request.form.get('userId')
	print '{}'.format(userId)

	if userId is None:
		return  render_template('userId.html')
	else:
		# booklist = getBooks(userId)

		booklist =['test', 'test2']

		return render_template('bookList.html', booklist=booklist)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)
