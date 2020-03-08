# Copyright (C) 2020 xiaojueguan
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import locale
import sys
import six

# only for developing
sys.path.append("../")

from article_synchronizer.scheduler import Scheduler


def main(argv=None):
    try:
        if argv is None:
            argv = sys.argv[1:]
            if six.PY2:
                # Emulate Py3, decode argv into Unicode based on locale so that
                # commands always see arguments as text instead of binary data
                encoding = locale.getpreferredencoding()
                if encoding:
                    argv = map(lambda arg: arg.decode(encoding), argv)
            #TODO Initialize the scheduler
        Scheduler().run(argv)

    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    sys.exit(main())
