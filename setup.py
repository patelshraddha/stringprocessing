#!/usr/bin/env python
import setuptools


setuptools.setup(name='pepperstone-string-processor',
      version='0.0.1',
      description='Pepperstone string problem',
      author='Shraddha Patel',
      author_email='shrapate@gmail.com',
      python_requires='>=3.7',
      packages=['string_processor'],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      # pylint: disable=line-too-long
      entry_points={
        'console_scripts': [
            'scrmabled-strings=string_processor.count:cli_run_counter'
        ],
      },
      include_package_data=True,
)