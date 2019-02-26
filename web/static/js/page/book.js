var book, bookCall;

book = function(sessionId, merchant) {
  if (bookCall(sessionId, merchant) !== true) {
    return loginOrRegister();
  } else {
    $('.modal').modal('hide');
    swal("You booked it! When you show up just check your calendar and tap the class name");
  }
};

bookCall = function(sessionId, merchant) {
  var val;
  val = null;
  console.log('create post is working!');
  $.ajax({
    url: '/livingDead/book/',
    type: 'POST',
    async: false,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'sessionId': sessionId,
      'merchant': merchant
    },
    success: function(json) {
      console.log('success');
      console.log(json);
      if (json['result'] === 'success') {
        console.log('true');
        val = true;
      } else if (json['result'] === 'already') {
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

$(document).ready(function() {});
