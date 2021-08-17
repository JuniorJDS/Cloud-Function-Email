def hello(request):
    ''' Cloud Function to Hello World...'''
    request_args = request.args
    request_json = request.get_json(silent=True)

    if request_args and 'name' in request_args:
        name = request_args['name']
    elif request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'Louco'
    return f'Hello, {name}'