// * Write a C program to emulate the ls command using stat and lstat API functions.
// * Print File type, permission etc all the attributes.

#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    struct stat statbuf;
    // statbuf is from sys/stat.h
    if (lstat(argv[1], &statbuf) == -1) {
        printf("Couldn't stat file!\n");
        exit(0);
    }
    printf("File: \t%s\n", argv[1]);
    printf("UID : \t%d\n", statbuf.st_uid);
    printf((S_ISDIR(statbuf.st_mode)) ? "File is a directory\n" : "");
    printf("GID : \t%d\n", statbuf.st_gid);

    printf("Type and permission : %o\n", statbuf.st_mode);
    printf("No of links : %ld\n", statbuf.st_nlink);
    printf("Inode no : %ld\n", statbuf.st_ino);

    exit(0);
}