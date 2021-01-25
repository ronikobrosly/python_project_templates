"""
Methods to process data received by the API
"""


def process_request_data(request):
    """
    Takes JSON data received in POST request and does very simple
    transformation to it. This is just for demostration purposes.

    Args:
        None
    Returns:
        A dictionary with fields to return to user
    """

    request_json = request.get_json()
    answer = str(len(request_json.keys()))
    output_json = {"answer": answer}

    return output_json
