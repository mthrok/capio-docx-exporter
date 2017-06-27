FROM python:3.6

WORKDIR opt
ADD ./ ./
RUN pip install .
CMD ["capio_word_exporter"]
