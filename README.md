# Overview
The repository is organised as a package `string_processor` with files `count.py` and `word.py` and a `tests` folder to store the unit tests.

`count.py` is the main file with two functions:
`count_large_datasets()` and `count_small_datasets()` based on the analysis in [Google Challenge](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/0000000000051004). 

`word.py` has the implementation of a class `Word` to support the function `count_large_datasets()`.

The package has a command line utility through `setup.py` and works with

```bash 
scrmabled-strings --dictionary input/dictionary.txt --input input/input.txt
```

The simplest way to build and run the package is to edit the files `dictionary.txt` and `input.txt` in the `input` folder.

This can now be built using a Dockerfile:

```bash
docker build --no-cache -t pepperstone-string-processor .
```
and run through 

```bash
docker run pepperstone-string-processor /code/build_and_run_string_processor.sh
```
The above command installs the package, runs unit tests and finally the code to generate the output.
