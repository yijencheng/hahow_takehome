from flask import Response


def err_response(status_code: int) -> Response:
    if status_code == 404:
        return Response("Not found", status=404)
    else:
        return Response("Internal Server Error", status=500)
