# Count Number of Island

This repo was set up to complete a technical assignment for an interview.

The steps are as below:
1. Prepare a script to calculate number of islands from a text file with 1(land) and 0(water).
2. Prepare a bash script to run a script.
3. Prepare a Dockerfile.

## Libraries required
## Run script
```
./count_island.sh ["input_file_path"]
```

## To run docker file
### Build docker image
```
docker build -t [image_name] --build_arg FILEPATH=[path_to_input_file] .
```

### Run Docker image
```
docker run [image_name]
```