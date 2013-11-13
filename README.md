# PiCam

These Bash scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.

This script checks if the area is secure and disable motion if it's the case.

Note that this is a personal project.
It might not fit you at all.

## Compatibility

This software has been tested on Raspberry Pi only.

## Requirements

- Motion
- ssmtp
- mpack
- dropbox_uploader.sh

## Installation

* Install the required packages:

```
apt-get install motion ssmtp mpack
```

* Configure ssmtp in /etc/ssmtp.conf. If you use gmail, a working example of this file is available in "examples/ssmtp.conf" folder.

* Download and install PiCam
```
git clone https://github.com/samyboy/picam
cd picam
sudo ./setup install
```
* Configure /etc/picam.conf (see below)
* Configure /etc/motion.conf
* Done!

## Uninstallation

```
sudo ./setup uninstall
rm /etc/picam.conf
```

## Configuration
The configuration file is stored at /etc/picam.conf.

## Contents

* picam_supervise
Decides to enable or disable motion detection based on $CHECK_SECURE_COMMAND in /etc/picam.conf

* motion_control
Controls motion. Executed by "motion_supervise"

* picam_event
Does something when a motion event is triggered. Executed by motion based on the settings in motion.conf

* picam_notify
Notifies you of something. Executed by picam_event and picam_supervise



