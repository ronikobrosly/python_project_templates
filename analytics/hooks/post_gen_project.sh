#!/usr/bin/env bash


# Install the basic packages needed for the template to work
echo "Installing basic packages needed for template"
pip install -r requirements.txt

# Initatialize git in new project
git init
git add .
git commit -m "Initial commit"
echo "Made initial commit to {{cookiecutter.project_repo}}"

# Creating develop branch
git checkout -b develop
