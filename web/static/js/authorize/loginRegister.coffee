login = (callback) ->
  $('.modal').modal('hide')
  $('#login').modal('show')
  $('#loginForm').submit (event) ->
    event.preventDefault()
    if loginCall()
      $('#login').modal('hide')
      if callback?
        callback(callback=true)
      else
        location.reload()
      return
    else
      alert('Wrong!')
      return
  return


loginCall = () ->
  val = null
  console.log 'create post is working!'
  # sanity check
  $.ajax
    url: '/lets/ajax/login/'
    type: 'POST'
    async: false
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'pass': $('#loginPassword').val()
      'username': $('#loginUsername').val()
    success: (json) ->
      # remove the value from the input
      # log the returned json to the console
      console.log 'success'
      # another sanity check
      console.log(json)
      if json['result'] == 'success'
        console.log('true')
        val = true
      else
        val = false
      return
    error: (xhr, errmsg, err) ->
      $('#results').html '<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>'
      # add the error to the dom
      console.log xhr.status + ': ' + xhr.responseText
      # provide a bit more info about the error to the console
      return
  return val


register = (callback) ->
  $('.modal').modal('hide')
  $('#signup').modal('show')
  $('#signupForm').submit (event) ->
    event.preventDefault()
    if registerCall()
      $('#signup').modal('hide')
      if callback?
        callback(callback=true)
      else
        location.reload()
      return
    else
      alert('Wrong!')
      return
  return


registerCall = () ->
  val = null
  console.log 'create post is working!'
  # sanity check
  $.ajax
    url: '/lets/ajax/register/'
    type: 'POST'
    async: false
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'pass': $('#registerPassword').val()
      'user': $('#registerUsername').val()

    success: (json) ->
      # remove the value from the input
      # log the returned json to the console
      console.log 'success'
      # another sanity check
      console.log(json)
      if json['result'] == 'success'
        console.log('true')
        val = true
      else
        val = false
      return
    error: (xhr, errmsg, err) ->
      $('#results').html '<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>'
      # add the error to the dom
      console.log xhr.status + ': ' + xhr.responseText
      # provide a bit more info about the error to the console
      return
  return val


loginOrRegister = () ->
  $('.modal').modal('hide')
  $('#loginOrRegister').modal('show')
  return
