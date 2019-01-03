from django.shortcuts import render
from hello.models import Hello
# Create your views here.


# GET Hello
def hello(request):

    # ORM
    # SQL문을 소스코드로 치는거
    # select * from hello_hello
    post = Hello.objects.all()
    print(post)

    context = {
        'post': post
    }
    return render(request, "hello/index.html", context=context)
