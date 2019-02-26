var submitForm;

submitForm = function(form) {
  var formData;
  formData = new FormData(form);
  console.log('create post is working!');
  $.ajax({
    url: '/lets/post/a/page/',
    type: 'POST',
    data: formData,
    processData: false,
    contentType: false,
    success: function(json) {
      console.log(json);
      console.log('success');
      $('.modal').modal('hide');
      window.location.reload();
    },
    error: function(xhr, errmsg, err) {
      $('#results').html('<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>');
      console.log(xhr.status + ': ' + xhr.responseText);
    }
  });
};

$(document).ready(function() {
  $('#createPageForm').submit(function(event) {
    event.preventDefault();
    submitForm(this);
  });
});
