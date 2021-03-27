function create(){
    var fname=document.getElementById("exampleFirstName").value;
    var lname=document.getElementById("exampleLastName").value;
    var email=document.getElementById("exampleInputEmail").value;
    var password=document.getElementById("exampleInputPassword").value;
    if(fname!="" && lname!="" && email!="" && password!=""){
        document.getElementById("createaccount").href="/createAccount"
    }else{
        if(fname==""){
            document.getElementById("exampleFirstName").style.borderColor="red";
        }else{
            document.getElementById("exampleFirstName").style.borderColor="#d1d3e2";
        }
        if(lname==""){
            document.getElementById("exampleLastName").style.borderColor="red";
        }
        else{
            document.getElementById("exampleLastName").style.borderColor="#d1d3e2";
        }
        if(email==""){
            document.getElementById("exampleInputEmail").style.borderColor="red";
        }
        else{
            document.getElementById("exampleInputEmail").style.borderColor="#d1d3e2";
        }
        if(password==""){
            document.getElementById("exampleInputPassword").style.borderColor="red";
        }
        else{
            document.getElementById("exampleInputPassword").style.borderColor="#d1d3e2";
        }
    }
}