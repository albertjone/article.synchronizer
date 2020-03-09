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
from article_synchronizer.poster.attachement.qiniu import *
from unittest import TestCase


# class TestQiniuAttaDriver(TestCase):

ak = ''
sk = ''
bucket_domain = 'dawncreat.s3-cn-east-1.qiniucs.com'
bucket_name = 'dawncreat'
file_path = '/Users/steveguan/code/Interest/Boostnote/attachments/0c762b83-9100-4e72-a78a-62a4d49d2864/b0015c5a.png'
file_name = '0c762b83-9100-4e72-a78a-62a4d49d2864:b0015c5a.png'


driver = QiniuAttaDriver(ak, sk, bucket_domain)
driver.save_atta_by_path(file_path, bucket_name)
driver.get_atta_by_path(file_path, bucket_name)
