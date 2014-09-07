#!/usr/bin/python

"""Test of sayAll."""

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_Add"))
sequence.append(utils.AssertPresentationAction(
    "1. KP_Add to do a SayAll",
    ["SPEECH OUTPUT: 'Home'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'News'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Projects'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Art'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Support'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Development'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Community'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'live.gnome.org '",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'entry Search'",
     "SPEECH OUTPUT: 'Titles push button grayed Text push button grayed'",
     "SPEECH OUTPUT: 'Home'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'RecentChanges'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'FindPage'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'HelpContents'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Orca'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'en Español'",
     "SPEECH OUTPUT: 'Home'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'Download/Installation'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'Configuration/Use'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'Accessible Applications'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | orca-list image link'",
     "SPEECH OUTPUT: 'Mailing List'",
     "SPEECH OUTPUT: ' ( orca-list image link'",
     "SPEECH OUTPUT: 'Archives'",
     "SPEECH OUTPUT: ') | '",
     "SPEECH OUTPUT: 'FAQ'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' | '",
     "SPEECH OUTPUT: 'DocIndex'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Welcome to Orca!'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Orca Logo'",
     "SPEECH OUTPUT: 'HOT HOT HOT: Notes on '",
     "SPEECH OUTPUT: 'access to Firefox 3.0'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Contents'",
     "SPEECH OUTPUT: '1.'",
     "SPEECH OUTPUT: 'Welcome to Orca!'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '2.'",
     "SPEECH OUTPUT: 'About'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '3.'",
     "SPEECH OUTPUT: 'Audio Guides'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '4.'",
     "SPEECH OUTPUT: 'Download/Installation'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '5.'",
     "SPEECH OUTPUT: 'Configuration/Use'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '6.'",
     "SPEECH OUTPUT: 'Accessible Applications'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '7.'",
     "SPEECH OUTPUT: 'How Can I Help?'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '8.'",
     "SPEECH OUTPUT: 'More Information'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'About'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Orca is a free, open source, flexible, extensible, and powerful assistive technology for people with visual impairments. Using various combinations of speech synthesis, braille, and magnification, Orca helps provide access to applications and toolkits that support the AT-SPI (e.g., the GNOME desktop). The development of Orca has been led by the access image link'",
     "SPEECH OUTPUT: 'Accessibility Program Office of Sun Microsystems, Inc.'",
     "SPEECH OUTPUT: ' with '",
     "SPEECH OUTPUT: 'contributions from many community members'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '.'",
     "SPEECH OUTPUT: 'The complete list of work to do, including bugs and feature requests, along with known problems in other components, is maintained in buglist image link'",
     "SPEECH OUTPUT: 'Bugzilla'",
     "SPEECH OUTPUT: ' (please see our '",
     "SPEECH OUTPUT: 'notes on how we use Bugzilla'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ').'",
     "SPEECH OUTPUT: 'Please join and participate on the orca-list image link'",
     "SPEECH OUTPUT: 'Orca mailing list'",
     "SPEECH OUTPUT: ' ( orca-list image link'",
     "SPEECH OUTPUT: 'archives'",
     "SPEECH OUTPUT: '): it's a helpful, kind, and productive environment composed of users and developers.'",
     "SPEECH OUTPUT: 'Audio Guides'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Darragh \xd3 H\xe9iligh'",
     "SPEECH OUTPUT: ' has created several audio guides for Orca. This is a fantastic contribution (THANKS!)!!! The audio guides can be found at linuxat image link'",
     "SPEECH OUTPUT: 'http://www.digitaldarragh.com/linuxat.asp'",
     "SPEECH OUTPUT: ' and include the following:'",
     "SPEECH OUTPUT: '• ubuntu-7-4-install-walk-through image link'",
     "SPEECH OUTPUT: 'Walk through of the installation of Ubuntu 7.4. Very helpful tutorial'",
     "SPEECH OUTPUT: '• linux-and-orca-review image link'",
     "SPEECH OUTPUT: 'Review of Fedora 7 and the Orca screen reader for the Gnome graphical desktop'",
     "SPEECH OUTPUT: '• installing-firefox-and-orca image link'",
     "SPEECH OUTPUT: 'Guide to installing the latest versions of Firefox and Orca'",
     "SPEECH OUTPUT: 'Download/Installation'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'As of GNOME 2.16, Orca is a part of the GNOME platform. As a result, Orca is already provided by default on a number of operating system distributions, including www.opensolaris.org image link'",
     "SPEECH OUTPUT: 'Open Solaris'",
     "SPEECH OUTPUT: ' and www.ubuntu.com image link'",
     "SPEECH OUTPUT: 'Ubuntu'",
     "SPEECH OUTPUT: '.'",
     "SPEECH OUTPUT: 'Please also refer to the '",
     "SPEECH OUTPUT: 'Download/Installation page'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for detailed information on various distributions as well as installing Orca directly from source.'",
     "SPEECH OUTPUT: 'Configuration/Use'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'The command to run orca is orca. You can enter this command by pressing Alt+F2 when logged in, waiting for a second or so, then typing orca and pressing return. Orca is designed to present information as you navigate the desktop using the keynav-1 image link'",
     "SPEECH OUTPUT: 'built-in navigation mechanisms of GNOME'",
     "SPEECH OUTPUT: '. These navigation mechanisms are consistent across most desktop applications.'",
     "SPEECH OUTPUT: 'You may sometimes wish to control Orca itself, such as bringing up the '",
     "SPEECH OUTPUT: 'Orca Configuration GUI'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' (accessed by pressing Insert+Space when Orca is running) and for using flat review mode to examine a window. Refer to '",
     "SPEECH OUTPUT: 'Orca Keyboard Commands'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '(Laptop Layout)'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for more information on Orca-specific keyboard commands. The '",
     "SPEECH OUTPUT: 'Orca Configuration GUI'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' also includes a \"Key Bindings\" tab that allows you to get a complete list of Orca key bindings.'",
     "SPEECH OUTPUT: 'Please also refer to the '",
     "SPEECH OUTPUT: 'Configuration/Use page'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for detailed information.'",
     "SPEECH OUTPUT: 'Accessible Applications'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'Orca is designed to work with applications and toolkits that support the assistive technology service provider interface (AT-SPI). This includes the GNOME desktop and its applications, '",
     "SPEECH OUTPUT: 'OpenOffice'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ', Firefox, and the Java platform. Some applications work better than others, however, and the Orca community continually works to provide compelling access to more and more applications.'",
     "SPEECH OUTPUT: 'On the '",
     "SPEECH OUTPUT: 'Accessible Applications page'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ', you will find a growing list of information regarding various applications that can be accessed with Orca as well as tips and tricks for using them. The list is not to be a conclusive list of all applications. Rather, the goal is to provide a repository within which users can share experiences regarding applications they have tested.'",
     "SPEECH OUTPUT: 'See also the '",
     "SPEECH OUTPUT: 'Application Specific Settings'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' page for how to configure settings specific to an application.'",
     "SPEECH OUTPUT: 'Please also refer to the '",
     "SPEECH OUTPUT: 'Accessible Applications page'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for detailed information.'",
     "SPEECH OUTPUT: 'How Can I Help?'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: 'There's a bunch you can do! Please refer to the '",
     "SPEECH OUTPUT: 'How Can I Help page'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ' for detailed information.'",
     "SPEECH OUTPUT: 'More Information'",
     "SPEECH OUTPUT: 'heading level 1'",
     "SPEECH OUTPUT: '• Frequently Asked Questions: '",
     "SPEECH OUTPUT: 'FAQ'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '• Mailing list: orca-list image link'",
     "SPEECH OUTPUT: 'orca-list@gnome.org'",
     "SPEECH OUTPUT: ' ( orca-list image link'",
     "SPEECH OUTPUT: 'Archives'",
     "SPEECH OUTPUT: ')'",
     "SPEECH OUTPUT: '• Bug database: bugzilla.gnome.org image link'",
     "SPEECH OUTPUT: 'GNOME Bug Tracking System (Bugzilla)'",
     "SPEECH OUTPUT: ' ( buglist image link'",
     "SPEECH OUTPUT: 'current bug list'",
     "SPEECH OUTPUT: ')'",
     "SPEECH OUTPUT: '• Design documents: orca image link'",
     "SPEECH OUTPUT: 'Orca Documentation Series'",
     "SPEECH OUTPUT: '• www.diveintopython.org image link'",
     "SPEECH OUTPUT: 'Dive Into Python, Mark Pilgrim'",
     "SPEECH OUTPUT: '• 103-6779448-2183842 image link'",
     "SPEECH OUTPUT: 'Python in a Nutshell, Alex Martelli'",
     "SPEECH OUTPUT: '• 103-6779448-2183842 image link'",
     "SPEECH OUTPUT: 'Python Pocket Reference, Mark Lutz'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'The information on this page and the other Orca-related pages on this site are distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.'",
     "SPEECH OUTPUT: 'separator'",
     "SPEECH OUTPUT: 'CategoryAccessibility'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Orca (last edited 2007-12-07 22:09:22 by '",
     "SPEECH OUTPUT: 'WillieWalker'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: ')'",
     "SPEECH OUTPUT: 'User'",
     "SPEECH OUTPUT: 'heading level 3'",
     "SPEECH OUTPUT: 'Login'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Page'",
     "SPEECH OUTPUT: 'heading level 3'",
     "SPEECH OUTPUT: 'Immutable Page'",
     "SPEECH OUTPUT: 'Info'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'Attachments'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: 'More Actions: combo box'",
     "SPEECH OUTPUT: 'GNOME World Wide'",
     "SPEECH OUTPUT: 'heading level 3'",
     "SPEECH OUTPUT: 'GnomeWorldWide image link'",
     "SPEECH OUTPUT: 'Copyright \xa9 2005, 2006, 2007 '",
     "SPEECH OUTPUT: 'The GNOME Project'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '.",
     "Hosted by '",
     "SPEECH OUTPUT: 'Red Hat'",
     "SPEECH OUTPUT: 'link'",
     "SPEECH OUTPUT: '.'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
