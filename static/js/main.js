$(document).ready(function(){
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
  });

  socket.on('my response', function(response) {
    console.log('got response from server:' + response);
  });

  navigator.mediaDevices.getUserMedia({video: true}).then(function(stream) {
    var video = document.querySelector("#videoElement");
    video.src = window.URL.createObjectURL(stream);
  }).catch(function(error) {
    console.log(error);
  });
});

