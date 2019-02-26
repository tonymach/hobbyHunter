scan = () ->
  $('#scanWindow').show()
  $('#beginWindow').hide()
  $('#reader').html5_qrcode ((data) ->
    alert data
    return
  ), ((error) ->
  ), (videoError) ->
  return
stopScan =  () ->
  $('#scanWindow').hide()
  $('#reader').html5_qrcode_stop()
  $('#finalize').show()
  return

endSession = () ->
  return

$(document).ready ->
  return
