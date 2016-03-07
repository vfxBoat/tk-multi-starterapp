# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
import os
import sys
import threading

# by importing QT from sgtk rather than directly, we ensure that
# the code will be compatible with both PySide and PyQt.
from sgtk.platform.qt import QtCore, QtGui
from .ui.dialog import Ui_Dialog

def show_dialog(app_instance, entity_type, entity_ids):
    """
    Shows the main dialog window, using the special Shotgun multi-select mode.
    """
    # in order to handle UIs seamlessly, each toolkit engine has methods for launching
    # different types of windows. By using these methods, your windows will be correctly
    # decorated and handled in a consistent fashion by the system.

    # we pass the dialog class to this method and leave the actual construction
    # to be carried out by toolkit.
<<<<<<< HEAD
    app_instance.engine.show_dialog("Starter Template App...", app_instance, AppDialog)

=======
    app_instance.engine.show_dialog("Starter Template App",    # window title
                                    app_instance,              # app instance
                                    AppDialog,                 # window class to instantiate
                                    entity_type,               # arguments to pass to constructor
                                    entity_ids)

>>>>>>> tk-multi-starterapp/shotgun_multi_select


class AppDialog(QtGui.QWidget):
    """
    Main application dialog window
    """
<<<<<<< HEAD

    def __init__(self):
=======

    def __init__(self, entity_type, entity_ids):
>>>>>>> tk-multi-starterapp/shotgun_multi_select
        """
        Constructor
        """
        # first, call the base class and let it do its thing.
        QtGui.QWidget.__init__(self)

        # now load in the UI that was created in the UI designer
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # most of the useful accessors are available through the Application class instance
        # it is often handy to keep a reference to this. You can get it via the following method:
        self._app = sgtk.platform.current_bundle()

        # via the self._app handle we can for example access:
        # - The engine, via self._app.engine
        # - A Shotgun API instance, via self._app.shotgun
        # - A tk API instance, via self._app.tk

        # lastly, set up our very basic UI
<<<<<<< HEAD
        self.ui.context.setText("Current Context: %s" % self._app.context)


=======
        self.ui.context.setText("Current selection type: %s, <br>Currently selected ids: %s" % (entity_type, entity_ids))


>>>>>>> tk-multi-starterapp/shotgun_multi_select
