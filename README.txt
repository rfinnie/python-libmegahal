=======
MegaHAL
=======

MegaHAL is a computer conversation simulator, or "chatterbot", created
by Jason Hutchens.  This module provides an object-oriented Python
interface to libmegahal.

    import libmegahal
    mh = libmegahal.MegaHAL(path='/path/to/brain/directory')
    print mh.initial_greeting()
    mh.learn('Hello world!')
    print mh.do_reply('Hello.')
    my.cleanup()
