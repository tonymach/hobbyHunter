$('#createSession').on 'show.bs.modal', (event) ->

  button = $(event.relatedTarget)
  # Button that triggered the modal
  page = button.data('pageid')
  # Extract info from data-* attributes
  # If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  # Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.

  modal = $(this)
  modal.find('#pageId').val page
  return



addSession = ()->

  console.log 'create post is working!'

  pageId = $('#pageId').val()
  spots = $('#spots').val()
  datetime = $('#datetime').val()
  # mainImage = $('editMainImage').val()

  $.ajax
    url: '/lets/add/a/session/'
    type: 'POST'
    async: true
    data:
      'csrfmiddlewaretoken': Cookies.get('csrftoken')
      'pageId': pageId
      'spots': spots
      'datetime': datetime
    success: (json) ->
      alert(json)
      console.log(json)
      return
    error: (xhr, errmsg, err) ->
      # add the error to the dom
      console.log xhr.status + ': ' + xhr.responseText
      # provide a bit more info about the error to the console
      return


$(document).ready ->
  $('#createSessionForm').submit (event) ->
    event.preventDefault()
    addSession()

  return
