PiCam
=====

These Bash scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.
This script checks if the area is secure and disable motion if it's the case.
If the area is considered unsecure, then Motion detection is enabled.

Basically:

1. When a new event is started, the user receives an email
1. When a new image is created, the user receives an email with the image as attachment. The image is uploaded to Dropbox.
1. When a new video is created, the user receives an image and the video is uploaded to Dropbox.

> Note that this is a personal project.
> It might not fit you at all.
> It does not work well anyway and is sketchy.

Compatibility
-------------

This software has been tested on Raspberry Pi only.

Requirements
------------

- Motion (`apt-get install motion`)
- ssmtp (`apt-get install ssmtp`)
- mpack (`apt-get install mpack`)
- [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)

Installation
------------

* Configure ssmtp in `/etc/ssmtp.conf`. If you use gmail, a working example of this file is available in `examples/ssmtp.conf` folder.

* Download and install PiCam
```
git clone https://github.com/samyboy/picam
cd picam
sudo ./setup install
```
* Configure `/etc/picam.conf` (see "Configuration" below)
* Configure `/etc/motion.conf` (see examples/motion.conf)
* Done!

Uninstallation
--------------

```
sudo ./setup purge
```

Configuration
-------------

The configuration file is stored at /etc/picam.conf.
Have a look and configure it wisely, especially the option `$CHECK_SECURE_AREA`.

Contents
--------

* `picam_supervise` ecides to enable or disable motion detection based on `$CHECK_SECURE_COMMAND` in `/etc/picam.conf`

* `motion_control` controls motion.
Executed by `motion_supervise`.

* `picam_event` does something when a motion event is triggered.
Executed by Motion based on the settings in `/etc/motion/motion.conf`

* `picam_notify`
notifies you of something. Executed by `picam_event` and `picam_supervise`.

* `examples/motion.conf`
is my configuration file for Motion. Kind of works with a Logitec C270.

* `examples/ssmtp.conf`
is file for ssmtp that works with gmail. Change your email, username and password to make it work.


