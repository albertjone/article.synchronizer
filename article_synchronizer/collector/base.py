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


import abc
from article_synchronizer import utils


class CollectorBase(object):
    """
    Base class of collector
    """
    # file type
    JSON = "JSON"
    YAML = "YANL"
    CSON = "CSON"
    RAW = 'RAW'

    def __init__(self):
        """no params"""
        pass

    @staticmethod
    def _get_content(file_path, file_type):
        return utils.get_file_content(file_path, file_type)
        
    def _get_all_files_in_dir(self, dir_name):
        """dir_name must be a absolute path"""
        return utils.get_all_files_in_dir(dir_name)

    def _get_all_dirs_in_dir(self, dir_name):
        """dir_name must be a absolute path"""
        return utils.get_all_dirs_in_dir(dir_name)

    def _concatenate_path(self, root_path, args):
        return utils.concatenate_path(root_path, args)

    @abc.abstractmethod
    def _get_articles(self, articles_dir):
        """All subclass should implement the method"""

    def get_articles(self, articles_dir):
        """all revoker should invoke this method"""
        articles_dir = utils.get_abs_path(articles_dir)
        articles = self._get_articles(articles_dir)
        return articles

