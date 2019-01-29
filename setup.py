from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(name='bined',
      version='1.0',
      url='https://github.com/Oseid/bined',
      author='oseid aldary',
      author_email='oseid.eng@gmail.com',
      description='encode/decode binary',
      keywords='bin, Encode, Decode, Binary',
      packages=find_packages(),
      py_modules=['bined'],
      data_files=[('', ['LICENSE'])],
      include_package_data=True,
      classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ])
