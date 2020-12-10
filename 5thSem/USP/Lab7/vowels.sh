# Program to count the number of vowels in a file using tr command
read -p "Enter file name: " fileName
tr -dc "aeiouAEIOU" < $fileName| wc -c