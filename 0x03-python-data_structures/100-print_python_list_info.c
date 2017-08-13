#include "Python.h"

/**
 * printElement - print element info
 * @p: python object
 * @n: number of items in object
 * Return: none
 */
void printElement(PyObject *p, int num)
{
	char *pyTypes[5] = { "str", "int", "float", "tuple", "list" };
	int i;
        PyObject *item = NULL;

	pyTypes[0] = pyTypes[0];
	item = item;

	if (num > 0)
	{
		for (i = 0; i < num; i++)
		{
/*			printf("Element %d: %s\n", i, pyTypes[i]);*/

			item = PyList_GetItem(p, i);
/*			PyObject_Print(item, stdout, i);*/
/*			PyObject_Print(type(item), stdout, i);*/
			printf("\n");
		}
	}
	printf("\n");
}

/**
 * print_python_list_info - Create a C function that prints some
 * basic info about Python lists
 * @p: python object
 * Return: none
 */
void print_python_list_info(PyObject *p)
{
	int number = 0, numAllocated = 0;

	if (!p)
		return;

	number = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", number);

	numAllocated = ((PyListObject*)p)->allocated;
	printf("[*] Allocated = %d\n",numAllocated);
	printElement(p, number);
}
