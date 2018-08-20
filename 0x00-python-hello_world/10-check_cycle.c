#include "lists.h"

/**
 * check_cycle - check for loop in a linked list
 * @list: pointer to linked list
 * Return: 0 if no loop
 *         1 if loop exists
 */
int check_cycle(listint_t *list)
{
	const listint_t *tortoise = NULL, *hare = NULL;


	if (list == NULL)
		return (0);

	tortoise = list;
	hare = list;

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
