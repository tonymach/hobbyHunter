viewSessions = (pageId) ->

  $('#viewSessions').modal('show')
  $('.startSessionButton').each ->
    $(this).attr 'href', $(this).attr('href') + pageId + '/'
  return

  return

$(document).ready ->
      return
