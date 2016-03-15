from flask import Flask, render_template
import util

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', \
    						currently_reading=util.get_books('currently-reading'), \
    						read=util.get_books('read'))

if __name__ == '__main__':
	app.run(debug=True)
