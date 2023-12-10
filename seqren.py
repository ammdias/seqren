#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""Sequencial file renamer

Renames files in a numerical sequence.
(C) 2021 António Manuel Dias

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""

__version__ = '0.5'
__date__ = '2023-12-10'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import sys
import shutil
import os.path
import argparse
import webbrowser


#------------------------------------------------------------------------------

def run(action, args):
    """Rename all the files, if they exist.
    """
    if not args.file:
        print("No files to rename.")
        return

    for i, f in enumerate(args.file, start=args.start):
        if not os.path.exists(f):
            print("Error: {} not found.".format(f))
            continue

        number = "{}{:0{ld}d}{}".format(args.text_before, i, args.text_after,
                                        ld=args.leading_zeroes)

        directory, filename = os.path.split(f)
        filename, extension = os.path.splitext(filename)

        if args.include_name_before:
            filename = filename + number
        elif args.include_name_after:
            filename = number + filename
        else:
            filename = number

        action(f, os.path.join(args.destination_directory or directory,
                               filename + (args.extension or extension)))


#------------------------------------------------------------------------------
# parse command line arguments
parser = \
 argparse.ArgumentParser()

parser.add_argument("file", type=str, nargs='*',
                    help="file(s) to be renamed.")

parser.add_argument("-s", "--start", type=int, default=1,
                    help="start number for the sequence (default 1).")

parser.add_argument("-z", "--leading_zeroes", type=int, default=0,
                    help="add leading zeroes to sequence number up to"\
                         " given number of digits.")

parser.add_argument("-t", "--text_after", type=str, default="",
                    help="text after the sequence number.")

parser.add_argument("-T", "--text_before", type=str, default="",
                    help="text before the sequence number.")

parser.add_argument("-i", "--include_name_after", action="store_true", 
                    help="include file name after the sequence number.")

parser.add_argument("-I", "--include_name_before", action="store_true", 
                    help="include file name before the sequence number.")

parser.add_argument("-e", "--extension", type=str,
                    help="extension for renamed files.")

parser.add_argument("-k", "--keep", action="store_true",
                    help="copy instead of move, keeping original files.")

parser.add_argument("-d", "--destination_directory", type=str,
                    help="destination directory for renamed files.")

parser.add_argument("-n", "--no_act", action="store_true",
                    help="show what files to rename, "
                         "without actually performing the action.")

parser.add_argument("--version", action="store_true",
                    help="show program's version.")

parser.add_argument("--copyright", action="store_true",
                    help="show the program's copyright information.")

parser.add_argument("--manual", action="store_true",
                    help="display the user's manual in a web browser window.")

parser.add_argument("--uninstall", action="store_true",
                    help="uninstall program.")


#------------------------------------------------------------------------------
# process options

args = parser.parse_args()

if args.uninstall:
    from UNINSTALL import uninstall
    uninstall()
elif args.version:
    try:
        appver = open(os.path.join(sys.path[0], '__version__')).read().strip()
    except:
        appver = __version__
    print("seqren", appver)
elif args.copyright:
    print(__doc__)
elif args.manual:
    webbrowser.open_new(os.path.join(sys.path[0], "MANUAL.html"))
else:
    if args.no_act:
        action = lambda s,d: print("cp" if args.keep else "mv", s, d)
    else:
        action = shutil.copy2 if args.keep else shutil.move
    run(action, args)

