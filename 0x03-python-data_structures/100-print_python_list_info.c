#include "Python.h"

/**
 * print_python_element - print element info
 * @p: python object
 * Return: none
 */
void print_python_element(PyObject *p)
{
	char *pyTypes[5] = { "str", "int", "float", "tuple", "list" };
	int i, num;

	p =p;

	num = 3; /*FIX*/
	for (i = 0; i < num; i++)
		printf("Element %d: %s\n", i, pyTypes[i]);
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
	int i;
	PyListObject *pp;

	if (!p)
		return;

	number = (int)PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", number);
	numAllocated = ((PyListObject*)p)->allocated;
	printf("[*] Allocated = %d\n",numAllocated);

	if (number > 0)
	{
		for (i = 0; i < number; i++)
		{
			PyObject *item = PyList_GetItem(p, i);
			PyObject_Print(item, stdout, i);
			pp=pp;
		}
	}
}
