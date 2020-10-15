#Shell script to  find the SUM OF EVEN NUMBERS UPTO N using Looping construct.

echo "Enter the value of N: \c"
read n 

sum=0
i=0

while [ $i -le $n ]
do
    sum=$((sum+i))
    i=$((i+2))
done 

echo $sum