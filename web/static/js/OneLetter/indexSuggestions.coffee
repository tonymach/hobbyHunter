submitForm = (form) ->

  formData = new FormData(form)
  console.log 'create post is working!'
  # sanity check
  $.ajax
    url: '/lets/post/a/page/'
    type: 'POST'
    data: formData
    processData: false
    contentType: false
    success: (json) ->
      # remove the value from the input
      console.log json
      # log the returned json to the console
      console.log 'success'
      # another sanity check

      $('.modal').modal('hide');

      return
    error: (xhr, errmsg, err) ->
      $('#results').html '<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>'
      # add the error to the dom
      console.log xhr.status + ': ' + xhr.responseText
      # provide a bit more info about the error to the console
      return
  return

$(document).ready ->
  $('#createPageForm').submit (event) ->
    event.preventDefault()
    submitForm(this)
    return
  return
