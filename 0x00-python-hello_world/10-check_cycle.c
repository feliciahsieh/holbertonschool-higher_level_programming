#include "lists.h"

/**
 * check_cycle - check for loop in a linked list
 * @list: pointer to linked list
 * Return: 0 if no loop
 *         1 if loop exists
 */
int check_cycle(listint_t *list)
{
	const listint_t *temp = NULL, *itemCheck = NULL;


	if (list == NULL)
		return (0);
	if (list->next == NULL)
		return (0);
	if (list == list->next)
		return (1);
	temp = list;
	while (temp != NULL)
	{
		itemCheck = temp->next;
		while (itemCheck != NULL)
		{
			if (temp == itemCheck)
				return (1);
			itemCheck = itemCheck->next;
		}
		temp = temp->next;
		if (temp == NULL)
			itemCheck = NULL;
	}
	return (0);
}
