echo "Enter the file source"
read f1 f2
echo "Enter the destination file"
read f3
rm -rf $f3
echo "$f1 contents: " >>f3
head -5 $f1 >>$f3
echo "$f2 contents: ">>f3
head -15 $f2| tail -8 >>$f3
echo "Successfully appended the lines to $f3"