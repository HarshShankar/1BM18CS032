echo "The home directories are:"
grep -v "nologin" /etc/passwd | cut -d ":" -f 6