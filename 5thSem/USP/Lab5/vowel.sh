#Program to perform arithmetic operations on a set of two numbers using case expression

#!/bin/bash
echo "Enter character: "
read char

case $char in
[aeiouAEIOU])
    echo "Character is a vowel"
    ;;
*)
    echo "Character is a consonant"
    ;;
esac