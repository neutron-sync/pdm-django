import argparse
import subprocess
import sys

from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.run import Command as RunCommand


class ManageCommand(RunCommand):
  """shortcut for pdm run python manage.py"""

  @staticmethod
  def _run_command(project, args, **kwargs):
    args = ['python', 'manage.py'] + args
    return RunCommand._run_command(project, args, **kwargs)


class AdminCommand(RunCommand):
  """shortcut for pdm run django-admin"""

  @staticmethod
  def _run_command(project, args, **kwargs):
    args = ['django-admin'] + args
    return RunCommand._run_command(project, args, **kwargs)


def reg_commands(core):
  core.register_command(ManageCommand, "manage")
  core.register_command(AdminCommand, "django-admin")
