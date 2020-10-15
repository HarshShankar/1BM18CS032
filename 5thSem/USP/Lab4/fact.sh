#Shell script to  find the FACTORIAL OF A NUMBER using Looping construct

echo "Enter a number: \c"
read num
f=$num
fact=1

while [ $num -gt 1 ]
do 
    fact=$(($fact * num))
    num=$((num - 1))
done

echo "The factorial of $f is $fact"