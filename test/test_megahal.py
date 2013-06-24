import unittest
import libmegahal
import os
import tempfile
import shutil


class TestMegaHAL(unittest.TestCase):
    def setUp(self):
        self.lastcwd = os.getcwd()
        self.path = tempfile.mkdtemp()

    def tearDown(self):
        os.chdir(self.lastcwd)
        shutil.rmtree(self.path)

    def write_initial_training(self):
        with open(os.path.join(self.path, 'megahal.trn'), 'w') as f:
            f.write('Hello there, it is indeed a great pleasure to meet you.\n')
            f.write('Welcome to my world.\n')

    def test_no_training(self):
        with self.assertRaises(OSError):
            libmegahal.MegaHAL(path=self.path)

    def test_invalid_directory(self):
        self.write_initial_training()
        with self.assertRaises(OSError):
            libmegahal.MegaHAL(path=os.path.join(self.path, 'invalid'))

    def test_cwd_unchanged(self):
        self.write_initial_training()
        old_cwd = os.getcwd()
        libmegahal.MegaHAL(path=self.path)
        self.assertEqual(os.getcwd(), old_cwd)

    def test_cleanup(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path, autosave=False)
        mh.learn('Hello world!')
        mh.cleanup()
        self.assertTrue(os.path.exists(os.path.join(self.path, 'megahal.brn')))

    def test_no_cleanup(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path, autosave=False)
        mh.learn('Hello world!')
        self.assertFalse(os.path.exists(os.path.join(self.path, 'megahal.brn')))

    def test_autosave(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path, autosave=True)
        mh.learn('Hello world!')
        del mh
        self.assertTrue(os.path.exists(os.path.join(self.path, 'megahal.brn')))

    def test_initial_greeting(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path)
        self.assertIsNotNone(mh.initial_greeting())

    def test_learn(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path)
        self.assertIsNone(mh.learn('Hello world!'))

    def test_do_reply(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path)
        self.assertIsNotNone(mh.do_reply('Hello.'))

    def test_do_reply_no_input(self):
        self.write_initial_training()
        mh = libmegahal.MegaHAL(path=self.path)
        self.assertIsNotNone(mh.do_reply())


if __name__ == '__main__':
    unittest.main()
