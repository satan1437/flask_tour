from flask import Flask, render_template, abort, url_for
import data

app = Flask(__name__)


@app.route('/')
def index():
	return render_template(
		'index.html',
		data=data.tours,
		nav=data.departure,
		title=data.title)


@app.route('/departures/<departure>')
def departures(departure):
	count = 0
	cost_min, cost_max = float('inf'), float('-inf')
	n_min, n_max = float('inf'), float('-inf')

	for i in data.tours:
		if data.tours[i]["departure"] == departure:
			count += 1
			if data.tours[i]["price"] > cost_max:
				cost_max = data.tours[i]["price"]
			if data.tours[i]["price"] < cost_min:
				cost_min = data.tours[i]["price"]
			if data.tours[i]["nights"] > n_max:
				n_max = data.tours[i]["nights"]
			if data.tours[i]["nights"] < n_min:
				n_min = data.tours[i]["nights"]

	temp = [count, cost_min, cost_max, n_min, n_max]
	return render_template(
		'departure.html',
		data=data.tours,
		rgn=departure,
		temp=temp,
		nav=data.departure,
		title=data.title)


@app.route('/tour/<int:id>')
def tours(id):
	try:
		hotel = data.tours[id]
	except KeyError:
		return abort(404)
	return render_template(
		'tour.html',
		data=hotel,
		nav=data.departure,
		title=data.title)


if __name__ == '__main__':
	app.run(debug=True)
