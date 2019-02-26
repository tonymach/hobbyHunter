var addSession;

$('#createSession').on('show.bs.modal', function(event) {
  var button, modal, page;
  button = $(event.relatedTarget);
  page = button.data('pageid');
  modal = $(this);
  modal.find('#pageId').val(page);
});

addSession = function() {
  var datetime, pageId, spots;
  console.log('create post is working!');
  pageId = $('#pageId').val();
  spots = $('#spots').val();
  datetime = $('#datetime').val();
  return $.ajax({
    url: '/lets/add/a/session/',
    type: 'POST',
    async: true,
    data: {
      'csrfmiddlewaretoken': Cookies.get('csrftoken'),
      'pageId': pageId,
      'spots': spots,
      'datetime': datetime
    },
    success: function(json) {
      alert(json);
      console.log(json);
    },
    error: function(xhr, errmsg, err) {
      console.log(xhr.status + ': ' + xhr.responseText);
    }
  });
};

$(document).ready(function() {
  $('#createSessionForm').submit(function(event) {
    event.preventDefault();
    return addSession();
  });
});
