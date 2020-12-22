// * Write a C Program to create a new process using Fork operation.
// * Print the Process ID of the child and its parent in the child process,
// * and print the process Id of parent, child Pid and parent’s parent process Id in Parent.
// * Make the parent to sleep for 3 seconds.

#include <stdio.h>
#include <unistd.h>

int main() {
    int fork_j;
    fork_j = fork();
    if (fork_j == 0) {
        printf("This is child process. Child PID : %d\n", getpid());
        printf("Child's parent's PID : %d\n", getppid());
    } else {
        sleep(3);
        printf("This is parent process. Parent PID : %d\n", getpid());
        printf("Parent's parent's PID : %d\n", getppid());
        printf("Return value of fork to parent is child's PID: %d\n", fork_j);
    }
    return 0;
}