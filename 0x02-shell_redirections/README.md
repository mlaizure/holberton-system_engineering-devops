0 - echo writes the input "Hello, World" with a new line appended
1 - echo can display the confused smiley with backslash escapes for bash special characters
2 - cat displays file contents
3 - cat with 2 operands can be used again to display 2 files' contents
4 - tail displays a file's last 10 lines
5 - head displays a file's first 10 lines
6 - pipe head into tail to display a certain line
7 - echo contents into file and use single quotes and/or backslashes to esacpe all the bash characters in the file name
8 - saves ls -la output to a file with >
9 - uses >> to append output of tail -n 1 ./iacta to the end of itself
10 - find . -name "*.js"  -type f  -delete can be used to delete files with a .js extension
11 - pipe find . -mindepth 1 -type d into wc -l to count number of directories and sub-directories in the current directory
12 - ls -At | head displays the 10 newest files in the current directory
13 - sort | uniq -u prints only words that appear exactly once
14 - grep displays lines containing "root" in the /etc/passwd file
15 - grep -c displays the number of lines that contain "bin" in /etc/passwd
16 - grep -A 3 displays lines containing the pattern "root" and 3 lines after them
17 - grep -v displays all the lines in a file that don't contain a pattern
18 - grep ^[[:alpha:]] displays all lines of a file starting with a letter
19 - tr A Z | tr c e replaces A with c and Z with e
20 - tr -d Cc deletes the cs in Chicago
21 - rev reverses input
22 - cut -d : cuts based on colons and the -f 1,6 option tells it which fields to display, then you use sort to sort based on users
23 - find ./ -empty -printf "%f\n" finds all the empty files and directories in the current directory and all sub-directories
24 - find . -name "*.gif" -type f -printf "%f\n" | rev | cut -c 5- | rev | LC_ALL=C sort -f lists files (type) that have .gif extensions (name) displays without extension (rev | cut | rev) and wihtout path (printf) and sorts by byte values but case-insensitive (LC_ALL=C sort -f)
25 - echo "$(cut -c 1 | tr -d "/n")" cuts the first letter off each line, trims the newlines in the output, and hten echo appends a newline to the end
26 - tail -n +2 | cut -f 1 | sort | uniq -c | sort -gr | head -11 | rev | cut -d -f 1 | rev ; tail strips off the header, cut deletes everything except the first column, sort sorts things together so uniq can number and squash them, sort again by number and in reverse so biggest at the top, head takes the top 11, rev cut rev to take the number back off

rev cut rev is so you can take the first field if there's not a clear delimeter (delimeter might occur inside parts of the input)

All of these files are executable bash shell scripts