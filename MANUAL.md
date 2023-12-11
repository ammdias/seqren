SEQUENTIAL FILE RENAMER
=======================

This is a small Python script to rename files in a numerical sequence.

Copyright (C) 2021 António Manuel Dias

contact: ammdias@gmail.com


CONTENTS
--------

* [Changes history]
* [INSTALLATION]
* [USAGE]
* [REFERENCE]
* [LICENSE]


INSTALLATION
------------

The instructions below are for installation on a modern Linux system.  They
may work on other modern Unix-like systems like BSD derivatives, including
MacOS, but that has not been tested and may require some tweaking.  Try it at
your own risk.  For MS Windows installation, the user will have to do some
tweaking.

1. Download and unzip the program's compressed file in a directory of your
   choosing.

2. Open a terminal in the directory where the program was uncompressed and run
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

3. Test that the installation was successful with the command:

       $ seqren --help

   (this should print the program's simple help page)


USAGE
-----

This utility is to be used from the command line (terminal), as any other shell
command.  The basic usage is:

    $ seqren [file [file ...]

which will rename the file(s) passed as arguments to a numerical sequence,
preserving their extensions.  It's also possible to change the final name (and
extension) of the renamed files using one or more of the optional arguments,
like preserving the file's original names, in addition to the sequence number,
inserting text before of after the number or changing the file's extensions.

The files could be passed explicitly or by globbing using the usual shell
wildcards, like:

    $ seqren *.jpg
    $ seqren IMG-202102??-*.jpg

The sequence will usually start at the number 1, with no leading zeroes, but
this behaviour may be altered with the `--start` and `--leading_zeroes`
options.  It is also possible to move the files while renaming them and to
keep the original files.

You may combine several options.  Check the [REFERENCE] section for the
explanation of the full capabilities of the utility.

### Examples of Usage

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


REFERENCE
---------

### Options to change the sequence number

* `-s <number>`, `--start <number>`: change the starting number of the sequence.
  The sequence will start at the number passed as argument and increase by 1 at
  each renamed file (reverse sequencing or other step increases is not
  possible). Example:

      $ seqren -s 10 *.jpg

  will rename all files with `.jpg` extension in the current directory,
  starting at number 10: `10.jpg`, `11.jpg`, etc.

* `-z <number>`, `--leading_zeroes <number>`: format the sequence number to a
  fixed width, adding the necessary leading zeroes.

      $ seqren -z 3 *.jpg

  will rename all files with `.jpg` extension in the current directory with
  three-digit numbers with leading zeroes: `001.jpg`, `002.jpg`, etc.

### Options to insert other text besides the sequence number

* `-t <text>`, `--text_after <text>`: insert the text passed as argument after
  the sequence number.

      $ seqren -t '-Rome' *.jpg

  will rename all `.jpg` files in the current directory, inserting the text
  `-Rome` after the number: `1-Rome.jpg`, `2-Rome.jpg`, etc.

* `-T <text>`, `--text_before <text>`: insert the text passed as argument
  before the sequence number.

      $ seqren -T 'Rome-' *.jpg

  will rename all `.jpg` files in the current directory, inserting the text
  `-Rome` before the number: `Rome-1.jpg`, `Rome-2.jpg`, etc.

* `-i`, `--include_name_after`: insert the original file name after the
  sequence number.

      $ seqren -i -t '-' MammaMia.mp3 NovemberRain.mp3

  will rename the files passed as argument, inserting their original name after
  the sequence number (also note the dash inserted by option `-t`):
  `1-MammaMia.mp3`, `2-NovemberRain.mp3`

* `-I`, `--include_name_before`: insert the original file name before the
  sequence number.

      $ seqren -I -T '-' MammaMia.mp3 NovemberRain.mp3

  will rename the files passed as argument, inserting their original name
  before the sequence number (also note the dash inserted by option `-T`):
  `MammaMia-1.mp3`, `NovemberRain-2.mp3`

### Options to change the default renaming behaviour of the program

* `-e <extension>`, `--extension <extension>`: change extension of renamed
  files to the passed argument.

      $ seqren -e .jpeg *.jpg *.JPG

  will rename all files with extensions `.jpg` and `.JPG`, change their
  extension to `.jpeg`: `1.jpeg`, `2.jpeg`, etc.

* `-k`, `--keep`: will keep the original files, making new renamed copies of
  them.

* `-d <directory>`, `--destination_directory <directory>`: will move (or copy,
  if the `-k` option was added) the renamed files to the directory passed as
  argument.

* `-n`, `--no_act`: will print the actions that would be performed by the
  program instead of actually executing them.  This is extremely useful to
  check the changes that will be made by all the options before submitting
  them.

### Miscellaneous options

* `-h`, `--help`: display the program's help page

* `--version`: display the program's name and version.

* `--copyright`: display the program's copyright information.

* `--manual`: display the user's manual in a web browser window.

* `--uninstall`: uninstall the program.


LICENSE
-------

Copyright (C) 2021 António Manuel Dias

contact: ammdias@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the [GNU General Public
License](http://www.gnu.org/licenses) along with this program.  If not,
please check the site above.


