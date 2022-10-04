from urllib import response


def status_middleware(get_response):
    print(f"Status: {True}")

    def get_message(request):
        print("Data successfully returned")
        res = get_response(request)
        print("Done!")
        return res

    return get_message
