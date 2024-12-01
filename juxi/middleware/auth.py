

def login_required(get_response):

    def middleware(request):
        print(get_response.__name__, request.path)
        return get_response(request)

    return middleware
