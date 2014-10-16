---
layout: default
title: Installing Fig
---

Installing Fig
==============

First, install Docker version 1.3 or greater.

If you're on OS X, you can use the [OS X installer](https://docs.docker.com/installation/mac/) to install both Docker and boot2docker. Once boot2docker is running, `boot2docker shellinit` will output the environment variables you need to set:

    $ boot2docker shellinit
    export DOCKER_HOST=tcp://192.168.59.103:2376
    export DOCKER_CERT_PATH=/Users/me/.boot2docker/certs/boot2docker-vm
    export DOCKER_TLS_VERIFY=1

You can wrap it in `$(...)` and it'll set up your environment for you:

    $ $(boot2docker shellinit)

To persist the environment variables across shell sessions, you can add the output of `boot2docker shellinit` to your `~/.bashrc` file.

There are also guides for [Ubuntu](https://docs.docker.com/installation/ubuntulinux/) and [other platforms](https://docs.docker.com/installation/) in Docker’s documentation.

Next, install Fig:

    curl -L https://github.com/docker/fig/releases/download/0.5.2/fig-`uname -s`-`uname -m` > /usr/local/bin/fig; chmod +x /usr/local/bin/fig

Releases are available for OS X and 64-bit Linux. Fig is also available as a Python package if you're on another platform (or if you prefer that sort of thing):

    $ sudo pip install -U fig

That should be all you need! Run `fig --version` to see if it worked.
