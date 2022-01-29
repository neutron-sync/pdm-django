# pdm-django: Django shortcuts for PDM

## Install

`pdm plugin add pdm-django`

## Usage

### manage.py

Example: `pdm manage runserver`

### django-admin

Example: `pdm django-admin startproject narf`

## Configuring .env

pdm-django inherits from the `pdm run` command, so if you would like to load a dotenv file, use the same notation in your `pyproject.toml` file.

```toml
[tool.pdm.scripts]
_.env_file = ".env"
```
