from distutils.core import setup


setup(
  name='meiteimayek-mapping',
  packages=['meiteimayek-mapping'],
  version='0.0.1-beta',
  license='Apache-2.0',
  description='Utility Functions for managing Meitei Mayek Characters and mapping to E-pao Font.',
  author='Gyanendro Kh',
  author_email='khgyanendro77@gmail.com',
  url='https://github.com/GyanendroKh/MayekMapping/tree/master/python',
  download_url='https://github.com/GyanendroKh/MayekMapping/releases/download/v0.0.1-beta/python.tar.gz',
  keywords=['meiteimayek', 'meitei-mayek', 'mapping', 'utility', 'manipuri'],
  install_requires=[            
    'json',
    'io',
  ],
  classifiers=[        
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Utility Program',
    'License :: OSI Approved :: Apache-2.0 License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
