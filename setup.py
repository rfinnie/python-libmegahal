from distutils.core import setup, Extension

pylibmegahal_ext = Extension(
    'libmegahal/pylibmegahal',
    sources=[
        'libmegahal/libmegahal.c',
        'libmegahal/pylibmegahal.c'
    ],
)

setup(
    name='LibMegaHAL',
    version='0.1',
    author='Ryan Finnie',
    author_email='ryan@finnie.org',
    packages=['libmegahal'],
    ext_modules=[pylibmegahal_ext],
    url='http://www.finnie.org/',
    license='LICENSE.txt',
    description='Python interface to libmegahal',
    long_description=open('README.txt').read(),
)
