function createcomplain() {
    var sms = document.getElementById("exampleInput").value;
    if (sms != "") {
        document.getElementById("textcomplain").textContent = sms;
        document.getElementById("textcomplain").classList = "btn-info btn-user text-white";
        document.getElementById('check').style.display = "block";
    }
    else{
        document.getElementById("exampleInput").style.borderColor="red";
    }
};
function removeword(){
    var sms = document.getElementById("exampleInput").value;
    if(sms!=""){
        sms = sms.slice(0, -1);
        document.getElementById("exampleInput").value=sms;
    }
}
