def prepare_success_response(message):
    """ prepare success response for all serializer """
    response = {
        'status': True,
        'message': message
    }
    return response


def prepare_error_response(serializer_error):
    """ prepare error response for all serializer """
    response = {
        'status': False,
        'message': serializer_error,
    }
    return response
