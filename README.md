# kedr
KEras-based online Digit Recognizer

You just draw your digit by mouse, and kedr recognize it! Magic! 

## Docker install & launch under Ubuntu 16.04

First of all, you need to clone this repo in some folder and type in cmd from there:

```bash
sudo docker build . -t kedr
```

Then it's needed to run backend:
```bash
sudo docker run kedr
```

To access the app you need to check out the docker container ip. For example:
```
sudo docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED              STATUS              PORTS               NAMES
3497542a0605        kedr                "python core.py"    About a minute ago   Up About a minute   5000/tcp            hungry_davinci

sudo docker inspect 3497542a0605
...
"IPAddress": "172.17.0.2"
```
Finally you can access to the app in your browser via link:
```
http://172.17.0.2:5000
```

Have fun! 
