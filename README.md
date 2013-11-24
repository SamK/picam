# PiCam

**WARNING: This project is under heavy developpment**

> Note that this is a personal project.
> It might not fit you at all.
> It does not work well anyway and is sketchy.

These scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.

Examples:

* When an image is created, it's sent by email.
* When an video is created, it's uploaded to Dropbox.
* automatically disables or enables motion detection

## Compatibility

This software has been tested on Raspbian on a Raspberry Pi with a logitec C720.

## Requirements

* Motion (`apt-get install motion`)
* ssmtp (`apt-get install ssmtp`)
* mpack (`apt-get install mpack`)
* [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)
  (or any other upload script).

## Components

* `picam_event` does something when a motion event is triggered.
Executed by Motion based on the settings in `/etc/motion/motion.conf`
* `picam_notify` notifies you of something by email.
* `picam_supervise` checks if the zone is secure and does appropriate action.
By default it is executed to check if the zone is secure.
It decides to enable or disable motion detection based on `$CHECK_ZONE_CMD` in `/etc/picam.conf`
It is executed by cron every minute.
* `motion_control` controls the Motion software. Executed by `picam_supervise`.

## Installation

The installation of the software is quite simple however the setup and configuration
require some work.

The summary of the installation looks like this:

1. Prepare the system
2. Install Picam
3. Configure PiCam
4. Configure Motion

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

    If you want you can copy the files in `misc/rsyslog.d/` and
    `misc/logrotate.d/` to the appropriate system folder if you want to have a
    separated log file.

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

