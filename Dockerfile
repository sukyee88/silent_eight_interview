FROM alpine:latest

ARG FILEPATH="./input/input.txt"
RUN apk update
RUN apk add python3 py3-pip

COPY docker_island.sh docker_island.sh
COPY ${FILEPATH} input.txt
ADD main.py main.py
ADD src/ src/

RUN chmod +x ./docker_island.sh 
ENTRYPOINT [ "python3", "main.py"]
CMD ["--input_file_path", "input.txt"]
# CMD ["/bin/sh", "./docker_island.sh"]