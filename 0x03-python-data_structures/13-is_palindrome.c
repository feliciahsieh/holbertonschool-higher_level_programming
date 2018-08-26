#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks linked list if it's a palindrome
 * @head: pointer to head of linked list
 * Return: 0 if Not Palindrome
 *         1 if Palindrome (or empty list)
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int word[1000], i = 0;
	int left = 0, right = 0;

	word[0] = word[0];

	if (*head == NULL)
		return (1);

	current = *head;
	while (current)
	{
		word[i] = current->n;
		current = current->next;
		i++;
	}
	if (i == 1)
		return (1);

	if ((i % 2) == 0)
	{
		left = i / 2 - 1;
		right = i / 2;
	} else
	{
		left = i / 2 - 1;
		right = i / 2 + 1;
	}

	while (left != 0)
	{
		if (word[left] != word[right])
			return (0);
		left--;
		right++;
	}

	return (1);
}
