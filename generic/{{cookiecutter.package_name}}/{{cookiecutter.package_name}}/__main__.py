"""Main entry point for app"""


from {{cookiecutter.package_name}}.example_transformation import example_function
{% if cookiecutter.requires_database_support == 'yes' -%}
from {{cookiecutter.package_name}}.example_query import query_module
{%- endif %}

def main():
    """
    Main function

    Args: None
    Returns: None
    """
    {% if cookiecutter.requires_database_support == 'yes' -%}
    # Query
    query_result = query_module()

    # Do some basic math
    math_result = example_function(100)

    # Final result
    return query_result, math_result
    {%- endif %}
    {% if cookiecutter.requires_database_support == 'no' -%}
    # Do some basic math
    math_result = example_function(100)

    # Final result
    return math_result
    {%- endif %}


if __name__ == "__main__":
    main()
