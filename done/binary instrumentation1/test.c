#include <stdio.h>
#include <unistd.h>

void say_hello()
{
    printf("Hi!\n");
    fflush(stdout);
}

void say_goodbye()
{
    printf("Goodbye!\n");
    fflush(stdout);
}

int main()
{
    say_hello();
    sleep(6000);
    say_goodbye();
    return 0;
}
