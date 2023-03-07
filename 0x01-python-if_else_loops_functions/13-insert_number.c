#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current_node;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    /* Initialize the new node */
    new_node->n = number;
    new_node->next = NULL;

    /* Handle the case when the list is empty or the new node should be the new head */
    if (*head == NULL || number < (*head)->n)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Traverse the list and find the node after which the new node should be inserted */
    current_node = *head;
    while (current_node->next != NULL && current_node->next->n <= number)
        current_node = current_node->next;

    /* Insert the new node */
    new_node->next = current_node->next;
    current_node->next = new_node;

    return (new_node);
}

