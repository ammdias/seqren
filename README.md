Sequential file renamer
=======================

Renames files in a numerical sequence.
(C) 2021 António Manuel Dias

Version 0.5 -- 2023-12-10

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


Installation
------------

The following instructions describe the installation process for basic usage
in a Linux environment.

1. Open a terminal in the directory where the program was uncompressed and run
   the installation script with Python 3:

       $ python3 INSTALL.py

   You will be prompted for the installation directory --- i.e. the directory
   under which the folder containing all the application files will be placed
   --- and for the start link directory --- i.e. the directory where the
   symbolic link for the program will be created.

   The default directories will install the program for the current user only
   and are suited for single-user systems.  If you want to keep these
   settings, just press ENTER when prompted.  The program will be installed in
   the directory `$HOME/.local/lib/seqren` and the symbolic link
   `$HOME/.local/bin/seqren` will be created.  On most Linux systems the
   `$HOME/.local/bin` directory will be inserted in the execution PATH, if it
   exists. If it doesn't, you will have to add it manually.

   If a previous installation exists on the selected directory, you will be
   asked if you want to overwrite it.  Answer "`yes`" (or just "`y`") if that
   is the case or "`no`" ("`n`") if not.

2. Test that the installation was successful with the command:

       $ seqren --help

   (you should be presented with the program's help page)

3. Read the MANUAL.  You can open it in a web browser with the command:

       $ seqren --manual

4. To uninstall the program use the command:

       $ seqren -uninstall


Examples of Usage
-----------------

1. Rename files `example.txt` and `test.txt` to `1.txt` and `2.txt`:

       $ seqren example.txt test.txt

2. Rename all files with extension `.jpg` in the current directory
   in a sequence (`1.jpg`, `2.jpg` ...)

       $ seqren *.jpg

3. Rename all files with extension `.jpg` in the current directory
   in a sequence starting in number 0 (`0.jpg`, `1.jpg`, ...)

       $ seqren *.jpg -s 0

4. Rename all files with extension `.jpg` in the current directory
   in a sequence, with 2 digit numbers with leading zeroes
   (`01.jpg`, `02.jpg`, ...)

       $ seqren *.jpg -z 2

5. Rename all files with extension .jpg in the current directory
   in a sequence, with 2 digit numbers and starting with the text
   "Day At The Beach-" (`Day At The Beach-01.jpg`,
   `Day At The Beach-02.jpg`, ...)

       $ seqren *.jpg -z 2 -T "Day At The Beach-"

6. Same as previous example but changing extension to `.jpeg`
   (`Day At The Beach-01.jpeg`, `Day At The Beach-02.jpeg`, ...)

       $ seqren *.jpg -z 2 -T "Day At The Beach-" -e .jpeg

7. Rename all files with extension `.mp3` in a sequence, keeping
   the original name after the number separated by a space
   (`1 House of the Rising Sun.mp3`, `2 Scarborough Fair.mp3`, ...):

       $ seqren *.mp3 -i -t " "

8. Same as previous example but moving the files to the directory
   "Folk Music" (`Folk Music/1 House of the Rising Sun.mp3`,
   `Folk Music/2 Scarborough Fair.mp3`, ...):

       $ seqren *.mp3 -i -t " " -d "Folk Music"

9. Add option `-k` to keep the original files:

       $ seqren *.mp3 -k -i -t " " -d "Folk Music"

10. Option `-n` only shows the operations to execute, without actually
    renaming the files. Example:

       $ seqren *.mp3 -n -k -i -t " " -d "Folk Music"

   would output:

       cp House of the Rising Sun.mp3 Folk Music/1 House of the Rising Sun.mp3
       cp Scarborough Fair.mp3 Folk Music/2 Scarborough Fair.mp3
