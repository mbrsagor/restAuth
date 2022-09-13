def success_response(message):
    response = {
        'status': True,
        'message': message,
    }
    return response


def failed_response(message):
    response = {
        'status': False,
        'message': message,
    }
    return response
