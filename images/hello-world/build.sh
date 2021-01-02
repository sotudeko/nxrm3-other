#!/bin/bash

javac HelloWorld.java
java -cp . HelloWorld

docker build -t helloworld-app .
docker tag a1fbd1c3128f sola.local:18082/helloworld-app:1.0
docker push sola.local:18082/helloworld-app:1.0
