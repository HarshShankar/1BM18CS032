# Write a Shell Script to find Fibonacci Series Upto N using While Construct

echo "Enter the value of N: \c"
read n
if [ $n -le 0 ]
then 
    echo "Enter a number greater than 0"
elif [ $n -eq 1 ]
then 
    echo "The series: 0"
else 
    i=0
    j=1
    echo "The series: $i $j\c"
    while test $n -ge 3 
    do 
        sum=$((i+j)) 
        echo " $sum\c"
        i=$j
        j=$sum
        n=$((n-1))
    done
fi 
echo "\n"