function checkid() {
    var myemail = document.getElementById("exampleInputEmail").value;
    var mypin = document.getElementById("exampleInputPassword").value;
    if (myemail == "") {
        document.getElementById("exampleInputEmail").style.borderColor = "red";
        document.getElementById("email-valid").style.display = "block";
        document.getElementById("email-valid").textContent="Looks Bad!!";
        document.getElementById("email-valid").classList = "text-danger";
    } else {
        document.getElementById("exampleInputEmail").style.borderColor = "#d1d3e2";
        document.getElementById("email-valid").style.display = "none";
    }
    if (mypin == "") {
        document.getElementById("exampleInputPassword").style.borderColor = "red";
        document.getElementById("button12").style.borderColor = "red";
        document.getElementById("pin-valid").style.display = "block";
        document.getElementById("pin-valid").textContent="Looks Bad!!";
        document.getElementById("pin-valid").classList = "text-danger";
    }
    else {
        document.getElementById("exampleInputPassword").style.borderColor = "#d1d3e2";
        document.getElementById("button12").style.borderColor = "#d1d3e2";
        document.getElementById("pin-valid").style.display = "none";
    }  
}

function showpassword(){
    var x = document.getElementById("exampleInputPassword");
    if (x.type == "password") {
        x.type = "text";
        document.getElementById("shape").classList="fa fa-eye";
    } else {
        x.type = "password";
        document.getElementById("shape").classList="fa fa-eye-slash";
    }
    
}