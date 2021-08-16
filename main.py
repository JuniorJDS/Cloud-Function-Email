def hello(request):
    request_args = request.args
    if request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'Louco'
    return f'Hello, {name}'