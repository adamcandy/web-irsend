var event;
var attendQuery;

$(document).ready(function () {
    //docReady();
});

function clickedOp(device_id, op)
{
    // $.ajax({url:'../device/' + device_id + '/clicked/' + op});
    $.ajax({url:device_id + '/clicked/' + op});
}

function clickedinputsource(device_id, op)
{
    in_tv = '#F3E600';
    in_apple = '#000000';

    option = document.getElementById('volumeten').getAttribute('opacity');
    option = document.getElementById('inputsource').getAttribute('fill');

    if (option == in_tv) {
        document.getElementById('inputsource').setAttribute('fill', in_apple);
    	$.ajax({url:device_id + '/clicked/inputsource/apple'});
    } else {
        document.getElementById('inputsource').setAttribute('fill', in_tv);
    	$.ajax({url:device_id + '/clicked/inputsource/tv'});
    }

    // $.ajax({url:'../device/' + device_id + '/clicked/' + op});
    //$.ajax({url:device_id + '/clicked/' + op});
}

function clickedvolumeten(device_id)
{
    volumetencolour_off = '0.0';
    volumetencolour_on = '1.0';
    option = document.getElementById('volumeten').getAttribute('opacity');
    if (option == volumetencolour_on) {
        document.getElementById('volumeten').setAttribute('opacity', volumetencolour_off);
    	$.ajax({url:device_id + '/clicked/volumeten/off'});
    } else {
        document.getElementById('volumeten').setAttribute('opacity', volumetencolour_on);
    	$.ajax({url:device_id + '/clicked/volumeten/on'});
    }

 
    //document.getElementById('volumeten').setAttribute('fill', 'yellow');
    //$('volumeten').style.fill="yellow";

}


