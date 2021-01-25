""" Tests the full pipeline of the app """

{% if cookiecutter.requires_database_support == 'no' -%}
import json
import hashlib

from flask_hmac import Hmac
import pytest

from {{cookiecutter.package_name}}.__main__ import application
from tests.conftest import main_API_inputs_and_outputs



# In this pytest decorator, you can run through a series of inputs and outputs
# for this particular test. List a bunch of test POSTs to the API here
# along with the expected output.
@pytest.mark.parametrize("test_input, expected", main_API_inputs_and_outputs())
def {{cookiecutter.package_name}}_good_result(test_input, expected, mocker):
    """Tests the API inputs and outputs. Using good inputs and expecting good outputs"""

    with application.test_client() as c:

        apikey = 'abc'
        apisecret = '123'

        hmac = Hmac()
        hmac.hmac_keys = {apikey: apisecret}
        body = json.dumps(test_input)
        body_hash = hmac.make_hmac_for(apikey, body)

        headers = {"Public-Key": apikey, "Signature": body_hash, "Content-Type": "application/json" }

        rv = c.post(
            'http://127.0.0.1:5000/process',
            json=test_input,
            headers=headers
        )
        observed_result = rv.get_json()

        assert observed_result == expected


def test_main_bad_secret_key(mocker):
    """Checks that using bad secret key with API returns 403."""

    with application.test_client() as c:

        apikey = 'abc'
        apisecret = 'bad_secret'

        hmac = Hmac()
        hmac.hmac_keys = {apikey: apisecret}
        body = json.dumps({'a': '1'})
        body_hash = hmac.make_hmac_for(apikey, body)

        headers = {"Public-Key": apikey, "Signature": body_hash, "Content-Type": "application/json" }

        rv = c.post(
            'http://127.0.0.1:5000/process',
            json={'a': '1'},
            headers=headers
        )

        rv == 403

{%- endif %}

{% if cookiecutter.requires_database_support == 'yes' -%}

import json
import hashlib

from flask_hmac import Hmac
import pytest

from {{cookiecutter.package_name}}.__main__ import application
from {{cookiecutter.package_name}} import example_query
from {{cookiecutter.package_name}}.__main__ import main_API
from tests.conftest import main_API_inputs_and_outputs


# In this pytest decorator, you can run through a series of inputs and outputs
# for this particular test. List a bunch of test POSTs to the API here
# along with the expected output.
@pytest.mark.parametrize("test_input, expected", main_API_inputs_and_outputs())
def {{cookiecutter.package_name}}_good_result(test_input, expected, cursor_fixture, mocker):
    """Tests the API inputs and outputs. Using good inputs and expecting good outputs"""

    with application.test_client() as c:

        example_query.CURSOR = cursor_fixture

        apikey = 'abc'
        apisecret = '123'

        hmac = Hmac()
        hmac.hmac_keys = {apikey: apisecret}
        body = json.dumps(test_input)
        body_hash = hmac.make_hmac_for(apikey, body)

        headers = {"Public-Key": apikey, "Signature": body_hash, "Content-Type": "application/json" }

        rv = c.post(
            'http://127.0.0.1:5000/process',
            json=test_input,
            headers=headers
        )
        observed_result = rv.get_json()

        assert observed_result == expected


def test_main_bad_secret_key(cursor_fixture, mocker):
    """Checks that using bad secret key with API returns 403."""

    with application.test_client() as c:

        example_query.CURSOR = cursor_fixture

        apikey = 'abc'
        apisecret = 'bad_secret'

        hmac = Hmac()
        hmac.hmac_keys = {apikey: apisecret}
        body = json.dumps({'a': '1'})
        body_hash = hmac.make_hmac_for(apikey, body)

        headers = {"Public-Key": apikey, "Signature": body_hash, "Content-Type": "application/json" }

        rv = c.post(
            'http://127.0.0.1:5000/process',
            json={'a': '1'},
            headers=headers
        )

        rv == 403


{%- endif %}
