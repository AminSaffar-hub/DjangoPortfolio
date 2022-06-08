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

## Installing the client
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

## Installing the local locker app
Pull the local locker image from the aws public registry(< 200 GB):

```bash
docker pull public.ecr.aws/f7d4x8o5/local-locker-add:latest
```

tag the local locker image:

```bash
docker tag public.ecr.aws/f7d4x8o5/local-locker-add:latest local-locker-add:latest
```

## Running the client and the local locker app
```bash
roslaunch rosbridge_server rosbridge_websocket.launch
```

```bash
cd add-mission-client
docker compose --profile without-rosmaster up
```

## Updating
to update the client re-reun the installation instructions.

