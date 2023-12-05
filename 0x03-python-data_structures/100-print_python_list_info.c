#include <Python.h>

/**
 * print_python_list_info -  function that prints info
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	Pyobject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] size of the python list = %d\n", size);
	pritnf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("", Py_TYPE(obj)->tp_name);
	}
}
