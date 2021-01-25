""" Contains tests and assertions for example_transformation module """


from {{cookiecutter.package_name}}.example_transformation import example_function


def test_example_function():
    """ Tests that that math of the `example_function` is correct """

    observed_result = example_function(2)
    expected_result = 20
    assert observed_result == expected_result


def test_something_else():
    """ Add more tests here, but make sure function begins with `test_` """

    assert True
