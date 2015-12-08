# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8
#
# Yum Kernel Module Support for PLD Linux
# Plugin for handling setting kernel packages as installonlypkgs in transaction
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# by Elan Ruusamäe <glen@pld-linux.org>

from yum.plugins import PluginYumExit
from yum.misc import unique
from yum.packages import YumInstalledPackage
from yum.plugins import TYPE_CORE
from yum.constants import TS_INSTALL

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

knames = ['kernel', 'kernel-smp', 'kernel-grsecurity', 'kernel-grsecurity-smp', 'kernel-desktop', 'kernel-laptop', 'kernel-vanilla']
ksubpkgs = ['drm', 'pcmcia', 'sound-oss', 'sound-alsa']

def preresolve_hook(conduit):
    ts = conduit.getTsInfo()

    for te in ts.getMembers():
        if te.ts_state != 'u':
            continue

        pkgname = te.name
        if pkgname in knames:
            conduit.info(2, 'Marking package %s for installation' % pkgname)
            te.ts_state = 'i'
            te.output_state = TS_INSTALL
            continue

        for kname in knames:
            if pkgname.startswith(kname + '-'):
                r = pkgname[len(kname) + 1:]
                if r in ksubpkgs:
                    conduit.info(2, 'Marking package %s for installation' % pkgname)
                    te.ts_state = 'i'
                    te.output_state = TS_INSTALL

# vim:ts=4:sw=4:expandtab
