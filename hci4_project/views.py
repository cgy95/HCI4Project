from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import LinearAxis, Range1d
from bokeh.models import HoverTool, PanTool, WheelZoomTool
from registration.models import UserProfile
from django.contrib.auth.models import User

def index(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        #x= [1,2,3,4,5,6,7]
	x=["20-Oct-17", "27-Oct-17", "02-Nov-17", "09-Nov-17", "16-Nov-17", "23-Nov-17", "30-Nov-17"]
        y= [2500,2250,2300, 2150,2050,2100,2200]
        title = 'Weight and Calories over Time'
	extra_y = [85, 84, 82, 83, 83, 82, 85]

	
	hover = HoverTool(tooltips=[
	    ("calories", "@y kcal"),
            ("date", "@x")
	], names=["calories"])

	


        plot = figure(title= title ,
	    x_range = x, 
	    y_range = Range1d(2000, 2500),
            x_axis_label= 'Time', 
            y_axis_label= 'Calories', 
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
        plot.add_layout(LinearAxis(y_range_name="weight", axis_label="Weight"), 'right') 
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

        #Feed them to the Django template.
        return render(request, 'visualisation/index.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div} )
     
    else:
	return render(request, 'index.html')

