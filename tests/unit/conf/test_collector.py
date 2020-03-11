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
from article_synchronizer.conf.collector import collect_parser


def test_collect_parser():
    args = ['--article-dir', '~/Boostnote', '--collector-name', 'boostnote']
    known_args = collect_parser.parse_known_args(args)
    print(known_args[0])
    # assert collect_parser.article_dir == '~/Boostnote'
    # assert collect_parser.collect_name == 'boostnote'

test_collect_parser()
