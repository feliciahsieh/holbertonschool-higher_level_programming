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


	itemCheck = itemCheck;
	temp = temp;

	if (list == NULL)
		return (0); /*no list item*/

	if (list->next == NULL)
		return (0); /*list of one item*/

	if (list == list->next)
		return (1); /*list of one item pointing to itself*/

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
		/*reset next item*/
		if (temp == NULL) /*new temp*/
			itemCheck = NULL;
	}

	return (0);
}
