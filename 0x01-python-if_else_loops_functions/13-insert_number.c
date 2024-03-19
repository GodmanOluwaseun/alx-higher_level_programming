#include "lists.h"

/**
 * insert_node - Function in C that inserts a number into
 * a sorted singly linked list.
 * @head: Pointer to head node.
 * @number: Number to insert.
 * Return: Pointer to new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node_ptr, *current;

	new_node_ptr = malloc(sizeof(listint_t));

	if (new_node_ptr == NULL)
	{
		return (NULL);
	}

	new_node_ptr->n = number;

	if (*head == NULL)
	{
		*head = new_node_ptr;
		new_node_ptr->next = NULL;
		return (new_node_ptr);
	}

	current = *head;

	while (current->next != NULL && current->next->n <= number)
	{
		current = current->next;
	}

	new_node_ptr->next = current->next;
	current->next = new_node_ptr;

	return (new_node_ptr);
}
