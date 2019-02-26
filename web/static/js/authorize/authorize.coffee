  authorize = (callback) ->
  $('#authorize').modal('show')
  $('#authorizeForm').submit (event) ->
    event.preventDefault()
    if authorizeCall()
      $('#authorize').modal('hide')
      callback(callback=true)
      return
    else
      alert('Wrong!')
      return
  return


authorizeCall = () ->
  val = null
  console.log 'create post is working!'
  # sanity check
  $.ajax
    url: '/lets/authorize/'
    type: 'POST'
    async: false
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'pass': $('#authorizePassword').val()
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


edit  = (callback=false) ->
  if callback
    submitEdit()
    return
  if not callback
    authorize(edit)
    return


submitEdit = ()->
  title = $('#editTitle').val()
  description = $('#editDescription').val()
  averageCost = $('#editAverageCost').val()
  # mainImage = $('editMainImage').val()

  $.ajax
    url: '/lets/authorize/'
    type: 'POST'
    async: true
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'title': title
      'description': description
      'averageCost': averageCost
    success: (json) ->
      alert('edited!')
      return
    error: (xhr, errmsg, err) ->
      $('#results').html '<div class=\'alert-box alert radius\' data-alert>Oops! We have encountered an error: ' + errmsg + ' <a href=\'#\' class=\'close\'>&times;</a></div>'
      # add the error to the dom
      console.log xhr.status + ': ' + xhr.responseText
      # provide a bit more info about the error to the console
      return

$(document).ready ->
  return
