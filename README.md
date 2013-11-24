# PiCam

**WARNING: This project is under heavy developpment***

These scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.
This script checks if the zone is secure and disable motion if it's the case.
If the zone is considered unsecure, then Motion detection is enabled.

Basically:

1. When a new event is started, the user receives an email
1. When a new image is created, the user receives an email with the image as
attachment. The image is uploaded to Dropbox.
1. When a new video is created, the user receives an image and the video is
uploaded to Dropbox.

> Note that this is a personal project.
> It might not fit you at all.
> It does not work well anyway and is sketchy.

## Compatibility

This software has been tested on Raspbian on a Raspberry Pi with a logitec C720.

## Requirements

* Motion (`apt-get install motion`)
* ssmtp (`apt-get install ssmtp`)
* mpack (`apt-get install mpack`)
* [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)
  (or any other upload script). Executed by `picam_event`.

## Components

### The "event" part

* `picam_notify` notifies you of something by email.

* `picam_event` does something when a motion event is triggered.
Executed by Motion based on the settings in `/etc/motion/motion.conf`

### The "supervise" part

* `picam_supervise` does stuff automatically.
By default it is executed to check if the zone is secure.
It decides to enable or disable motion detection based on `$CHECK_ZONE_CMD` in `/etc/picam.conf`
It is executed by cron every minute.

* `motion_control` controls motion. Executed by `picam_supervise`.

## Installation

The installation of the software is quite simple however the setup and configuration
require some work.

The summary of the installation looks like this:

1. Prepare the system
2. Install Picam
3. Configure PiCam
4. Configure motion

### 1. Prepare the system

* Install the required packages above
* Install dropbody_uploader.sh or any other script that uploads the media files somewhere safe.

### 2. Install Picam

This is how to dowload and install the files:

```
git clone https://github.com/samyboy/picam

# Install the binaries
sudo cp ./picam/bin/* /usr/local/bin/

# Copy the config files
sudo cp ./picam/etc/picam.conf /etc/picam.conf
sudo cp ./picam/etc/cron.d/picam /etc/cron.d/
```

It's time for some configuration.

### 3. Configure PiCam

* Have a look at `/etc/picam.conf` and configure it wisely.

* Configure notifications

    By default the notifications are done by email with the script `picam_notify`.

    * Configure ssmtp in `/etc/ssmtp.conf`.
    If you use gmail, a working example of this file is available in the
    `misc` folder.

* Configure syslog

    By default everything is sent to syslog using the `logger` command.
    You can copy the files in `misc/rsyslog.d/picam.conf` and
    `misc/logrotate.d/picam` to the appropriate folder if you want to have a
    special generated log file.

### 4. Configure motion

* Configure your motion installation with the following settings in `/etc/motion/motion.conf`:

```
;on_event_start /usr/local/bin/picam_event event_start %v %C
;on_event_end /usr/local/bin/picam_event event_end %v %C
;on_picture_save /usr/local/bin/picam_event picture_save %v %C %f
;on_movie_start /usr/local/bin/picam_event movie_start %v %C %f
;on_movie_end /usr/local/bin/picam_event movie_end %v %C %f
;on_camera_lost /usr/local/bin/picam_event camera_lost
```

Restart motion to apply changes

## License

TODO

