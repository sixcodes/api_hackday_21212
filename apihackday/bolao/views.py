# Create your views here.
import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME, logout as auth_logout
from django.conf import settings
from django.contrib.auth import user_logged_in, BACKEND_SESSION_KEY, SESSION_KEY, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from apihackday.bolao.models import Bolao, Aposta


def home(r):
    return render_to_response('home.html', context_instance=RequestContext(r))

@login_required
def apostarBolao(r):
    if r.POST:
        id_bolao = r.POST.get('id', None)
        meu_bolao = Bolao.objects.get(id=id_bolao)
        valor_time_1 = r.POST.get('valor_time_1', None)
        valor_time_2 = r.POST.get('valor_time_2', None)
        Aposta.objects.create(bolao=meu_bolao, valor_time_1=valor_time_1, valor_time_2=valor_time_2, owner_id=r.POST['owner_id'])
        return render_to_response('form-apostar-bolao.html', context_instance=RequestContext(r))
    else:
        id_bolao = r.GET.get('id', None)
        meu_bolao = Bolao.objects.get(id=id_bolao)

        dict = {}
        dict['titulo'] = meu_bolao.titulo
        dict['time_1'] = meu_bolao.time_1
        dict['time_2'] = meu_bolao.time_2

        return render_to_response('form-apostar-bolao.html', dict, context_instance=RequestContext(r))



@login_required
def finalizarBolao(r):
    return render_to_response('form-resultado-bolao.html', context_instance=RequestContext(r))

@login_required
def convidarBolao(r):
    return render_to_response('convidar.html', context_instance=RequestContext(r))

@login_required
def listarBolao(r):
    return render_to_response('listar-bolao.html', context_instance=RequestContext(r))

@login_required
def criarBolao(r):
    print r.user
    return render_to_response('form-criar-bolao.html', context_instance=RequestContext(r))

@login_required
def exibirBolao(r):
    return render_to_response('exibir-bolao.html', context_instance=RequestContext(r))


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=request.POST)
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]

            # Use default setting if redirect_to is empty
            if not redirect_to:
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Heavier security check -- don't allow redirection to a different
            # host.
            elif netloc and netloc != request.get_host():
                redirect_to = settings.LOGIN_REDIRECT_URL

            # Okay, security checks complete. Log the user in.
            user = form.get_user()

            if user is None:
                user = request.user


            request.session[SESSION_KEY] = user.id
            request.session[BACKEND_SESSION_KEY] = user.backend
            if hasattr(request, 'user'):
                request.user = user
            user_logged_in.send(sender=user.__class__, request=request, user=user)

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return HttpResponseRedirect(redirect_to)
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        form = authentication_form(request)

    request.session.set_test_cookie()

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context, current_app=current_app)

def logout(request, next_page=None,
           template_name='registration/logged_out.html',
           redirect_field_name=REDIRECT_FIELD_NAME,
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)

    if redirect_field_name in request.REQUEST:
        next_page = request.REQUEST[redirect_field_name]
        # Security check -- don't allow redirection to a different host.
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path

    if next_page:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page)

    current_site = get_current_site(request)
    context = {
        'site': current_site,
        'site_name': current_site.name,
        'title': ('Logged out')
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
        current_app=current_app)


def logout_then_login(request, login_url=None, current_app=None, extra_context=None):
    """
    Logs out the user if he is logged in. Then redirects to the log-in page.
    """

    if not login_url:
        login_url = settings.LOGIN_URL
    return logout(request, login_url, current_app=current_app, extra_context=extra_context)
