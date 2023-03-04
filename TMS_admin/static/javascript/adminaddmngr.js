var admgmanagername_error= document.getElementById('admgmanagername');
var admgmanagermail_error= document.getElementById('admgmanagermail');
var admgmanagerphone_error= document.getElementById('admgmanagerphone');
var admgturfname_error= document.getElementById('admgturfname');
var admgturfloc_error= document.getElementById('admgturfloc');
var admgmanagerid_error= document.getElementById('admgmanagerid');
var admgmanagerpass_error= document.getElementById('admgmanagerpass');

        admg1 = 1;
        admg2 = 1;
        admg3 = 1;
        admg4 = 1;
        admg5 = 1;
        admg6 = 1;
        admg7 = 1;
        function addmanager(){
            var mgname1 = document.getElementById('mgname').value;
            var mgmail1 = document.getElementById('mgmail').value;
            var mgphone1 = document.getElementById('mgphone').value;
            var mgturfname1 = document.getElementById('mgturfname').value;
            var mgturfloc1 = document.getElementById('mgturfloc').value;
            var mgid1 = document.getElementById('mgid').value;
            var mgpassword1 = document.getElementById('mgpassword').value;
    
            if(mgname1 == ""){
                admgmanagername_error.innerHTML = "Please enter name";
                document.getElementById('mgname').style.borderColor = "red";
                admg1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(mgname1) === false) {
                    document.getElementById('mgname').style.borderColor = "red";
                    admgmanagername_error.innerHTML = "Please enter Proper name";
                    admg1 = 0;
                } 
                else {
                    admg1 = 1;
                }
            }  

            if(mgmail1 == ""){
                admgmanagermail_error.innerHTML = "Please enter E-mail";
                document.getElementById('mgmail').style.borderColor = "red";
                admg2 = 0;
            }
            else{
                var regex = /^\S+@\S+\.\S+$/;
                if(regex.test(mgmail1) === false) {
                    document.getElementById('mgmail').style.borderColor = "red";
                    admgmanagermail_error.innerHTML = "Please enter Proper E-mail";
                    admg2 = 0;
                } 
                else {
                    admg2 = 1;
                }
            }  
            if(mgphone1 == ""){
                admgmanagerphone_error.innerHTML = "Please enter contact number";
                document.getElementById('mgphone').style.borderColor = "red";
                admg3 = 0;
            }
            else{
                var regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
                if(regex.test(mgphone1) === false){
                    document.getElementById('mgphone').style.borderColor = "red";
                    admgmanagerphone_error.innerHTML = "Please enter proper contact number";
                    admg3 = 0; 
                }
                else{
                    admg3 = 1;
                }
            }

            if(mgturfname1 == ""){
                admgturfname_error.innerHTML = "Please enter Turf Name";
                document.getElementById('mgturfname').style.borderColor = "red";
                admg4 = 0;
            }
            else{
                var regex = /^[A-Za-z][A-Za-z0-9_]{3,29}$/;
                if(regex.test(mgturfname1) === false){
                    document.getElementById('mgturfname').style.borderColor = "red";
                    admgturfname_error.innerHTML = "Please enter correct Turf name";
                    admg4 = 0; 
                }
                else{
                    admg4 = 1;
                }
            }

            if(mgturfloc1 == ""){
                admgturfloc_error.innerHTML = "Please enter turf location";
                document.getElementById('mgturfloc').style.borderColor = "red";
                admg5 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(mgturfloc1) === false) {
                    document.getElementById('mgturfloc').style.borderColor = "red";
                    admgturfloc_error.innerHTML = "Please enter correct Location";
                    admg5 = 0;
                } 
                else {
                    admg5 = 1;
                }
            }

            if(mgid1 == ""){
                admgmanagerid_error.innerHTML = "Please enter Manager ID";
                document.getElementById('mgid').style.borderColor = "red";
                admg6 = 0;
            }
            else{
                var regex = /^[A-Za-z0-9_]{5,29}$/;
                if(regex.test(mgid1) === false) {
                    document.getElementById('mgid').style.borderColor = "red";
                    admgmanagerid_error.innerHTML = "Please enter proper Manager ID";
                    admg6 = 0;
                } 
                else {
                    admg6 = 1;
                }
            }

            if(mgpassword1 == ""){
                admgmanagerpass_error.innerHTML = "Please enter Manager Password";
                document.getElementById('mgpassword').style.borderColor = "red";
                admg7 = 0;
            }
            else{
                var regex = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
                if(regex.test(mgpassword1) === false) {
                    document.getElementById('mgpassword').style.borderColor = "red";
                    admgmanagerpass_error.innerHTML = "Please enter proper password";
                    admg7 = 0;
                } 
                else {
                    admg7 = 1;
                }
            }

            if(admg1 == 1 && admg2 == 1 && admg3 == 1 && admg4 == 1 && admg5 == 1 && admg6 == 1 && admg7 == 1){
                return true;  
            }
            else{
                return false;
            }
        }   