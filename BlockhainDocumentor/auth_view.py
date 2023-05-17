from django.contrib.auth import authenticate, login
from django.http import HttpResponse
import uuid
from views import session_storage

def auth_view(request):
    username = request.POST["username"]  # допустим передали username и password
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        random_key = uuid.uuid4()
        session_storage.set(random_key, username)

        response = HttpResponse("{'status': 'ok'}")
        response.set_cookie("session_id", random_key)  # пусть ключем для куки будет session_id
        return response
    else:
        return HttpResponse("{'status': 'error', 'error': 'login failed'}")