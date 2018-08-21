#include <stdlib.h>
#include "lists.h"


/**
 * insert_node - insert node in singly linked list
 * @head: pointer to head of linked list
 * @number: integer
 * Return: address if inserted successfully or
 *         NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new = NULL, *prev = NULL;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if(*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
		{
			if (current->n < number)
			{
				prev = current;
				current=current->next;
			}
			else
				break;
		}

		if (current->next == NULL)
		{
			current->next = new;
		} else
		{
			prev->next = new;
			new->next = current;
		}
	}

	return(NULL);
}
