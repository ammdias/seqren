#!/usr/bin/python3
#-*- coding: utf-8 -*-

"""Sequencial file renamer

Renames files in a numerical sequence.
(C) 2019 António Manuel Dias

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

__version__ = '0.3'
__date__ = '2019-09-01'
__license__ ='GNU General Public License version 3'
__author__ = 'António Manuel Dias <ammdias@gmail.com>'


import shutil
import os.path
import argparse

#------------------------------------------------------------------------------
# parse command line arguments
parser = \
 argparse.ArgumentParser(description="Renames files in a numerical sequence.",
                         epilog=
"""Sequencial file renamer (C) 2019 António Manuel Dias.
This program comes with ABSOLUTELY NO WARRANTY;
This is free software, and you are welcome to redistribute it under the
GNU General Public License version 3 or (at your option) any later version.
See https://www.gnu.org/licenses/ for the full license text.""")

parser.add_argument("file", type=str, nargs='+',
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
                    help="show what files to rename,"\
                         " without actually performing the action.")

args = parser.parse_args()

#------------------------------------------------------------------------------
# rename all the files, if they exist
if args.no_act:
    action = lambda s,d: print("cp" if args.keep else "mv", s, d)
else:
    action = shutil.copy2 if args.keep else shutil.move

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
