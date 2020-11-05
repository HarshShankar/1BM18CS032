#Program to check if the character is a vowel or character

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