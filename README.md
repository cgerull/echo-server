# Echo Server

Simple web echo server for orchestration testing.

## Usage

Use the docker-compose file to build and run the client server demo locally.

For swarm testing use the docker-stack.yml configuration. Change to the image value to use your own, customized images.

## ToDo

- Make path on log volume configurable.
- ~~Create a central logging container with log viewer.~~
- ~~Add logger to call-generator~~
- Add socket exception handling to client.py
- ~~Add REST API to server.~~
- ~~Configure gunicorn log format and include hostname.~~
