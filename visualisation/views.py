from django.shortcuts import render
from registration.models import UserProfile
from django.contrib.auth.models import User
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components
from bokeh.models import LinearAxis, Range1d
from bokeh.models import HoverTool

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
	extra_y = [85, 84, 82, 83, 83, 82, 85]

	
	hover = HoverTool(tooltips=[
	    ("index", "$index"),
	    ("(x,y)", "($x, $y)"),
	    ("calories", "@y"),
	], names=["calories"])

	hoverweight = HoverTool(tooltips=[
	    ("index", "$index"),
	    ("(x,y)", "($x, $y)"),
	    ("weight", "@extra_y"),
	], names=["weight"])


        plot = figure(title= title ,
	    x_range = x, 
	    y_range = Range1d(2000, 2500),
            x_axis_label= 'Time', 
            y_axis_label= 'Calories', 
            plot_width =600,
            plot_height =400,
	    tools=[hover]

	    )

        plot.line(x, y, legend= 'calories over time', line_width = 2, name="calories")
	plot.extra_y_ranges['weight'] = Range1d(70, 90)

	
	#plot.multi_line([x, y], [x, extra_y], color=["firebrick", "navy"], line_width=4)
        plot.add_layout(LinearAxis(y_range_name="weight", axis_label="Weight"), 'right') 
	plot.line(x, extra_y, legend= 'weight over time', line_width = 2, y_range_name="weight", name="weight", color="firebrick")

        #Store components 
        script, div = components(plot)

        #Feed them to the Django template.
        return render(request, 'visualisation/client1.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div} )

def client2(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        x= [1,3,5,7,9,11,13]
        y= [1,2,3,4,5,6,7]
        title = 'y = f(x)'

        plot = figure(title= title , 
            x_axis_label= 'X-Axis', 
            y_axis_label= 'Y-Axis', 
            plot_width =400,
            plot_height =400)

        plot.line(x, y, legend= 'f(x)', line_width = 2)
        #Store components 
        script, div = components(plot)

        #Feed them to the Django template.
        return render(request, 'visualisation/client2.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div} )

def client3(request):

    if request.user.is_authenticated():
        username = request.user.get_username()
        if request.method == 'GET' and request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            is_supervisor = user_profile.supervisor
        x= [10,3,5,7,9,11,13]
        y= [1,2,3,4,5,6,70]
        title = 'y = f(x)'

        plot = figure(title= title , 
            x_axis_label= 'X-Axis', 
            y_axis_label= 'Y-Axis', 
            plot_width =400,
            plot_height =400)

        plot.line(x, y, legend= 'f(x)', line_width = 2)
        #Store components 
        script, div = components(plot)

        #Feed them to the Django template.
        return render(request, 'visualisation/client3.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div} )
