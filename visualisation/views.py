from django.shortcuts import render
from registration.models import UserProfile
from django.contrib.auth.models import User
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import CustomJS, LinearAxis, Range1d, Legend, LegendItem, ColumnDataSource, DataRange1d, Plot, LinearAxis, Grid, HoverTool, PanTool, WheelZoomTool 
import pandas as pd
from numpy import pi
from bokeh.models.glyphs import HBar
from bokeh.core.properties import value
from bokeh.io import show, output_file
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select


# Create your views here.
def index(request):
    return render(request, 'visualisation/index.html', context_dict)

def client1(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        #x= [1,2,3,4,5,6,7]
	x=["20-Oct-17", "27-Oct-17", "02-Nov-17", "09-Nov-17", "16-Nov-17", "23-Nov-17", "30-Nov-17"]
        y= [2500,2250,2300, 2150,2050,2100,2200]
        title = 'Weight and Calories over Time'
	extra_y = [85, 83, 80, 78, 77, 76, 75]

	
	hover = HoverTool(tooltips=[
	    ("calories", "@y kcal"),
            ("date", "@x")
	], names=["calories"])

	


        plot = figure(title= title ,
	    x_range = x, 
	    y_range = Range1d(2000, 2500),
            x_axis_label= 'Time (Weekly)', 
            y_axis_label= 'Daily Average Calores (kcal)', 
            plot_width =600,
            plot_height =400,
	    tools=[hover]

	    )

        plot.line(x, y, legend= 'Calories Over Time', line_width = 2, name="calories")
	plot.circle(x, y, fill_color="blue", size=8, legend= 'Calories Over Time')
	plot.extra_y_ranges['weight'] = Range1d(70, 90)

	hoverweight = HoverTool(tooltips=[
	    ("weight", "@y kg"),
            ("date", "@x")
	], names=["weight"])
	
	#plot.multi_line([x, y], [x, extra_y], color=["firebrick", "navy"], line_width=4)
        plot.add_layout(LinearAxis(y_range_name="weight", axis_label="Weight (kg)"), 'right') 
        source = ColumnDataSource(data=dict(x=x, y=extra_y))
        plot.circle('x', 'y', source=source, fill_color="firebrick", line_color="firebrick", size=8, y_range_name="weight", name="weight", legend="Weight Over Time")
	plot.line(x, extra_y, legend= 'Weight Over Time', line_width = 2, y_range_name="weight", name="weight", color="firebrick")
        
	zoom = WheelZoomTool()
	plot.add_tools(hoverweight, PanTool(), zoom)

	plot.legend.location = "bottom_left"
	plot.legend.click_policy="hide"
	plot.toolbar.active_scroll = zoom
        
        plot.toolbar.logo = None
	plot.toolbar_location = None

        #Store components 
        script, div = components(plot)

	#The code which changes kilos to pounds. This needs to be integrated using ajax I think.
        callback = CustomJS(args=dict(source=source), code="""
	    var data = source.data;
	    var f = cb_obj.value
	    y = data['y']
            if (f === "Kilos") {
		    for (i = 0; i < y.length; i++) {
	 	         y[i] = y[i] / 2.2
		    }
            }
            if (f === "Pounds") {
		    for (i = 0; i < y.length; i++) {
	 	         y[i] = y[i] * 2.2
		    }
            }
            source.change.emit();
	""")

        s = Select(title = 'Units', value="Kilos", options=['Kilos','Pounds'])
        s.js_on_change('value', callback)
        select_script,select_div = components(s)
	#pie chart#

	# a color for each pie piece
	colors = ["red", "blue"]

	p = figure(x_range=(-1,1), y_range=(-1,1), plot_width =200,
            plot_height =200, tools=[])

	p.wedge(x=0, y=0, radius=1, start_angle=0, end_angle=0.12, color="red", legend="weight loss", name="change" )
	p.wedge(x=0, y=0, radius=1, start_angle=0.12, end_angle=0, color="blue", legend="current weight", name="current" )

	hoverchange = HoverTool(tooltips=[
	    ("Total Weight Loss", "10kg (12%)"),
	], names=["change"])

	hovercurrent = HoverTool(tooltips=[
	    ("Current Weight", "75kg (88%)"),
	], names=["current"])

	p.add_tools(hoverchange, hovercurrent, PanTool(), zoom)

	# display/save everythin  

	script1, div1 = components(p)
	
        #Feed them to the Django template.
        return render(request, 'visualisation/client1.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div, 'script1' : script1 , 'div1' : div1, 'select_script': select_script, 'select_div': select_div} )

def client2(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        #x= [1,2,3,4,5,6,7]
	x=["20-Oct-17", "27-Oct-17", "02-Nov-17", "09-Nov-17", "16-Nov-17", "23-Nov-17", "30-Nov-17"]
        y= [1850,1900,2000, 2200,2150,2250,2400]
        title = 'Weight and Calories over Time'
	extra_y = [65, 66, 68, 69, 70, 69, 70]

	
	hover = HoverTool(tooltips=[
	    ("calories", "@y kcal"),
            ("date", "@x")
	], names=["calories"])

	


        plot = figure(title= title ,
	    x_range = x, 
	    y_range = Range1d(1800, 2500),
            x_axis_label= 'Time (Weekly)', 
            y_axis_label= 'Daily Average Calories (kcal)', 
            plot_width =600,
            plot_height =400,
	    tools=[hover]

	    )

        plot.line(x, y, legend= 'Calories Over Time', line_width = 2, name="calories")
	plot.circle(x, y, fill_color="blue", size=8, legend= 'Calories Over Time')
	plot.extra_y_ranges['weight'] = Range1d(60, 75)

	hoverweight = HoverTool(tooltips=[
	    ("weight", "@y kg"),
            ("date", "@x")
	], names=["weight"])
	
	#plot.multi_line([x, y], [x, extra_y], color=["firebrick", "navy"], line_width=4)
        plot.add_layout(LinearAxis(y_range_name="weight", axis_label="Weight (kg)"), 'right') 
        plot.circle(x, extra_y, fill_color="firebrick", line_color="firebrick", size=8, y_range_name="weight", name="weight", legend="Weight Over Time")
	plot.line(x, extra_y, legend= 'Weight Over Time', line_width = 2, y_range_name="weight", name="weight", color="firebrick")
        
	zoom = WheelZoomTool()
	plot.add_tools(hoverweight, PanTool(), zoom)

	plot.legend.location = "bottom_left"
	plot.legend.click_policy="hide"
	plot.toolbar.active_scroll = zoom
        
        plot.toolbar.logo = None
	plot.toolbar_location = None

        #Store components 
        script, div = components(plot)

	#pie chart#

		# a color for each pie piece
	colors = ["red", "blue"]

	# NOTE: this is the changed line
	p = figure(x_range=(-1,1), y_range=(-1,1), plot_width =200,
            plot_height =200, tools=[])

	p.wedge(x=0, y=0, radius=1, start_angle=0, end_angle=0.08, color="red", legend="weight gain", name="change" )
	p.wedge(x=0, y=0, radius=1, start_angle=0.08, end_angle=0, color="blue", legend="current weight", name="current" )

	hoverchange = HoverTool(tooltips=[
	    ("Total Weight Gain", "5kg (7%)"),
	], names=["change"])

	hovercurrent = HoverTool(tooltips=[
	    ("Start Weight", "65kg (93%)"),
	], names=["current"])

	p.add_tools(hoverchange, hovercurrent, PanTool(), zoom)

	# display/save everythin  

	script1, div1 = components(p)

        #Feed them to the Django template.
        return render(request, 'visualisation/client2.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div, 'script1' : script1 , 'div1' : div1} )

def client3(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        #x= [1,2,3,4,5,6,7]
	x=["20-Oct-17", "27-Oct-17", "02-Nov-17", "09-Nov-17", "16-Nov-17", "23-Nov-17", "30-Nov-17"]
        y= [3100,2900,2800, 2900,2600,2500,2200]
        title = 'Weight and Calories over Time'
	extra_y = [98, 95, 92, 90, 88, 85, 81]

	
	hover = HoverTool(tooltips=[
	    ("calories", "@y kcal"),
            ("date", "@x")
	], names=["calories"])

	


        plot = figure(title= title ,
	    x_range = x, 
	    y_range = Range1d(2100, 3200),
            x_axis_label= 'Time (Weekly)', 
            y_axis_label= 'Daily Average Calories (kcal)', 
            plot_width =600,
            plot_height =400,
	    tools=[hover]

	    )

        plot.line(x, y, legend= 'Calories Over Time', line_width = 2, name="calories")
	plot.circle(x, y, fill_color="blue", size=8, legend= 'Calories Over Time')
	plot.extra_y_ranges['weight'] = Range1d(80, 100)

	hoverweight = HoverTool(tooltips=[
	    ("weight", "@y kg"),
            ("date", "@x")
	], names=["weight"])
	
	#plot.multi_line([x, y], [x, extra_y], color=["firebrick", "navy"], line_width=4)
        plot.add_layout(LinearAxis(y_range_name="weight", axis_label="Weight (kg)"), 'right') 
        plot.circle(x, extra_y, fill_color="firebrick", line_color="firebrick", size=8, y_range_name="weight", name="weight", legend="Weight Over Time")
	plot.line(x, extra_y, legend= 'Weight Over Time', line_width = 2, y_range_name="weight", name="weight", color="firebrick")
        
	zoom = WheelZoomTool()
	plot.add_tools(hoverweight, PanTool(), zoom)

	plot.legend.location = "bottom_left"
	plot.legend.click_policy="hide"
	plot.toolbar.active_scroll = zoom
        
        plot.toolbar.logo = None
	plot.toolbar_location = None

        #Store components 
        script, div = components(plot)

	# bar chart #

	weight = ["Weight"]
	changes = ["current", "change"]
	colors = ["red", "blue"]

	data = {'weight' : weight,
		'current' : [98],
		'change' : [17],
		}

	source = ColumnDataSource(data=data)

	p = figure(x_range=weight, plot_height=150, plot_width=240, title="Weight Change since 20-Oct-17",
		   toolbar_location=None, tools="")

	p.vbar_stack(changes, x='weight', width=0.2, color=colors, source=source, name=changes, legend=[value(x) for x in changes])

	hover = HoverTool(tooltips=[
	    ("Total Weight Loss", "17kg (17.3%)")], names=['change'])

	hovercurrent = HoverTool(tooltips=[
	    ("Current Weight", "81kg (82.7%)")], names=['current'])

	p.y_range.start = 0
	p.x_range.range_padding = 0.1
	p.xgrid.grid_line_color = None
	p.axis.minor_tick_line_color = None
	p.outline_line_color = None
	p.legend.orientation = "horizontal"
	p.legend.location = "bottom_left"
	p.add_tools(hover, hovercurrent)

	script1, div1 = components(p)

        #Feed them to the Django template.
        return render(request, 'visualisation/client3.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div, 'script1' : script1 , 'div1' : div1} )
