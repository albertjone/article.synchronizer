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
from abc import ABC
from abc import abstractclassmethod


class BaseAttaDriver(ABC):
    @abstractclassmethod
    def get_atta_by_path(self, atta, bucket_name):
        """return an attachement"""

    @abstractclassmethod
    def save_atta_by_path(self, atta, bucket_name):
        """save an attachement and return an url"""
