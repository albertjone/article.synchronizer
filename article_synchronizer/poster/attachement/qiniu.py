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
import requests
from qiniu import Auth, put_file
from datetime import datetime
from article_synchronizer.poster.attachement.base import BaseAttaDriver


class QiniuAttaDriver(BaseAttaDriver):
    TOKEN = None
    TOKEN_CREATE = None
    EXPIRE_TIME = 3600


    def __init__(self, ak, sk, bucket_domain):
        self.ak = ak
        self.sk = sk
        self.auth = Auth(self.ak, self.sk)
        self.bucket_domain = bucket_domain

    def _get_auth_token(self, bucket_name):
        expired = False
        if self.TOKEN:
            if (datetime.now() - self.TOKEN_CREATE).total_seconds() >= 3600:
                expired = True
        else:
            expired = True
        if expired:
            self.TOKEN_CREATE = datetime.now()
            self.TOKEN = self.auth.upload_token(
                bucket_name,
                expires=self.EXPIRE_TIME
            )
        return self.TOKEN

    def _get_atta_name(self, atta):
        note, atta = atta.split('/')[-2:]
        return '%s:%s' %(note, atta)

    def get_atta_by_path(self, atta, bucket_name):
        token = self._get_auth_token(bucket_name)
        url = 'http://%s/%s' % (
            self.bucket_domain, self._get_atta_name(atta))
        private_url = self.auth.private_download_url(url, expires=3600)
        print(private_url)
        r = requests.get(private_url)
        print(r.text)
        return r

    def save_atta_by_path(self, atta, bucket_name):
        token = self._get_auth_token(bucket_name)
        ret, info = put_file(token, self._get_atta_name(atta), atta)
        print(ret, info)
        return (ret, info)
