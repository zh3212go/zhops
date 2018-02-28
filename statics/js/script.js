function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}
$(document).ready(function(){
    $("#loginBtn").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};
        if (user.length === 0) {
            $("#username_tip").text('username is null') ;
            $("#password_tip").text('') ;
            $("#username").focus();
            return false;
        }
        if (pwd.length === 0) {
            $("#username_tip").text('') ;
            $("#password_tip").text('password is null') ;
            $("#password").focus();
            return false;
        }
        $.ajax({
            type:"post",
            url:"/login",
            data:pd,
            cache:false,
            success:function(data){
                if (data === user) {
                    window.location.href = "/user?user="+data;
                }
                if (data === "-1") {
                    $("#username_tip").text('user is not exist') ;
                    $("#password_tip").text('') ;
                    $("#username").focus();
                }
                if (data === "-2") {
                    $("#username_tip").text('') ;
                    $("#password_tip").text('password is wrong') ;
                    $("#password").focus();
                }
            },
            error:function(){
                alert("error!");
            }
        });
        return false;
    });
});