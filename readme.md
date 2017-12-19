# About this python script
This script implement a function to display who have not yet submit the homework by comparing a given set of names and filenames form a given dir. So there must be sutdents' names at the files in that dir. 

# Usage
Firstly, make sure your python version is >= 3.4. (Have not yet tested on lower version environment)
Then run on terminal like:
```shell
python main.py
```
You can set up the names:
1. at line 46 in `main.py`, which is commented with `MARK:`
2. at file `name_set_with_blank_to_separate` with blank
> If you leave the `name_set_with_blank_to_separate` file existed, students' names in `main.py` will be covered by names in file even though the file is empty. If you want to use names in `main.py`, you could just delete the file `name_set_with_blank_to_separate` or change its name. After that when you run the script, there will be a `WARNING` appeared in you terminal. So my suggestion is to always use names in file, which is a more flexible way. 

# Notice
The file `name_set_with_blank_to_separate` must be encoded by UTF8
> If you want a executable binary, which is not recommended, get gcc installed and set up environment variable of `$C_INCLUDE_PATH` and `$PYTHON_LIB` and then run `./build.sh`. 

# Known bugs
1. Cannot follow soft link
2. Sometimes it will raise `NotADirectoryError` after I change to python3.6 on macOS. (The script is written on python3.4)

Because this script is currently for personal use, there must be a number of bugs in it, so feel free to submit issues. 

