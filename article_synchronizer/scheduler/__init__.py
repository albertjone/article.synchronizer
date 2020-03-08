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


from six.moves import input
from article_synchronizer.collector import get_collector
from article_synchronizer.collector import COLLECTORS
from article_synchronizer import utils

class Scheduler(object):
    def __init__(self):
        pass

    def run(self, argv):
        # collector
        flag = True
        while flag:
            print('Current avaiable client is boostnote')
            print('Please input your client name:')
            client_name = input()
            if client_name in COLLECTORS:
                flag = False
        flag = True
        while flag:
            print('Please input your articles directory:')
            articles_dir = input()
            if utils.is_dir_exits(articles_dir):
                flag = False
        flag = True
        collector = get_collector(client_name)
        blogs = collector.get_articles(articles_dir)
        # poster
        print('Please input your login url:')
        login_url = input()
        print('Please input user name')
        user_name = input()
        print('Please input password')
        password = input()

            