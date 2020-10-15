#! /bin/sh

# Write a shell program to find biggest of three Numbers using  read statement or positional parameter technique.
a=$1
b=$2
c=$3 

ans=$a

if test $b -gt $ans
then 
    ans=$b
fi 

if test $c -gt $ans
then 
    ans=$c
fi 

echo "$ans is the largest number amongst $a,$b and $c"