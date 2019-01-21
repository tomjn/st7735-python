from setuptools import setup, find_packages


classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'ST7735',
      version           = '0.0.1',
      description       = 'Library to control an ST7735 168x80 TFT LCD display.',
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/pimoroni/st7735-160x80-python/',
      packages          = find_packages())
