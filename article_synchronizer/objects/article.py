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
from article_synchronizer import utils
from article_synchronizer import poster

class Article(object):
    def __init__(self, *args, **kwargs):
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')
        self.type = kwargs.get('type')
        self.title = kwargs.get('title')
        self.tags = kwargs.get('tags')
        self.content = kwargs.get('content')
        self.lines_highlighted = kwargs.get('lines_highlighted')
        self.is_starred = kwargs.get('is_starred')
        self.is_trashed = kwargs.get('is_trashed')
        self.attachements = kwargs.get('attachements')
        self.folder_name = kwargs.get('folder_name')
        self.folder = kwargs.get('folder')
        self.atta_driver = kwargs.get('atta_driver_name', 'qiniu')
        self._setup_article()

    def _setup_article(self):
        self._load_atta_driver()
        for atta in self.attachements:
            self._post_attachement(atta)

    def _load_atta_driver(self):
        poster.get_atta_poster_driver_by_name(self.atta_driver)

    def _post_attachement(self, atta):
        temp = self.atta_driver.get_atta_by_path(atta)
        if utils.cmp(temp, atta):
            return
        url = self._atta_driver.save_atta_by_path(atta)
        return {atta, url}
