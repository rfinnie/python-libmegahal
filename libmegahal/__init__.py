#!/usr/bin/python

import pylibmegahal
import os


class MegaHAL:
    """ MegaHAL C library wrapper

    mh = MegaHAL(path='/path/to/brain/directory')
    print mh.initial_greeting()
    mh.learn('Hello world!')
    print mh.do_reply('Hello.')
    mh.cleanup()
    """
    initialized = False
    autosave = True
    data_path = None

    def __init__(self, path='.', autosave=True):
        """ MegaHAL initialization

        Keyword arguments:
        path -- Path to the MegaHAL brain
        """
        self.autosave = autosave

        if not (
            os.path.isfile(os.path.join(path, 'megahal.brn'))
            or os.path.isfile(os.path.join(path, 'megahal.trn'))
        ):
            raise OSError('%s: megahal.brn or megahal.trn not found' % path)

        self.data_path = os.path.abspath(path)
        old_path = os.getcwd()
        os.chdir(self.data_path)
        pylibmegahal.megahal_setnobanner()
        pylibmegahal.megahal_setnowrap()
        pylibmegahal.megahal_setnoprompt()
        pylibmegahal.megahal_initialize()
        os.chdir(old_path)
        self.initialized = True

    def __del__(self):
        """ Clean up after dereference

        Note that __del__ is not guaranteed to always trigger if an
        instance is deleted.  To be sure, call cleanup() yourself.
        """
        if self.initialized and self.autosave:
            self.cleanup()

    def cleanup(self):
        """ Save and clean up """
        old_path = os.getcwd()
        os.chdir(self.data_path)
        pylibmegahal.megahal_cleanup()
        os.chdir(old_path)

    def initial_greeting(self):
        """ Return an initial greeting

        Note that the result will be in all uppercase.  If you're just
        looking for a response with no context, you're better off doing
        do_reply() with no input.

        """
        return pylibmegahal.megahal_initial_greeting()

    def learn(self, input):
        """ Train MegaHAL with given input

        Keyword arguments:
        input -- Text to input
        """
        pylibmegahal.megahal_learn(input, 0)

    def do_reply(self, input=''):
        """ Return a reply with given input

        Keyword arguments:
        input -- Text to input

        If no input is given, this is equivalent to initial_greeting(),
        but with better presentation.
        """
        return pylibmegahal.megahal_do_reply(input, 0)
