web-irsend
==========

Web-based IR Remote on the Raspberry Pi, a modification of the branch developed by slimjim777 at:

http://github.com/slimjim777/web-irsend

git://github.com/slimjim777/web-irsend.git

with information at:

http://randomtutor.blogspot.co.uk/2013/01/web-based-ir-remote-on-raspberry-pi.html

and using Alex Bain's lirc details at:

http://alexba.in/blog/2013/02/23/controlling-lirc-from-the-web/

Developments
============

The developments include:
 - New web remote layout (with bigger buttons) - see below.
 - Enable multiple lirc commands to be sent with one button press
 - Cleaned up links to enable proxying through an Apache server
 - Daemon script added

Daemon for autorunning on boot
==============================

Add the following line to /etc/rc.local

/home/pi/web-irsend/daemon &

(replace path with the full path to the daemon script).

New remote layout
=================

![Remote layout](./static/remote_layout.png?raw=true "Remote layout")
