$(document).ready(function() {

    $("#flag_map").hide();

    $("#btnLogIn").click(function() {
        login();
    });

    $("#btnRegister").click(function() {
        register();
    });
    
});

function showFlag() {
    $("#original_map").hide();
    $("#flag_map").show();
}

function hideFlag() {
    $("#original_map").show();
    $("#flag_map").hide();
}

function gotToLandingPage() {
    window.location.href = "/home";
}

function smartWatch() {
    window.location.href = "/smart-watch";
}

function setTime() {
    window.location.href = "/set-time";
}

function createSketch() {
    window.location.href = "/sketch";
}

function register() {
    var first_name = $("#firstname").val();
    var last_name = $("#lastname").val();
    var email = $("#email").val();
    var contact_number = $("#contact_number").val();
    var password = $("#password").val();

    var allies = [];
    allies.push({"name": $("#name1").val(), "contact_number": $("#number1").val()});
    allies.push({"name": $("#name2").val(), "contact_number": $("#number2").val()});
    allies.push({"name": $("#name3").val(), "contact_number": $("#number3").val()});
    allies.push({"name": $("#name4").val(), "contact_number": $("#number4").val()});
    allies.push({"name": $("#name5").val(), "contact_number": $("#number5").val()});
    allies.push({"name": $("#name6").val(), "contact_number": $("#number6").val()});

    $.ajax({
        method: "POST",
        url: "/add_user",
        data: {"first_name": first_name, "last_name": first_name, "email": email, "contact_number": contact_number, "password": password, "allies": allies},
        success: function(data) {
            console.log("Creation successful. " + JSON.stringify(data));
        },
        error: function(data) {
            console.log("Error in creating user. " + JSON.stringify(data));
        }
    })
}

function login() {
    var email = $("#email").val();
    var password = $("#password").val();

    $.ajax({
        method: "POST",
        url: "/execute_login",
        data: {"email": email, "password": password},
        dataType: "application/json",
        success: function(data) {
            console.log(data);
            data = JSON.parse(data)
            if(data.message == "Exists.") {
                window.location = "/home"
            } else {
                alert("Account does not exists.")
            }
        },
        error: function(data) {
            console.log("Error in loggin in. " + JSON.stringify(data));
            data = JSON.parse(data.responseText)
            console.log(data)
            if(data.message == "Exists.") {
                window.location = "/home"
            } else {
                alert("Account does not exists.")
            }
        }
    });
}