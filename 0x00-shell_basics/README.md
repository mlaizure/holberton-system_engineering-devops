0 - pwd prints the current working directory
1 - ls lists the contents of the current directory
2 - cd changes the working directory to the home directory
3 - ls -l shows files in long format
4 - ls -la includes hidden files in a long format
5 - ls -nla same as above but user and group IDs are numeric
6 - mkdir creates a directory
7 - mv moves files between directories
8 - rm deletes files
9 - rmdir deletes directories
10 - cd - changes working directory to previous one
11 - list can take multiple directories (list -la . .. /boot)
12 - file shows the file type
13 - ln -s makes a symbolic link
14 - cp -u *.html .. copies html files from current to parent directory but only files that didn't exist in the parent or were newer than parent versions
15 - mv [:upper:]* move all files beginning with an uppercase character
16 - rm *~ deletes all swap files
17 - mkdir -p creates a directory and any subdirectories specified (welcome/to/holberton)
18 - ls -lma is long form, comma separated, and shows hidden files
19 - holberton.mgc is a magic file that can be used with the file command to detect Holberton data tiles

(Files 0 - 18 are executable shell scripts.)