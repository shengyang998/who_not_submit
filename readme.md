# About this python script
This script implement a function to display who have not yet submit the homework by comparing a given set of names and filenames form a given dir. So there must be sutdents' names at the files in that dir. 

# Usage
Firstly, make sure your python version is >= 3 (Have not yet tested on lower version environment).
Then run the following command in terminal:
```shell
python main.py
```
You can set up the names in two ways:
1. Add the names at file `name_set` with blank to separate
2. Add the names with ',' to separate at line 79 in `main.py`, which is commented with `MARK: `

# Notice
1. The file `name_set` should be encoded by UTF8
2. If the `name_set` file existed, even though the file is empty, the students' names hard coded in `main.py` will be covered by names in file.

# Known problems
1. Cannot follow soft link
2. If there is blank in you path or dir name, the program will raise a 'NotADirectoryError'. So make sure that there is no blank in you path.

Because this script is currently for personal use, there must be a number of bugs in it, so feel free to submit issues. 

