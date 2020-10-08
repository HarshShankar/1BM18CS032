#! /bin/sh

#Write an Interactive Shell program to check whether a  number is zero,positive or Negative

echo "Enter a number"
read a

if test $a -gt 0
then 
    echo "Positive number"
elif test $a -lt 0
then 
    echo "Negative number" 
else
    echo "Zero"
fi 