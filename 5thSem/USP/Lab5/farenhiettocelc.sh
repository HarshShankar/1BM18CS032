# Write a Shell Script to convert the Temperatures FAHERENHEIT to celsius (f -32) *5 /9 

echo "Enter the temperature in Farenhiet \c"
read f
if [ $f -ge 32 ] && [ $f -le 212 ] 
then
    f=`expr $f - 32`
    f=`expr $f \* 5`
    f=`expr $f / 9`
    echo "Temperature in Celcius= $f"
else
    echo "Enter a valid temperature between 32 and 212"
fi
