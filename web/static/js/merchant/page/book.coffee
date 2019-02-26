book = (sessionId, merchant) ->
  # Gameplan
  # Ajax book, if not logged in,
  # return result: notLoggedIn
  # popup login/signup prompt
  # authenticate
  # callback to book
  # book()
  # celebrate
  if not bookCall(sessionId, merchant)
    loginOrRegister()
  return

bookCall = (sessionId, merchant) ->
  val = null
  console.log 'create post is working!'
  # sanity check
  $.ajax
    url: '/lets/book/'
    type: 'POST'
    async: false
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'sessionId': sessionId
      'merchant': merchant

    success: (json) ->
      # remove the value from the input
      # log the returned json to the console
      console.log 'success'
      # another sanity check
      console.log(json)
      if json['result'] == 'success'
        $('.modal').modal('hide')
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





$(document).ready ->
  return
