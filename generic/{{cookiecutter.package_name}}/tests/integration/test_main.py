""" Tests the full pipeline of the app """

{% if cookiecutter.requires_database_support == 'yes' -%}
from {{cookiecutter.package_name}} import example_query
from {{cookiecutter.package_name}}.__main__ import main


def test_main(cursor_fixture, mocker):
    """Tests the full pipeline for the app."""

    example_query.CURSOR = cursor_fixture

    observed_query_result, observed_math_result  = main()
    observed_query_result_length = len(observed_query_result)

    assert observed_math_result == 1000
    assert observed_query_result_length == 3
{%- endif %}
{% if cookiecutter.requires_database_support == 'no' -%}
from {{cookiecutter.package_name}}.__main__ import main


def test_main():
    """Tests the full pipeline for the app."""

    observed_math_result  = main()
    assert observed_math_result == 1000

{%- endif %}
