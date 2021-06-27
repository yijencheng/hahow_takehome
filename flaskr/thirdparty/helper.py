def retry_if_resp_502(resp):
    return resp["status_code"] == 502
