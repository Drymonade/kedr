# kedr
Keras-based online digit recognizer

You just draw your one digit by mouse, and kedr recognize it! Magic! 

## Docker install & launch

All you need to do is to clone this repo in some folder and type in cmd from there:

```bash
docker -t build kedr .
```
Then you should check your docker machine ip. For example:
```
docker-machine ip
192.168.99.100
```
So it's needed to run backend:
```bash
docker run -p 5000:5000 kedr
```

Finally you can access to the app in your browser via link:
```
http://192.168.99.100:5000
```

Have fun! 
