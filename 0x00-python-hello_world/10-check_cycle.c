#include <stdio.h>
#include <unistd.h>
#include "lists.h"

/**
 * check_cycle - checks if the list contains a cycle
 * 
 * @list: the list
 * Return: 0 if there is no cycle
 *		   1 if contains cycle 
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (!list)
		return(-1);

	ptr = list;

	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		if (ptr == list)
			return (1);
	}
	return (0);
}
