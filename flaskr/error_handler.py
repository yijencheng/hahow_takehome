from flask import Response


def err_response(status_code: int) -> Response:
    if status_code == 400:
        return Response("Bad Request", status=400)
    elif status_code == 401:
        return Response(
            "Unauthorized client. Please check your name and password.", status=401
        )
    elif status_code == 404:
        return Response("Not found", status=404)
    elif status_code == 502:
        return Response("Bad Gateway.Please retry later", status=502)
    elif status_code == 504:
        return Response("Gateway Timeout. Please retry later", status=504)
    else:
        return Response("Internal Server Error", status=500)
