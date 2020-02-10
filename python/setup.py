from setuptools import setup

with open("README", "r") as fh:
  long_description = fh.read()

setup(
  name='meiteimayek-mapping',
  packages=['mayek'],
  version='0.0.1b0',
  license='Apache-2.0',
  description='Utility Functions for managing Meitei Mayek Characters and mapping to E-pao Font.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Gyanendro Kh',
  author_email='khgyanendro77@gmail.com',
  url='https://github.com/GyanendroKh/MayekMapping/tree/master/python',
  keywords=['meiteimayek', 'meitei-mayek', 'mapping', 'utility', 'manipuri'],
  classifiers=[        
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
)
