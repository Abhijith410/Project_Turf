var rname_error= document.getElementById('rname');
var rmail_error= document.getElementById('rmail');
var rnumber_error= document.getElementById('rnumber');
var rturf_error= document.getElementById('rturf');
var rlocation_error= document.getElementById('rlocation');

        treq1 = 1;
        treq2 = 1;
        treq3 = 1;
        treq4 = 1;
        treq5 = 1;
        function trequest(){
            var requestname1 = document.getElementById('requestname').value;
            var requestmail1 = document.getElementById('requestmail').value;
            var requestnumber1 = document.getElementById('requestnumber').value;
            var requestturf1 = document.getElementById('requestturf').value;
            var requestlocation1 = document.getElementById('requestlocation').value;
    
            if(requestname1 == ""){
                rname_error.innerHTML = "Please enter name";
                treq1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(requestname1) === false) {
                    document.getElementById('requestname').style.borderColor = "red";
                    rname_error.innerHTML = "Please enter correct name";
                    treq1 = 0;
                } 
                else {
                    treq1 = 1;
                }
            }  

            if(requestmail1 == ""){
                rmail_error.innerHTML = "Please enter E-mail";
                treq2 = 0;
            }
            else{
                var regex = /^\S+@\S+\.\S+$/;
                if(regex.test(requestmail1) === false) {
                    document.getElementById('requestmail').style.borderColor = "red";
                    rmail_error.innerHTML = "Please enter correct E-mail";
                    treq2 = 0;
                } 
                else {
                    treq2 = 1;
                }
            }  
            if(requestnumber1 == ""){
                rnumber_error.innerHTML = "Please enter contact number";
                treq3 = 0;
            }
            else{
                var regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
                if(regex.test(requestnumber1) === false){
                    document.getElementById('requestnumber').style.borderColor = "red";
                    rnumber_error.innerHTML = "Please enter correct contact number";
                    treq3 = 0; 
                }
                else{
                    treq3 = 1;
                }
            }

            if(requestturf1 == ""){
                rturf_error.innerHTML = "Please enter Turf Name";
                treq4 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(requestturf1) === false){
                    document.getElementById('requestturf').style.borderColor = "red";
                    rturf_error.innerHTML = "Please enter correct Turf name";
                    treq4 = 0; 
                }
                else{
                    treq4 = 1;
                }
            }

            if(requestlocation1 == ""){
                rlocation_error.innerHTML = "Please enter turf location";
                treq5 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(requestlocation1) === false) {
                    document.getElementById('requestlocation').style.borderColor = "red";
                    rlocation_error.innerHTML = "Please enter correct Location";
                    treq5 = 0;
                } 
                else {
                    treq5 = 1;
                }
            }

            if(treq1 === 1 && treq2 === 1 && treq3 === 1 && treq4 === 1 && treq5 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      