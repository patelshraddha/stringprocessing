#!/bin/bash

cd /code

# Build the package
pip wheel . -w ./wheelhouse; yes y | pip uninstall pepperstone-string-processor ; TMPDIR=./tmp pip install pepperstone-string-processor --no-index --find-links ./wheelhouse --upgrade
# Run unit tests
python3 -m unittest discover tests/
# Run string counter
scrmabled-strings --dictionary input/dictionary.txt --input input/input.txt