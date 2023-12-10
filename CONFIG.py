'''Configuration file for the seqren installation script.
'''

DOC = 'Installation script for seqren.'''
COPYRIGHT_YEAR = '2021'
VERSION = '0.5'
DATE = '2023-12-10'
AUTHOR = 'António Manuel Dias <ammdias@gmail.com>'
LICENSE = '''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


# List of file to be copied to installation the directory
FILES = ('seqren.py', 'UNINSTALL.py', 'MANUAL.md', 'MANUAL.html',
         '__version__', 'LICENSE.md', 'README.md', 'CHANGES.md')

# List of directories to be copied to the installation directory
TREES = ()

# Name of the icon file
ICO_FILE = None

# Name of the desktop entry file (for GUI menus)
DESKTOP_FILE = None

# Files to make executable
EXECS = ('seqren.py',)

# Name of the application (will be the name of the installation directory)
APP_NAME = 'seqren'

# Symbolic links to make: dictionary of 'link name': 'executable name' pairs
LINKS = {'seqren': 'seqren.py'}

# List of configuration files
CONFIG_FILES = ()
