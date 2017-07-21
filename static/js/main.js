$(document).ready(function(){
  let namespace = "/test";
  let video = document.querySelector("#videoElement");
  let canvas = document.querySelector("#canvasElement");
  let ctx = canvas.getContext('2d');
  let image = document.querySelector("#imageElement");

  var localMediaStream = null;

  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

  function sendImage(dataURL) {
    socket.emit('input image', dataURL);
  }

  function snapshot() {
    if (!localMediaStream) {
      return null;
    }

    ctx.drawImage(video, 0, 0);

    let dataURL = canvas.toDataURL('image/jpeg');
    sendImage(dataURL);
  }

  socket.on('connect', function() {
    console.log('Connected!');
  });

  // socket.on('new image', function(newImageURL) {
  //   image.src = newImageURL;
  // });

  var constraints = {
    video: {
      width: { min: 640 },
      height: { min: 360 }
    }
  };

  navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
    video.srcObject = stream;
    localMediaStream = stream;

    setInterval(function () {
      snapshot();
    }, 50);
  }).catch(function(error) {
    console.log(error);
  });
});

