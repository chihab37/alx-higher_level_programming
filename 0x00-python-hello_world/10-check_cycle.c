#include "lists.h"
/**
  *check_cycle - checks if a singly linked list contains a cycle
  *@list: pointer to the head of the list
  *Return: 1 if a cycle is found, 0 otherwise
  */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
