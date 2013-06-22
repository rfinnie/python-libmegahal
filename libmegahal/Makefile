PYVER  := $(shell python -c 'import sys; print sys.version[0:3]')
PYTHON = python$(PYVER)
PYTHONINCLUDE = /usr/include/$(PYTHON)

all: pylibmegahal.so

libmegahal.o: libmegahal.c
	$(CC) -c $(CPPFLAGS) $(CFLAGS) -o $@ -fPIC $<

pylibmegahal.o: pylibmegahal.c
	$(CC) -c $(CPPFLAGS) -I$(PYTHONINCLUDE) $(CFLAGS) -o $@ -fPIC $<

clean:
	$(RM) pylibmegahal.so *.o

pylibmegahal.so: libmegahal.o pylibmegahal.o
	$(CC) $(CPPFLAGS) $(CFLAGS) -shared libmegahal.o pylibmegahal.o $(LDFLAGS) -o pylibmegahal.so
