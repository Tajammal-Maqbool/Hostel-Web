function checkid() {
    var myemail = document.getElementById("exampleInputEmail").value;
    var mypin = document.getElementById("exampleInputPassword").value;
    if (myemail == "") {
        document.getElementById("exampleInputEmail").style.borderColor = "red";
    } else {
        document.getElementById("exampleInputEmail").style.borderColor = "#d1d3e2";
    }
    if (mypin == "") {
        document.getElementById("exampleInputPassword").style.borderColor = "red";
    }
    else {
        document.getElementById("exampleInputPassword").style.borderColor = "#d1d3e2";
    }
}