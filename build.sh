cd /Volumes/Ysy/计科卓越班/Helper/who_not_submit
cython main.py --embed
gcc -I$C_INCLUDE_PATH -L$PYTHON_LIB -lpython3.4m -o main main.c
