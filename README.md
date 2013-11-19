# PiCam

These Bash scripts handle the events of the [Motion](http://www.lavrsen.dk/foswiki/bin/view/Motion/WebHome) program.
This script checks if the area is secure and disable motion if it's the case.
If the area is considered unsecure, then Motion detection is enabled.

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

This software has been tested on Raspbian on a Raspberry Pi.

## Requirements

- Motion (`apt-get install motion`)
- ssmtp (`apt-get install ssmtp`)
- mpack (`apt-get install mpack`)
- [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)
  (or any other upload script)
 Executed by `picam_event` and `picam_supervise`.

## Components

### The "event" part

* `picam_event` does something when a motion event is triggered.
Executed by Motion based on the settings in `/etc/motion/motion.conf`

* `picam_notify` notifies you of something.

### The "supervise" part

* `picam_supervise` does stuff automatically.
By default it is executed to check if the area is secure.
It decides to enable or disable motion detection based on `$CHECK_SECURE_AREA` in `/etc/picam.conf`
It is executed by cron every minute (maybe a bit overkill?).

* `motion_control` controls motion. Executed by `picam_supervise`.

## Installation

The installation of the software is quite simple however the setup and configuration
require some work.

The summary of the installation looks like this:

1. Prepare the system
2. Write your check_secure_area script
3. Install Picam
4. Configure motion
5. Configure PiCam

### 1. Prepare the system

* Install the required packages above
* Install dropbody_uploader.sh or any other script that uploads the media files somewhere safe. <!-- TODO: put in picam.conf -->

### 2. Write your `check_secure_area` script

This is a script that you will write yourself!

It is a script that decides if the area is considered "secure".
For instance if friendly presence is in the room, the area can be considered secure.
If the room is empty, then it is considered "insecure"

This will be used to disable or enable motion detection.

* If the area is considered "secure", then motion detection is disabled.
* If the area is considered "insecure", then motion detection is enabled.

This script must exit `0` if the area is considered secure.
If this script exits with something else than `0`, the area will be considered "not secure"
and motion detection will be activated.

This file must be referenced in `$CHECK_SECURE_AREA` field of `/etc/picam.conf`.

Look in the `examples` folder for an example poorly based on ping.

### 3. Install Picam

* Download PiCam
```
git clone https://github.com/samyboy/picam

# Copy the config file
sudo cp ./picam/etc/picam.conf /etc/picam.conf

# Install the event part
sudo cp ./picam/bin/picam_event /usr/local/bin/
sudo cp ./picam/bin/picam_notify /usr/local/bin/

# Install the  "supervise" part
sudo cp ./picam/bin/motion_control /usr/local/bin/
sudo cp ./picam/bin/picam_supervise /usr/local/bin/
sudo cp ./picam/etc/cron.d/picam /etc/cron.d/
```

The basic setup is done: it's time for some configuration.

### 4. Configure motion

* Configure your motion installation with the following settings in `/etc/motion/motion.conf`:

```
on_event_start /usr/local/bin/picam_event event_start %v %C
on_event_end /usr/local/bin/picam_event event_end %v %C
on_picture_save /usr/local/bin/picam_event picture_save %v %C %f
on_movie_start /usr/local/bin/picam_event movie_start %v %C %f
on_movie_end /usr/local/bin/picam_event movie_end %v %C %f
on_camera_lost /usr/local/bin/picam_event camera_lost
```

Restart motion to apply changes

### 5. Configure PiCam

* The main configuration file is `/etc/picam.conf`.
Have a look and configure it wisely, especially the option `$CHECK_SECURE_AREA`.

#### 5.1 Configure notifications

By default the notifications are done by email with the script `picam_notify`.

* Configure ssmtp in `/etc/ssmtp.conf`.
If you use gmail, a working example of this file is available in the
`examples/ssmtp.conf` folder.

Feel free to edit `picam_notify` if you want to use another notification system.

#### 5.2. Configure syslog

By default everything is sent to syslog using the `logger` command.

You can copy the files `examples/rsyslog.d/picam.conf` and
`examples/logrotate.d/picam` to the appropriate folder if you want to have a
special generated log file.
<!-- TODO: move the syslog files into /examples -->


## The `examples` folder
<!-- TODO: refaire -->

* `examples/motion.conf`

    is my configuration file for Motion. Kind of works with a Logitec C270.

* `examples/ssmtp.conf`

    is file for ssmtp that works with gmail. Change your email, username and password to make it work.


## License

TODO

