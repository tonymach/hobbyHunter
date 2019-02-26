var login, logout;

login = function(user, pass) {
  return $.post('/lets/login/', {
    username: user
  }, password(pass), {
    success: function(data) {
      return alert(data);
    }
  });
};

logout = function() {
  return $.post('/lets/logout/', {
    success: function(data) {
      return alert(data);
    }
  });
};
