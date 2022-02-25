import argparse
import subprocess
import sys

from pdm.cli.utils import PdmFormatter
from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.run import Command as RunCommand
from pdm.cli.commands.run import TaskRunner
from pdm.cli.utils import check_project_file


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
    options.command = self.COMMAND_PREFIX[0]

    check_project_file(project)
    runner = TaskRunner(project)
    runner.global_options.update({"site_packages": options.site_packages})
    sys.exit(runner.run(options.command, self.COMMAND_PREFIX[1:] + options.args))


class ManageCommand(DjangoRunCommand):
  """shortcut for pdm run python manage.py"""

  COMMAND_PREFIX = ['python', 'manage.py']


class AdminCommand(DjangoRunCommand):
  """shortcut for pdm run django-admin"""

  COMMAND_PREFIX = ['django-admin']


def reg_commands(core):
  core.register_command(ManageCommand, "manage")
  core.register_command(AdminCommand, "django-admin")
