echo "Enter arithmetic operation: "
read x op y

case $op in
    "+") res=`expr $x + $y`
    ;;
    "-") res=`expr $x - $y`
    ;;
    "*") res=`expr $x \* $y`
    ;;
    "/") res=`expr $x / $y`
    ;;
    "%") res=`expr $x % $y`
    ;;
    *) echo "Invalid operator."
    exit 1
    ;;
esac

echo "$x $op $y = $res"