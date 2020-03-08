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


class Article(object):
    def __init__(self,
                 created_at,
                 updated_at,
                 type,
                 title,
                 tags,
                 content,
                 lines_highlighted,
                 is_starred,
                 is_trashed):
        self.created_at = created_at
        self.updated_at = updated_at
        self.type = type
        self.title = title
        self.tags = tags
        self.content = content
        self.lines_highlighted = lines_highlighted
        self.is_starred = is_starred
        self.is_trashed = is_trashed