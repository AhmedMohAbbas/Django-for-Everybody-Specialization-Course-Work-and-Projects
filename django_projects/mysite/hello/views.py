from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
# Create your views here.

class tryII(TemplateView):
    template_name= 'hello/mainpage.html' #Even if you don't use, it blowes up the code if it is not there

    def get(self, request):
        num_visits = request.session.get('visits', 0) + 1
        request.session['visits'] = num_visits
        if num_visits > 4 : del(request.session['visits'])
        ctx = {'num_visits': num_visits}
        t = loader.get_template(self.template_name)
        resp = HttpResponse(t.render(ctx, request))
        resp.set_cookie('dj4e_cookie', '5a38a1eb', max_age=1000)
        '''
        resp = HttpResponse('view count='+ str(num_visits))
        resp.set_cookie('dj4e_cookie', '5a38a1eb', max_age=1000)
        '''
        return resp


'''
def SesAsign(request):
    num_visits = request.session.get('visits', 0) + 1
    request.session['visits'] = num_visits
    if num_visits > 4 : del(request.session['visits'])
    resp = HttpResponse('view count='+ str(num_visits))
    resp.set_cookie('dj4e_cookie', '5a38a1eb', max_age=1000)
    return resp
''' # Both do the same work, one using the function approach and using the object approach