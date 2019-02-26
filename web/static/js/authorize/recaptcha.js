var get_action;

get_action = function(form) {
  var v;
  v = grecaptcha.getResponse();
  if (v.length === 0) {
    document.getElementById('captcha').innerHTML = 'You can\'t leave Captcha Code empty';
    return false;
  } else {
    document.getElementById('captcha').innerHTML = 'Captcha completed';
    return true;
  }
};
