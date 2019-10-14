from django.http import JsonResponse


def response(status=None, message=None, data=[]):
    """
    实现Api的固定格式的返回
    :param status:
    :param message:
    :param data:
    :return:
    """
    if status is None:
        status = 10200
    if message is None:
        message = "success"

    response_dict = {
        "status": status,
        "message": message,
        "data": data
    }
    return JsonResponse(response_dict)
