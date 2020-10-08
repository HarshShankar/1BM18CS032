#! /bin/bash

#Write a shell program to perform the basic Airthmetic Operations using expr command Addition,Subtraction,Multiplication and Division

echo "Enter values of a and b"
read a b 
sum=`expr $a + $b`
sub=`expr $a - $b`
mul=`expr $a \* $b`
div=`expr $a / $b`
echo "Sum= $sum"
echo "Subtraction= $sub"
echo "Multiply= $mul"
echo "Division= $div"