var viewSessions;

viewSessions = function(pageId) {
  $('#viewSessions').modal('show');
  $('.startSessionButton').each(function() {
    return $(this).attr('href', $(this).attr('href') + pageId + '/');
  });
  return;
};

$(document).ready(function() {});
