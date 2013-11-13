PiCam
=====

These Bash scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.

Note that this is a personal project.
It might not fit you at all.

This script checks if the area is secure and disable motion if it's the case.

If the area is considered unsecure, then Motion detection is enabled.

Basically:

* When a new event is started, the user receives an email
* When a new image is created, the user receives an email with the image as attachment. The image is uploaded to Dropbox.
* When a new video is created, the user receives an image and the video is uploaded to Dropbox.

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

* `picam_supervise`
Decides to enable or disable motion detection based on `$CHECK_SECURE_COMMAND` in /etc/picam.conf

* `motion_control`
Controls motion. Executed by `motion_supervise`

* `picam_event`
Does something when a motion event is triggered. Executed by Motion based on the settings in `/etc/motion/motion.conf`

* `picam_notify`
Notifies you of something. Executed by `picam_event` and `picam_supervise`.

* `examples/motion.conf`
My configuration file for Motion. Kind of works with a Logitec C270.

* `examples/ssmtp.conf`
A file that works with gmail. Change your email, username and password to make it work.


