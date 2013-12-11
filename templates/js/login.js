$(function(){
    $('#signin').bind('click', function(){
        controller.login(
            $('input[name="username"]').val(), 
            $('input[name="password"]').val(), 
            $('input[name="remember_me"]').is(':checked'));
        window.location.href = 'content.html'
    });
});