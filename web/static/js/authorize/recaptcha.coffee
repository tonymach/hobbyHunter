get_action = (form) ->
  v = grecaptcha.getResponse()
  if v.length == 0
    document.getElementById('captcha').innerHTML = 'You can\'t leave Captcha Code empty'
    false
  else
    document.getElementById('captcha').innerHTML = 'Captcha completed'
    true
