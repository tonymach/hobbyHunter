# out: basicAdminFuncs.js
login = (user,pass) ->
    $.post '/lets/login/',
        username: user
        password pass
        success: (data) -> alert data

logout = () ->
    $.post '/lets/logout/',
        success: (data) -> alert data
