from django.shortcuts import render,render_to_response
import random
import datetime
import time


# Create your views here.

def index(req):
	return render(req, 'demo/index.html')

def echart(req):
    return render(req, 'demo/echart/index.html')

def piechart(req):
	xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
	ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
	chartdata = {'x': xdata, 'y': ydata}
	charttype = "pieChart"
	chartcontainer = 'piechart_container'
	data = {
	    'charttype': charttype,
	    'chartdata': chartdata,
	    'chartcontainer': chartcontainer,
	    'extra': {
	        'x_is_date': False,
	        'x_axis_format': '',
	        'tag_script_js': True,
	        'jquery_on_ready': False,
	    }
	}
	return render_to_response('demo/piechart.html', data)


def multibarchart(request):
    """
    multibarchart page
    """
    nb_element = 10
    xdata = range(nb_element)
    ydata = [random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)
    ydata3 = map(lambda x: x * 3, ydata)
    ydata4 = map(lambda x: x * 4, ydata)

    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"}}

    chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
        'name3': 'series 3', 'y3': ydata3, 'extra3': extra_serie,
        'name4': 'series 4', 'y4': ydata4, 'extra4': extra_serie
    }

    nb_element = 100
    start_time = int(time.mktime(datetime.datetime(2012, 6, 1).timetuple()) * 1000)
    xdata = range(nb_element)
    xdata = map(lambda x: start_time + x * 1000000000, xdata)
    ydata = [i + random.randint(1, 10) for i in range(nb_element)]
    ydata2 = map(lambda x: x * 2, ydata)

    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "There are ", "y_end": " calls"},
                   "date_format": tooltip_date}

    date_chartdata = {
        'x': xdata,
        'name1': 'series 1', 'y1': ydata, 'extra1': extra_serie,
        'name2': 'series 2', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "multiBarChart"
    chartcontainer = 'multibarchart_container'  # container name
    chartcontainer_with_date = 'date_multibarchart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
        'chartdata_with_date': date_chartdata,
        'chartcontainer_with_date': chartcontainer_with_date,
        'extra_with_date': {
            'name': chartcontainer_with_date,
            'x_is_date': True,
            'x_axis_format': '%d %b %Y',
            'tag_script_js': True,
            'jquery_on_ready': True,
        },
    }
    return render_to_response('demo/multibar.html', data)


def test(req):
	return render(req, 'demo/dump.html')
