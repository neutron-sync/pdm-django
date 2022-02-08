import argparse
import subprocess
import sys

from pdm.cli.utils import PdmFormatter
from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.run import Command as RunCommand


class DjangoRunCommand(RunCommand):
  OPTIONS = []
  COMMAND_PREFIX = []

  def add_arguments(self, parser):
    parser.add_argument(
      "args",
      nargs=argparse.REMAINDER,
      help="Arguments that will be passed to the command",
    )

  def handle(self, project, options):
    options.list = False
    options.site_packages = False
    options.command = 'django'
    super().handle(project, options)

  @classmethod
  def _run_command(cls, project, args, **kwargs):
    # remove dummy command
    args.pop(0)

    # add real command
    args = cls.COMMAND_PREFIX + args
    return RunCommand._run_command(project, args, **kwargs)


class ManageCommand(DjangoRunCommand):
  """shortcut for pdm run python manage.py"""

  COMMAND_PREFIX = ['python', 'manage.py']


class AdminCommand(DjangoRunCommand):
  """shortcut for pdm run django-admin"""

  COMMAND_PREFIX = ['django-admin']


def reg_commands(core):
  core.register_command(ManageCommand, "manage")
  core.register_command(AdminCommand, "django-admin")
