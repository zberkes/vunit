# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2016, Lars Asplund lars.anders.asplund@gmail.com

"""
This script will run the VUnit test suite using tox.
"""
from subprocess import check_call
from vunit import ROOT

check_call('tox', cwd=ROOT, shell=True)
