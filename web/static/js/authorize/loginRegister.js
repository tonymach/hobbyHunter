var login, loginCall, loginOrRegister, register, registerCall;

login = function(callback) {
  $('.modal').modal('hide');
  $('#login').modal('show');
  $('#loginForm').submit(function(event) {
    event.preventDefault();
    if (loginCall()) {
      $('#login').modal('hide');
      if (callback != null) {
        callback(callback = true);
      } else {
        location.reload();
      }
    } else {
      alert('Wrong!');
    }
  });
};

loginCall = function() {
  var val;
  val = null;
  console.log('create post is working!');
  $.ajax({
    url: '/lets/ajax/login/',
    type: 'POST',
    async: false,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'pass': $('#loginPassword').val(),
      'username': $('#loginUsername').val()
    },
    success: function(json) {
      console.log('success');
      console.log(json);
      if (json['result'] === 'success') {
        console.log('true');
        val = true;
      } else {
        val = false;
      }
    },
    error: function(xhr, errmsg, err) {
      $('#results').html('<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>');
      console.log(xhr.status + ': ' + xhr.responseText);
    }
  });
  return val;
};

register = function(callback) {
  $('.modal').modal('hide');
  $('#signup').modal('show');
  $('#signupForm').submit(function(event) {
    event.preventDefault();
    if (registerCall()) {
      $('#signup').modal('hide');
      if (callback != null) {
        callback(callback = true);
      } else {
        location.reload();
      }
    } else {
      alert('Wrong!');
    }
  });
};

registerCall = function() {
  var val;
  val = null;
  console.log('create post is working!');
  $.ajax({
    url: '/lets/ajax/register/',
    type: 'POST',
    async: false,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'pass': $('#registerPassword').val(),
      'user': $('#registerUsername').val()
    },
    success: function(json) {
      console.log('success');
      console.log(json);
      if (json['result'] === 'success') {
        console.log('true');
        val = true;
      } else {
        val = false;
      }
    },
    error: function(xhr, errmsg, err) {
      $('#results').html('<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>');
      console.log(xhr.status + ': ' + xhr.responseText);
    }
  });
  return val;
};

loginOrRegister = function() {
  $('.modal').modal('hide');
  $('#loginOrRegister').modal('show');
};
