from distutils.core import setup
setup(
  name = 'ProfanityBlocker',
  packages = ['ProfanityBlocker'],
  version = '0.1',
  license='MIT',
  description = 'A Python Intergration For The Profanity Blocker API',
  author = 'David Crompton',
  author_email = 'davidallancrompton@outlook.com',
  url = 'https://github.com/voarsh/ProfanityBlocker-Python-Implementation',
  download_url = 'https://github.com/voarsh/ProfanityBlocker-Python-Implementation/archive/master.tar.gz',
  keywords = ['Profanity Blocker', 'Profanity', 'Word Filter', 'Filter'],
  install_requires=[ 
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)