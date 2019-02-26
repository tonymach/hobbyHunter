var endSession, scan, stopScan;

scan = function() {
  $('#scanWindow').show();
  $('#beginWindow').hide();
  $('#reader').html5_qrcode((function(data) {
    alert(data);
  }), (function(error) {}), function(videoError) {});
};

stopScan = function() {
  $('#scanWindow').hide();
  $('#reader').html5_qrcode_stop();
  $('#finalize').show();
};

endSession = function() {};

$(document).ready(function() {});
