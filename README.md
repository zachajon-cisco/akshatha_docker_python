### Building the container

```bash
docker build -t uber_python_test .
```

### Example execution

```bash
$ docker build -t akshatha .
[+] Building 2.1s (12/12) FINISHED                                                                                                                                                                                                                                                                                                                                docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                                                                                                                                                                                                                              0.0s
 => => transferring dockerfile: 285B                                                                                                                                                                                                                                                                                                                                              0.0s
 => [internal] load metadata for docker.io/library/python:3.12                                                                                                                                                                                                                                                                                                                    0.0s
 => [internal] load .dockerignore                                                                                                                                                                                                                                                                                                                                                 0.0s
 => => transferring context: 2B                                                                                                                                                                                                                                                                                                                                                   0.0s
 => [1/8] FROM docker.io/library/python:3.12                                                                                                                                                                                                                                                                                                                                      0.0s
 => [internal] load build context                                                                                                                                                                                                                                                                                                                                                 0.0s
 => => transferring context: 37B                                                                                                                                                                                                                                                                                                                                                  0.0s
 => CACHED [2/8] RUN apt update                                                                                                                                                                                                                                                                                                                                                   0.0s
 => CACHED [3/8] RUN apt upgrade -y                                                                                                                                                                                                                                                                                                                                               0.0s
 => CACHED [4/8] RUN pip3 install aws_requests_auth==0.4.3                                                                                                                                                                                                                                                                                                                        0.0s
 => CACHED [5/8] RUN pip3 install requests==2.32.3                                                                                                                                                                                                                                                                                                                                0.0s
 => [6/8] RUN pip3 install boto3==1.35.2                                                                                                                                                                                                                                                                                                                                          1.9s
 => [7/8] COPY test-uber-ip.py .                                                                                                                                                                                                                                                                                                                                                  0.0s
 => ERROR [8/8] RUN python test-uber-ip.py                                                                                                                                                                                                                                                                                                                                        0.2s
------
 > [8/8] RUN python test-uber-ip.py:
0.188 Traceback (most recent call last):
0.188   File "//test-uber-ip.py", line 22, in <module>
0.188 hello
0.188     with open("ip_test.txt") as f:
0.188          ^^^^^^^^^^^^^^^^^^^
0.188 FileNotFoundError: [Errno 2] No such file or directory: 'ip_test.txt'
------
Dockerfile:10
--------------------
   8 |     COPY test-uber-ip.py .
   9 |
  10 | >>> RUN python test-uber-ip.py
--------------------
ERROR: failed to solve: process "/bin/sh -c python test-uber-ip.py" did not complete successfully: exit code: 1
```
