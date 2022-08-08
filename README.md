# pdm-django: Django command shortcuts for PDM

A plugin that gives you command shortcuts for developing with [PDM](https://pdm.fming.dev/).

`pdm run python manage.py runserver` -> `pdm manage runserver`

`pdm run django-admin startproject narf` -> `pdm django-admin startproject narf`

## Requirements

Tested with PDM 2.1.X

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

## CLI Option Conflicts

You may run into some options conflicts between the `pdm` command and the Django command you run. As of right now the only one I can find is `pdm manage --help` for which you will get the pdm help instead of the Django help. However, note you can still run `pdm manage` or `pdm manage help` to view the Django help. Same situation applies for `pdm django-admin --help`.

## Shameless Plugs

I built this library originally for the [NeutronSync Service](https://www.neutronsync.com/). So if you would like to support this project please support the service with a subscription to NeutronSync or a [donation](https://github.com/sponsors/neutron-sync) to the open source libraries.
