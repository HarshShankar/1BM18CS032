#Write a Shell program to accept two parameters perform File Test and display their attributes with suitable message if not display a suitable  message to pass right number of arguments.

if test $# -eq 0
then 
echo "Usage: sh $0 file file "
elif test $# -eq 2
then 
    if test -f $1
    then 
        ls -l  $1 || echo "$1 not found "
    fi 
    if test -f $2
    then 
        ls -l  $2 || echo "$2 not found "
    fi
else
    echo "You didn't enter two arguments"
fi


