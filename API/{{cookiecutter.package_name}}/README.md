# {{cookiecutter.package_name}} API

- [Changelog](#version)
- [About](#about)
- [Installation](#installation)
- [Commands](#commands)


## About

Add something here, in plain language, about the purpose of {{cookiecutter.package_name}}.


## Changelog


0.0.1 ({% now 'local', '%m/%d/%Y' %}):
* Project started


## Installation

Add instructions here if necessary. Make them clear, simple, and step-by-step.


## Commands

`python -m {{cookiecutter.package_name}}`: run the python code as it is, outside of a container (make sure you have all requirements installed)

`make build-image`: builds the docker image from scratch or rebuilds after code changes

`make run`: run the docker container in the background

`make stop`: stop the docker container running in the background

`make clean`: cleans the code with python `black` and then gives a `pylint` report for syntax and style issues. Note that black and pylint must be installed (see `requirements.txt`)

`make test`: starts `pytest` to run all unit and integration tests **within the docker container**

`make pyshell`: starts a python shell **within the docker container**
