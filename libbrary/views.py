from django.http import HttpResponse

def home_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
            <h1>Добро пожаловать на главную страницу!</h1>
                <div><a href="/api/">API</a></div>
                <div><a href="/admin/">Админ-панель</a></div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)