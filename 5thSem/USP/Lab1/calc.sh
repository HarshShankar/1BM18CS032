#!/bin/sh

# Program to perform calculator operations
echo "Enter two numbers"
read a
read b
sum=$(($a+$b))
sub=$(($a-$b))
mul=$(($a*$b))
div=$(($a/$b))
rem=$(($a%$b))
echo $sum
echo $sub
echo $mul
echo $div
echo $rem
