status=418
match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")