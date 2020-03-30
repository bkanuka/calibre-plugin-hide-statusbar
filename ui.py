#!/usr/bin/env python2
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import absolute_import, division, print_function, unicode_literals

__license__   = 'GPL v3'
__copyright__ = '2020, Bennett Kanuka <bkanuka@gmail.com>'
__docformat__ = 'restructuredtext en'


# The class that all interface action plugins must inherit from
from calibre.gui2.actions import InterfaceAction

class InterfacePlugin(InterfaceAction):

    name = 'Hide Statusbar'
    action_spec = ('Toggle Statusbar', 'dialog_information.png',
                        'Toggle Statusbar', 'Ctrl+Shift+S')

    def gui_layout_complete(self):
        self.gui.status_bar.hide()
        self.qaction.triggered.connect(self.toggle)

    def toggle(self):
        if self.gui.status_bar.isVisible():
            self.gui.status_bar.hide()
        else:
            self.gui.status_bar.show()

