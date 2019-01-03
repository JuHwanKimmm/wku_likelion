from django.shortcuts import render
from world.models import World

# Create your views here.


# GET Hello
def world(request):

 # ORM
    # SQL문을 소스코드로 치는거
    # select * from hello_hello
    post = World.objects.all()
    print(post)

    context = {
        'post': post
    }
    return render(request, "world/index.html", context=context)
