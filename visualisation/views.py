from django.shortcuts import render
from registration.models import UserProfile
from django.contrib.auth.models import User
from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

# Create your views here.
def index(request):
    return render(request, 'visualisation/index.html', context_dict)

def client1(request):

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
        return render(request, 'visualisation/client3.html', {'username': str(username), 'is_supervisor': is_supervisor, 'script' : script , 'div' : div} )
