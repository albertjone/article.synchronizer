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
from article_synchronizer.poster.attachement.qiniu import QiniuAttaDriver
from unittest import TestCase
import os


# class TestQiniuAttaDriver(TestCase):

ak = 'BuQqHKUu2j3QYze_yXBHjd3JtUCBVQWcjOKtw1zZ'
sk = '3JG79bjDaWvCA6ROqnWTSGNPvyJpDipGmHek5BGr'

file_path = '/Users/steveguan/code/Interest/Boostnote/attachments/0c762b83-9100-4e72-a78a-62a4d49d2864/b0015c5a.png'
file_name = '0c762b83-9100-4e72-a78a-62a4d49d2864:b0015c5a.png'


class TestQiniuAttaDriver():
    def setup(self):
        self.tf = '/tmp/article.synchronizer/' \
                  '0c762b83-9100-4e72-a78a-62a4d49d2864/b0015c5a.png'
        self.f_ct = 'Article.synchronizer is the most wanting tool' \
                    'i want to dev'
        self.bucket_domain = 'cdn.dawncreat.com'
        self.bucket_name = 'dawncreat'
        os.mkdir(self.tf)
        with open(self.tf, 'w') as fd:
            fd.write(self.f_ct)
        self.driver = QiniuAttaDriver(ak, sk, self.bucket_domain)

    def test_save_atta_by_path(self):
        
        ret, info = self.driver.save_atta_by_path(self.tf, self.bucket_name)
        assert info.status_code == 200


    def test_get_atta_name(self):
        tem_file = self.driver._get_atta_name(self.tf)
        assert tem_file == '%s:%s' % tuple(tem_file.split('/')[-2:])

    def test_get_atta_by_path(self):
        tf = self.driver.get_atta_by_path(self.tf, self.bucket_name)
        assert self.f_ct == os.read(tf)

    def test_get_atta_url_by_path(self, atta, bucket_domain):
        url = self.driver.get_atta_url_by_path(self.tf, self.bucket_name)
        assert url is not None







# ret, info = driver.save_atta_by_path(file_path, bucket_name)
# print(ret, info)
# url = driver.get_atta_url_by_path(file_path, bucket_name)
# print(url)
# driver.get_atta_by_path(file_path, bucket_name)
