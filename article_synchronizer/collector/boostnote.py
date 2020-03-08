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


from article_synchronizer.collector.base import CollectorBase


class BoostnoteCollector(CollectorBase):
    """The note schema
        {
            "createdAt": "2019-03-24T03:11:54.069Z",
            "updatedAt": "2019-03-24T03:40:45.129Z",
            "type": "MARKDOWN_NOTE",
            "folder": "279b9950aaa1780b083b",
            "title": "horizon 无法访问，This site can’t be reached",
            "tags": [],
            "content": "## horizon 无法访问![b0015c5a.png](:storage/0c762b83-9100-4e72-a78a-62a4d49d2864/b0015c5a.png)\n\n\n\n\n",
            "linesHighlighted": [],
            "isStarred": False,
            "isTrashed": False,
            "attachements: ["Users/xiaojueguan/Boostnote/attachments/0c762b83-9100-4e72-a78a-62a4d49d2864/b0015c5a.png"]
        }
    """

    notes_dir = 'notes'
    attachments_dir = 'attachments'
    boostnote_file = 'boostnote.json'

    def _get_boostnote_dict(self, file_path):
        return self._get_content(file_path, file_type=self.JSON)

    def _get_note_file_dict(self, files):
        note_file_dict = {
            files.split('/')[-1]: self._get_content(file, self.CSON)
            for file in files}
        return note_file_dict
   
    def _get_atta_dict(self, atta_dir):
        atta_dict = {
            dir.split('/')[-1]: self._get_all_files_in_dir(dir)
            for dir in self._get_all_dirs_in_dir(atta_dir)
        }
        return atta_dict

    def _get_note_dict(self, note_dir):
        note_dict = {
            file.split('/')[-1]: self._get_content(file, self.CSON)
            for file in self._get_all_files_in_dir(note_dir)
        }
        return note_dict

    def _add_atta_to_note(self, note_dict, atta_dict):
        for key, note in note_dict.items():
            note['attachements'] = atta_dict.get(key)

    def _add_folder_to_note(self, note_dict, boosnote_dict):
        folder_dict = boosnote_dict.get('folders')
        for item in folder_dict:
            for key, note in note_dict.items():
                if item['key'] == note['folder']:
                    note['folder_name'] = item['name']

    def _get_articles(self, articles_dir):
        notes_dir = self._concatenate_path(
            articles_dir, self.notes_dir)
        atta_dir = self._concatenate_path(
            articles_dir, self.attachments_dir)
        boostnote_file = self._concatenate_path(
            articles_dir, self.boostnote_file)

        boosnote_dic = self._get_boostnote_dict(boostnote_file)
        atta_dict = self._get_atta_dict(atta_dir)
        note_dict = self._get_note_dict(notes_dir)
        self._add_atta_to_note(note_dict, atta_dict)
        self._add_folder_to_note(note_dict, boosnote_dic)
        return note_dict
        

