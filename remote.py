#!/usr/bin/env python

from lirc.lirc import Lirc
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

BASE_URL = ''
volumeten = False

app = Flask(__name__)

# Initialise the Lirc config parser
lircParse = Lirc('/etc/lirc/lircd.conf')


@app.route("/")
@app.route("/<device>")
def index(device=None):
    # Get the devices from the config file
    devices = []
    for dev in lircParse.devices():
        d = {
            'id': dev,
            'name': dev,
        }
        devices.append(d)
    
    return render_template('remote.html', devices=devices)

def volumetencolour(option):
    #volumetencolour_off = '#F18518'
    #volumetencolour_on = '#FF0000'
    volumetencolour_off = '0'
    volumetencolour_on = '1'
    if option:
	return volumetencolour_on
    else:
        return volumetencolour_off
  
@app.route("/device/<device_id>")
def device(device_id=None):
    d = {'id':device_id}        
    if device_id.startswith('apple'):
        return render_template('control_apple.html', d=d, volumetencolour=volumetencolour(volumeten))
    else:
        return render_template('control.html', d=d, volumetencolour=volumetencolour(volumeten))


@app.route("/device/<device_id>/clicked/<op>")
def clicked(device_id=None, op=None):
    # Send message to Lirc to control the IR
    if (op.startswith('volume') and volumeten):
        op = op + ( ' ' + op ) * 9
        lircParse.send_once(device_id, op)
    else:	
        lircParse.send_once(device_id, op)
    return ""

@app.route("/device/<device_id>/clicked/volumeten/<op>")
def clickedvolumetenoption(device_id=None, op='off'):
    global volumeten
    if op == 'on':
        volumeten = True
    else:
        volumeten = False
    return ""



if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')


