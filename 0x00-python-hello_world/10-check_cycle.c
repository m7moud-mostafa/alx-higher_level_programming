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
	listint_t *slow_ptr = list;
	listint_t *fast_ptr = list;

	if (!list)
		return (0);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
		if (slow_ptr == fast_ptr)
			return (1);
	}
	return (0);
}
