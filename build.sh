#!usr/bin/bash


## using clang compiler

exe_name='bs-blc'

#echo ${exe_name}.c  &&

set -xe
make 

#if [ $1 == '-Termux-run' ]; 
#then
    mv ${exe_name} ~/exes
    chmod +x ~/exes/${exe_name}
    ~/exes/${exe_name} $1;
#fi
