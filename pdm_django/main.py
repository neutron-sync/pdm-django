import argparse
import subprocess
import sys

from pdm.cli.utils import PdmFormatter
from pdm.cli.commands.base import BaseCommand
from pdm.cli.commands.run import Command as RunCommand
from pdm.cli.commands.run import TaskRunner
from pdm.cli.hooks import HookManager
from pdm.cli.utils import check_project_file


class DjangoRunCommand(RunCommand):
  OPTIONS = []
  COMMAND_PREFIX = []

  def add_arguments(self, parser):
    parser.add_argument(
      "-s",
      "--site-packages",
      action="store_true",
      help="Load site-packages from the selected interpreter",
    )
    parser.add_argument(
      "args",
      nargs=argparse.REMAINDER,
      help="Arguments that will be passed to the command",
    )

  def handle(self, project, options):
    options.list = False
    options.command = self.COMMAND_PREFIX[0]

    check_project_file(project)
    hooks = HookManager(project, options.skip)
    runner = TaskRunner(project, hooks=hooks)
    if options.site_packages:
      runner.global_options.update({"site_packages": options.site_packages})

    sys.exit(runner.run(options.command, self.COMMAND_PREFIX[1:] + options.args))

    hooks.try_emit("pre_run", script=options.command, args=options.args)
    exit_code = runner.run(options.command, self.COMMAND_PREFIX[1:] + options.args)
    hooks.try_emit("post_run", script=options.command, args=options.args)
    sys.exit(exit_code)


class ManageCommand(DjangoRunCommand):
  """shortcut for pdm run python manage.py"""

  COMMAND_PREFIX = ['python', 'manage.py']


class AdminCommand(DjangoRunCommand):
  """shortcut for pdm run django-admin"""

  COMMAND_PREFIX = ['django-admin']


def reg_commands(core):
  core.register_command(ManageCommand, "manage")
  core.register_command(AdminCommand, "django-admin")
