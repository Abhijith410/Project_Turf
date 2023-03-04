var ufeedname_error= document.getElementById('ufeedname');
var ufeedphone_error= document.getElementById('ufeedphone');
var ufeedemail_error= document.getElementById('ufeedemail');
var ufeeddesc_error= document.getElementById('ufeeddesc');

        userfeed1 = 1;
        userfeed2 = 1;
        userfeed3 = 1;
        userfeed4 = 1;
        function userfeedback(){
            var feedName1 = document.getElementById('feedname').value;
            var feedemail1 = document.getElementById('feedemail').value;
            var feedphone1 = document.getElementById('feedphone').value;
            var feeddesc1 = document.getElementById('feeddesc').value;
    
            if(feedName1 == ""){
                document.getElementById('feedname').style.borderColor = "red";
                ufeedname_error.innerHTML = "Please enter full name";
                userfeed1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(feedName1) === false) {
                    document.getElementById('feedname').style.borderColor = "red";
                    ufeedname_error.innerHTML = "Please enter correct name";
                    userfeed1 = 0;
                } 
                else {
                    userfeed1 = 1;
                }
            }  

            if(feedemail1 == ""){
                ufeedemail_error.innerHTML = "Please enter E-mail";
                document.getElementById('feedemail').style.borderColor = "red";
                userfeed2 = 0;
            }
            else{
                var regex = /^\S+@\S+\.\S+$/;
                if(regex.test(feedemail1) === false) {
                    document.getElementById('feedemail').style.borderColor = "red";
                    ufeedemail_error.innerHTML = "Please enter correct E-mail";
                    userfeed2 = 0;
                } 
                else {
                    userfeed2 = 1;
                }
            }  
            
            if(feedphone1 == ""){
                ufeedphone_error.innerHTML = "Please enter phone number";
                document.getElementById('feedphone').style.borderColor = "red";
                userfeed3 = 0;
            }
            else{
                var regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
                if(regex.test(feedphone1) === false){
                    document.getElementById('feedphone').style.borderColor = "red";
                    ufeedphone_error.innerHTML = "Please enter correct phone number";
                    userfeed3 = 0; 
                }
                else{
                    userfeed3 = 1;
                }
            }

            if(feeddesc1 == ""){
                ufeeddesc_error.innerHTML = "Please enter any message";
                document.getElementById('feeddesc').style.borderColor = "red";
                userfeed4 = 0;
            }
            else{
                userfeed4 = 1;
            }

            if(userfeed1 === 1 && userfeed2 === 1 && userfeed3 === 1 && userfeed4 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      