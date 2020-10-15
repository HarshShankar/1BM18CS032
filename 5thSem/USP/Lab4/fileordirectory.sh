#Write shell scripts accept a file as a command line argument and 
#display whether it is ordinary file or directory file and display their attributes.

if [ $# -ne 1 ]
then 
    echo "Enter the file/directory name"
else
    echo "Attributes:"
    if [ -f $1 ]
    then
        echo `ls -l $1`
    elif [ -d $1 ]
    then 
        echo `ls $1`
    fi 
fi

