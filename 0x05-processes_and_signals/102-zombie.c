#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - creates 5 zombie processes
 *
 * Return: Nothing.
 */
int main(void)
{
	pid_t child;
	unsigned int i;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (!child)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(1);
		}
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - loop until forced to stop
 *
 * Return: None.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
