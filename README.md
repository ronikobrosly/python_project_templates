# python_project_templates

Cookiecutter templates for python projects (complete with makefiles, dockerfiles, pytest testing templates, pylint, and more)



## Current list of templates

* Generic python project template: `generic`
* API/model serving template: `API`
* Analytics project: `analytics`


## Installation and Usage

To create a new python project:

1) You'll need to first install python. Feel free to use whatever installation method you want, but we recommend installing `pyenv-virtualenv` through homebrew, this way you can easily switch between versions of python and easily create your own virtual environments.

2) Install [Docker](https://www.docker.com/products/docker-desktop).

3) With whatever version of python you're working with, install cookiecutter through `pip install`:

```
pip install cookiecutter~=1.7.0
```

4) Run the following commands (assumes Mac OS):

```
cd ~
mkdir projects
cd projects
git clone -b develop git@github.com:ronikobrosly/python_project_templates.git
```

5) Then decide which template you need and run one of the following commands:

* `cookiecutter ./python_project_starter/generic`
* `cookiecutter ./python_project_starter/API`
* `cookiecutter ./python_project_starter/analytics`

You'll be prompted to answer a few questions in your terminal and then you're good to go! Cookiecutter will create a new project folder for you,
along with all the necessary files, and initialize it all as a git repo.
