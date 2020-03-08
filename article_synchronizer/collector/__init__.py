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


COLLECTORS = {
    "boostnote":
        ("article_synchronizer.collector.boostnote", "BoostnoteCollector")
}


def get_collector(client, collectors=COLLECTORS):
    if client in collectors:
        mod_name, client_name = collectors[client]
        _mod = __import__(mod_name, globals(), locals(), [client_name])
        return getattr(_mod, client_name)
    raise AttributeError("%s not exists in %s" % (mod_name, client_name))
