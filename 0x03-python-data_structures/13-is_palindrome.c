#include "lists.h"
/**
 * is_palindrome - checks if palindrome exists
 *
 * @head: a pointer to the list
 * Return: return 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	int length = 0;
	listint_t *ptr = *head;
	int i;
	int k;

	if (!head || !(*head))
		return (1);

	while (ptr)
	{
		length++;
		ptr = ptr->next;
	}

	int array[length];

	for (i = 0, ptr = *head; i < length; i++, ptr = ptr->next)
		array[i] = ptr->n;

	for (i = 0, k = length - 1; i < k; i++, k--)
	{
		if (array[i] != array[k])
			return (0);
	}
	return (1);
}
