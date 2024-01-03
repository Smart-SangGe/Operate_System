#include <signal.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
void signal_handler(int sig)
{
    switch (sig)
    {
    case SIGINT:
        printf("\nGroup 10, Get a signal:SIGINT. You pressed ctrl+c.\n");
        break;
    case SIGQUIT:
        printf("\nGroup 10, Get a signal:SIGQUIT. You pressed ctrl+\\.\n");
        break;
    case SIGTSTP:
        printf("\nGroup 10, Get a signal:SIGTSTP. You pressed ctrl+z.\n");
        break;
    }
    exit(0);
}
int main()
{
    printf("Group 10, Current process ID is %d\n", getpid());
    signal(SIGINT, signal_handler);
    signal(SIGQUIT, signal_handler);
    signal(SIGTSTP, signal_handler);
    for (;;)
        ;
}
