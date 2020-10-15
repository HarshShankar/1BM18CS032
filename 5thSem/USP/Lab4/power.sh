# Write a Shell script to find the POWER OF A NUMBER using loop construct.

echo "Enter the number and its power"
read a b
res=1
while [ $b -ne 0 ]
do 
    res=$((res*a))
    b=$((b-1))
done 

echo $res