#! /bin/bash

#Write a shell Program to accept a filename from the User and display the attributes,
#contents and word count of the file Perform copy,rename  operation by accepting two filenames from the user

echo "Enter the filename :\c"
read filename
echo "attributes of the file are: \n"
ls -l $filename
echo "contents of the file are: \n"
cat $filename
echo "word count of the file is: \n"
 wc -w $filename

