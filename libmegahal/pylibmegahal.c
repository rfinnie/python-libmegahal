/*
 * Copyright (C) 2013 Ryan Finnie
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 */

#include <Python.h>
#include "megahal.h"

static PyObject * wrap_megahal_initialize(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_cleanup(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_setnobanner(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_setnowrap(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_setnoprompt(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_initial_greeting(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_learn(PyObject * s, PyObject * args);
static PyObject * wrap_megahal_do_reply(PyObject * s, PyObject * args);

static PyMethodDef megahalMethods[] = {
    { "megahal_initialize", (PyCFunction) wrap_megahal_initialize, METH_VARARGS, NULL },
    { "megahal_cleanup", (PyCFunction) wrap_megahal_cleanup, METH_VARARGS, NULL },
    { "megahal_setnobanner", (PyCFunction) wrap_megahal_setnobanner, METH_VARARGS, NULL },
    { "megahal_setnowrap", (PyCFunction) wrap_megahal_setnowrap, METH_VARARGS, NULL },
    { "megahal_setnoprompt", (PyCFunction) wrap_megahal_setnoprompt, METH_VARARGS, NULL },
    { "megahal_initial_greeting", (PyCFunction) wrap_megahal_initial_greeting, METH_VARARGS, NULL },
    { "megahal_learn", (PyCFunction) wrap_megahal_learn, METH_VARARGS, NULL },
    { "megahal_do_reply", (PyCFunction) wrap_megahal_do_reply, METH_VARARGS, NULL },
    { NULL }
} ;

static PyObject * wrap_megahal_initialize(PyObject * s, PyObject * args) {
    megahal_initialize();
    return Py_BuildValue("s", NULL);
}
static PyObject * wrap_megahal_cleanup(PyObject * s, PyObject * args) {
    megahal_cleanup();
    return Py_BuildValue("s", NULL);
}
static PyObject * wrap_megahal_setnobanner(PyObject * s, PyObject * args) {
    megahal_setnobanner();
    return Py_BuildValue("s", NULL);
}
static PyObject * wrap_megahal_setnowrap(PyObject * s, PyObject * args) {
    megahal_setnowrap();
    return Py_BuildValue("s", NULL);
}
static PyObject * wrap_megahal_setnoprompt(PyObject * s, PyObject * args) {
    megahal_setnoprompt();
    return Py_BuildValue("s", NULL);
}

static PyObject * wrap_megahal_initial_greeting(PyObject * s, PyObject * args) {
    char *ret;

    ret = megahal_initial_greeting();
    return Py_BuildValue("s", ret);
}

static PyObject * wrap_megahal_learn(PyObject * s, PyObject * args) {
    char *input;
    int log;

    if (!PyArg_ParseTuple(args, "si", &input, &log))
        return NULL;

    megahal_learn(input, log);
    return Py_BuildValue("s", NULL);
}

static PyObject * wrap_megahal_do_reply(PyObject * s, PyObject * args) {
    char *ret;
    char *input;
    int log;

    if (!PyArg_ParseTuple(args, "si", &input, &log))
        return NULL;

    ret = megahal_do_reply(input, log);
    return Py_BuildValue("s", ret);
}

void initpylibmegahal(void) {
    (void)Py_InitModule("pylibmegahal", megahalMethods);
}
