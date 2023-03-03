FROM alpine:latest

ARG FILEPATH="./input/input.txt"
RUN apk update
RUN apk add python3 py3-pip

COPY requirements.txt requirements.txt
COPY ${FILEPATH} input.txt
COPY main.py main.py
COPY src/ src/

RUN pip install -r requirements.txt
ENTRYPOINT [ "python3", "main.py"]
CMD ["--input_file_path", "input.txt"]
