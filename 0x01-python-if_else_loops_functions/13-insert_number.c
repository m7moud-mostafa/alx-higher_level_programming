#include "lists.h"
#include <limits.h>

/**
 * insert_node - inserts a node in sorted list
 *
 * @head: head of the list
 * @number: number to be inserted
 * Return: a pointer to the new node or the NULL when failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h;
	listint_t *ptr;
	listint_t *tmp;
	int next_n;

	h = malloc(sizeof(listint_t));
	if (!h)
		return (NULL);

	h->n = number;
	if (!head || !(*head))
	{
		*head = h;
		(*head)->next = NULL;
		return (h);
	}
	ptr = *head;
	if (ptr->n > number)
	{
		h->next = ptr;
		*head = h;
		return (h);
	}

	for (; ptr; ptr = ptr->next)
	{
		if (ptr->next)
			next_n = (ptr->next)->n;
		else
			next_n = INT_MAX;

		if (ptr->n <= number && number <= next_n)
		{
			tmp = ptr->next;
			ptr->next = h;
			h->next = tmp;
			return (h);
		}
	}
	return (NULL);
}
