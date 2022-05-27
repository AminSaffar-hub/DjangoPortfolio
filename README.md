## description
This git repository contains the launch file necessary to run the lmad mission client on an add robot. Currently it contains the following files.

map_param_files/params.yaml: the ros parameters necessary to configure the client.
docker-compose.yml: the docker compose file used to run the client image.
model_configs.env: the file containing environment variables used to configure the robot and locker types.
rosmaster_configs.env: the file containing environment variables used to connect the client to a running rosmaster on the robot.

## Requirements
- Docker (https://www.docker.com/get-started)
- Xserver:
    - Xserver for Ubuntu users:
        -installation guide: https://askubuntu.com/questions/213678/how-to-install-x11-xorg

## Installation
Pull the git repository:

```bash
git clone https://github.com/AmineSaffar/add-mission-client.git
```

Pull the client image from the aws public registry(1.5GB):

```bash
docker pull public.ecr.aws/f7d4x8o5/mission-client-add:latest
```

tag the client image:

```bash
docker tag public.ecr.aws/f7d4x8o5/mission-client-add:latest mission-client-add:latest 
```

## Running the client
if there is already a running roscore:

```bash
cd add-mission-client
docker compose --profile without-rosmaster up
```

if there is no roscore running:

```bash
cd add-mission-client
docker compose --profile with-rosmaster up
```

## Updating the client
to update the client re-reun the installation instructions.

## Testing communication:

if there is already a running roscore:

```bash
cd /path/to/add/launch/repostiory
docker-compose --profile test-without-rosmaster up
```

if there is no roscore running:

```bash
cd /path/to/add/launch/repostiory
docker-compose --profile test-with-rosmaster up
```
