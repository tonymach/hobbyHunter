var authorize, authorizeCall, edit, submitEdit;

authorize = function(callback) {
  $('#authorize').modal('show');
  $('#authorizeForm').submit(function(event) {
    event.preventDefault();
    if (authorizeCall()) {
      $('#authorize').modal('hide');
      callback(callback = true);
    } else {
      alert('Wrong!');
    }
  });
};

authorizeCall = function() {
  var val;
  val = null;
  console.log('create post is working!');
  $.ajax({
    url: '/lets/authorize/',
    type: 'POST',
    async: false,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'pass': $('#authorizePassword').val()
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

edit = function(callback) {
  if (callback == null) {
    callback = false;
  }
  if (callback) {
    submitEdit();
    return;
  }
  if (!callback) {
    authorize(edit);
  }
};

submitEdit = function() {
  var averageCost, description, title;
  title = $('#editTitle').val();
  description = $('#editDescription').val();
  averageCost = $('#editAverageCost').val();
  return $.ajax({
    url: '/lets/authorize/',
    type: 'POST',
    async: true,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'title': title,
      'description': description,
      'averageCost': averageCost
    },
    success: function(json) {
      alert('edited!');
    },
    error: function(xhr, errmsg, err) {
      $('#results').html('<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>');
      console.log(xhr.status + ': ' + xhr.responseText);
    }
  });
};

$(document).ready(function() {});
