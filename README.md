# Mini_Proj1_Fuyao_Li

### Author name: Fuyao Li

## Overview
This repository contains a Python project skeleton including:
+ .devcontainer: development container to ensure consistency, portability, and isolation for your projects development environment
    - `devcontainer.json` 
    - `Dockerfile`
+ Makefile: highly valuable tool for easy command line entries as well as CI/CD yaml commands.
+ CI/CD: functioning CI/CD for setup, lint, test 
+ README.md: Show the overview of the repo and how to set up and run the repo

## Set up
1. Clone the repository:
``` shell
git clone git@github.com:nogibjj/Mini_Proj1_Fuyao_Li.git
```
2. Create a virtual environment
``` shell
conda create --name test python=3.9
conda activate test
```
3. Install required packages
``` shell
pip install -r requirements.txt
```