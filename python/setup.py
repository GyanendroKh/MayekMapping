from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name='meiteimayek-mapping',
  packages=['mayek'],
  include_package_data=True,
  version='0.0.1',
  license='Apache-2.0',
  description='Utility Functions for managing Meitei Mayek Characters and mapping to E-pao Font.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Gyanendro Kh',
  author_email='me@gyanendrokh.dev',
  url='https://github.com/GyanendroKh/MayekMapping/tree/master/python',
  keywords=['meiteimayek', 'meitei-mayek', 'mapping', 'utility', 'manipuri'],
  classifiers=[        
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Operating System :: OS Independent'
  ],
)
