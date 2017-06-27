# capio-word-exporter
Generate Word document from Capio transcription result


## Setup

### Python environment.

This package runs on Python 3.6 runtime.
For the clean install, use either Anaconda or Virtualenv to create new environment.

For Anaconda,

```bash
conda create --name capio-word-exporter python=3.6
source activate capio-word-exporter
pip install .
```


## Command line usage

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


## Test

You can run unit test with the following command.

```
python setup.py test
```
