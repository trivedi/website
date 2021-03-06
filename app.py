from flask import Flask, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', quote=util.get_quote(), \
    						currently_reading=util.get_books('currently-reading'), \
    						read=util.get_books('read'))

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/teaching')
def teaching():
	return render_template('teaching.html')


if __name__ == '__main__':
	app.run(debug=True)
