#include "lists.h"

/**
 * is_palindrome - checks linked list if it is a palindrome
 * @head: pointer to head of linked list
 * Return: 0 if Not Palindrome
 *         1 if Palindrome (or empty list)
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int word[1000], i = 0;
	int left = 0, right = 0;

	if ((head == NULL) || (*head == NULL) || ((*head)->next == NULL))
		return (1);
	current = *head;
	while (current)
	{
		word[i] = current->n;
		current = current->next;
		i++;
	}
	left = i / 2 - 1;
	if ((i % 2) == 0)
		right = i / 2;
	else
		right = i / 2 + 1;
	while (left != 0)
	{
		if (word[left] != word[right])
			return (0);
		left--;
		right++;
	}
	return (1);
}
