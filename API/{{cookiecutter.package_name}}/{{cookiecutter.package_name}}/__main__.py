"""Main entry point for app"""
{% if cookiecutter.requires_database_support == 'no' -%}
import warnings

from flask import Flask, request, jsonify, Response
from flask_hmac import Hmac
from flask_hmac.exceptions import InvalidSignature, SecretKeyIsNotSet, UnknownKeyName

from {{cookiecutter.package_name}} import API_KEY_ID, API_KEY_SECRET
from {{cookiecutter.package_name}}.example_transformation import example_function
from {{cookiecutter.package_name}}.process_request import process_request_data


warnings.filterwarnings("ignore", message="Unverified HTTPS request")

application = Flask(__name__)
application.config["JSON_SORT_KEYS"] = False
application.config["HMAC_KEYS"] = {API_KEY_ID: API_KEY_SECRET}
hmac = Hmac(application)


@application.route("/process", methods=["POST", "OPTIONS"])
@hmac.auth()
def main_API():
    """
    Main service entrance. We only authenticate the POST request, so the hmac
    authentication does not apply to the OPTIONS.

    Args:
        None
    Returns:
        A returns tuple of a response message and an error code
    """

    try:

        if request.method == "OPTIONS":
            api_response = Response()

        else:

            hmac.validate_signature(request)

            # Do some basic math
            math_result = example_function(100)

            # Process the request
            result_dict = process_request_data(request)

            # JSONify the dictionary
            api_response = jsonify(result_dict)

        api_response.headers.add("Access-Control-Allow-Origin", "*")
        api_response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Signature"
        )
        api_response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")

        return api_response, 200


    except (SecretKeyIsNotSet, InvalidSignature, UnknownKeyName):
        error_message = "Unauthorized request"
        status_code = 403
        return error_message, status_code

    except:
        error_message = "Internal Server Error"
        status_code = 500
        return error_message, status_code
{%- endif %}
{% if cookiecutter.requires_database_support == 'yes' -%}
import warnings

from flask import Flask, request, jsonify, Response
from flask_hmac import Hmac
from flask_hmac.exceptions import InvalidSignature, SecretKeyIsNotSet, UnknownKeyName

from {{cookiecutter.package_name}} import API_KEY_ID, API_KEY_SECRET
from {{cookiecutter.package_name}}.example_transformation import example_function
from {{cookiecutter.package_name}}.example_query import query_module
from {{cookiecutter.package_name}}.process_request import process_request_data


warnings.filterwarnings("ignore", message="Unverified HTTPS request")

application = Flask(__name__)
application.config["JSON_SORT_KEYS"] = False
application.config["HMAC_KEYS"] = {API_KEY_ID: API_KEY_SECRET}
hmac = Hmac(application)


@application.route("/process", methods=["POST", "OPTIONS"])
@hmac.auth()
def main_API():
    """
    Main service entrance. We only authenticate the POST request, so the hmac
    authentication does not apply to the OPTIONS.

    Args:
        None
    Returns:
        A returns tuple of a response message and an error code
    """

    try:

        if request.method == "OPTIONS":
            api_response = Response()

        else:

            hmac.validate_signature(request)

            # Query
            query_result = query_module()

            # Do some basic math
            math_result = example_function(100)

            # Process the request
            result_dict = process_request_data(request)

            # JSONify the dictionary
            api_response = jsonify(result_dict)

        api_response.headers.add("Access-Control-Allow-Origin", "*")
        api_response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Signature"
        )
        api_response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")

        return api_response, 200


    except (SecretKeyIsNotSet, InvalidSignature, UnknownKeyName):
        error_message = "Unauthorized request"
        status_code = 403
        return error_message, status_code

    except:
        error_message = "Internal Server Error"
        status_code = 500
        return error_message, status_code
{%- endif %}


if __name__ == "__main__":
    application.run(debug=True)
