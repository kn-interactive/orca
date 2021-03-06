# Orca
#
# Copyright 2010 Informal Informatica LTDA.
# Author: Jose Vilmar <vilmar@informal.com.br>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the
# Free Software Foundation, Inc., Franklin Street, Fifth Floor,
# Boston MA  02110-1301 USA.

"""Custom script for Eclipse."""
__id__        = "$Id$"
__version__   = "$Revision$"
__date__      = "$Date$"
__copyright__ = "Copyright (c) 2010 Informal Informatica LTDA."
__license__   = "LGPL"

import orca.orca as orca
import orca.scripts.toolkits.GAIL as GAIL
import pyatspi

########################################################################
#                                                                      #
# The Eclipse script class.                                            #
#                                                                      #
########################################################################
class Script(GAIL.Script):

    def __init__(self, app):
        """Creates a new script for the given application."""
        GAIL.Script.__init__(self, app)
        self.movementKeys = ["Up", "Down", "Left", "Right", "Page_Up",
                   "Page_Down", "Home", "End"]

    def _presentTextAtNewCaretPosition(self, event, otherObj=None):
        """Updates braille and outputs speech for the event.source or the
        otherObj. Overridden here so that we can give more feedback to user.
        """

        # Let the default script's normal behavior do its thing
        #
        GAIL.Script._presentTextAtNewCaretPosition(self, event, otherObj)

        # check if the obj was spoken in the default script
        lastKey, mods = self.utilities.lastKeyAndModifiers()
        if lastKey in self.movementKeys:
            # already spoken in default script
            return

        obj = otherObj or event.source
        if obj.getState().contains(pyatspi.STATE_SINGLE_LINE):
            return

        # if Tab key is pressed and there is text selected, we must announce
        # the text selected because probably we are in a parameter list
        # and we are jumping between the parameters with the tab key. 
        hasSelection = False
        if lastKey in ["Tab", "ISO_Left_Tab"]:
            [text, startOffset, endOffset] = self.utilities.selectedText(obj)
            hasSelection = endOffset > 0

        if hasSelection:
            self.sayPhrase(obj, startOffset, endOffset)
        else:
            self.sayLine(obj)

        self._saveLastTextPosition(obj)

    def onFocus(self, event):
        """Callback for focus: accessibility events."""

        # NOTE: This event type is deprecated and Orca should no longer use it.
        # This callback remains just to handle bugs in applications and toolkits.

        role = event.source.getRole()

        menuItems = [pyatspi.ROLE_CHECK_MENU_ITEM,
                     pyatspi.ROLE_MENU,
                     pyatspi.ROLE_MENU_ITEM,
                     pyatspi.ROLE_RADIO_MENU_ITEM]
        if role in menuItems:
            orca.setLocusOfFocus(event, event.source)
            return

        if role == pyatspi.ROLE_PANEL:
            orca.setLocusOfFocus(event, event.source)
            return

        super().onFocus(event)

    def onTextInserted(self, event):
        """Called whenever text is inserted into an object. Overridden here
        so that we can avoid speaking text when caret moves after new text
        is inserted.

        Arguments:
        - event: the Event
        """

        if self.utilities.isTextArea(event.source):
            length = event.source.queryText().characterCount
            if event.detail1 == 0 and event.detail2 == length:
                # seems to be generated by a reformat (ctrl+shift+f)
                # or by commenting some block (ctrl+/).
                # if not discarded, orca will speak all the text of the file.
                return
            # Let the default script's normal behavior do its thing
            GAIL.Script.onTextInserted(self, event)
            self._saveLastTextPosition(event.source)

    def onTextDeleted(self, event):
        """Called whenever text is deleted from an object.  Overridden here
        so that we can avoid speaking text when caret moves after new text
        is deleted.

        Arguments:
        - event: the Event
        """

        # Let the default script's normal behavior do its thing
        #
        GAIL.Script.onTextDeleted(self, event)
        self._saveLastTextPosition(event.source)

    def _saveLastTextPosition(self, obj):
        if self.utilities.isTextArea(obj):
            self._saveLastCursorPosition(obj, obj.queryText().caretOffset)

    def onSelectionChanged(self, event):
        """Callback for object:selection-changed accessibility events."""

        obj = event.source
        state = obj.getState()
        # sometimes eclipse issues an object:selection-changed for objects not focused.
        # we do not want that orca announces this objects.

        if not state.contains(pyatspi.STATE_FOCUSED):
            # the exception, at least for while, is the MenuBar
            if obj.getRole() != pyatspi.ROLE_MENU_BAR:
                return
        GAIL.Script.onSelectionChanged(self, event)

