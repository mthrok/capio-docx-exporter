[![CircleCI](https://circleci.com/gh/mthrok/capio-word-exporter.svg?style=svg)](https://circleci.com/gh/mthrok/capio-word-exporter)

# Capio Transcript Word Exporter
Generate Word document from Capio transcript

## 1. Setup

This package can be run as command line tool. Either you can install it in your local environment, or in a Docker container.

- Install as command line tool.

This package runs on Python 3.6 runtime.
For the clean install, use either Anaconda or Virtualenv to create new environment.

For Anaconda,

```bash
conda create --name capio-word-exporter python=3.6
source activate capio-word-exporter
pip install .
```

- Install as executable Docker

You can execute the above command inside of Docker.

Simply build docker container and run it.

```bash
docker build -t capio:latest  .
docker run -it capio:test capio_word_exporter
```
For the usage, see bellow.


## 2. Usage

You can use `capio_word_exporter` command line to run the exporter.
Currently this command takes tanscript ID and API Key as arguments as follow. 

```
capio_word_exporter --id <transcript_id> --key <api_key> --output <output file name>
```

If you omit these, the default test values are used.

Usage will be changed over the time, but you can always consult usage with `--help` option.

```bash
capio_word_exporter --help
```


## 3. Test

You can run unit test with the following command.

```
python setup.py test
```
