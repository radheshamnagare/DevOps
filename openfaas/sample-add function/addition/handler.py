def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    l = list(req.split(","))
    res = 0
    for no in l:
        res += int(no)

    return res

