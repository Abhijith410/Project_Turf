var userfullname_error= document.getElementById('userfullname');
var useremail_error= document.getElementById('useremail');
var userphone_error= document.getElementById('userphone');
var useroldpass_error= document.getElementById('useroldpass');
var usernewpass_error= document.getElementById('usernewpass');

        uspr1 = 1;
        uspr2 = 1;
        uspr3 = 1;
        uspr4 = 1;
        uspr5 = 1;
        function userprofile(){
            var ufullName1 = document.getElementById('ufullName').value;
            var ueMail1 = document.getElementById('ueMail').value;
            var uphone1 = document.getElementById('uphone').value;
            var uoldpass1 = document.getElementById('uoldpass').value;
            var unewpass1 = document.getElementById('unewpass').value;
    
            if(ufullName1 == ""){
                document.getElementById('ufullName').style.borderColor = "red";
                userfullname_error.innerHTML = "Please enter full name";
                uspr1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(ufullName1) === false) {
                    document.getElementById('ufullName').style.borderColor = "red";
                    userfullname_error.innerHTML = "Please enter correct name";
                    uspr1 = 0;
                } 
                else {
                    uspr1 = 1;
                }
            }  

            if(ueMail1 == ""){
                useremail_error.innerHTML = "Please enter E-mail";
                document.getElementById('ueMail').style.borderColor = "red";
                uspr2 = 0;
            }
            else{
                var regex = /^\S+@\S+\.\S+$/;
                if(regex.test(ueMail1) === false) {
                    document.getElementById('ueMail').style.borderColor = "red";
                    useremail_error.innerHTML = "Please enter correct E-mail";
                    uspr2 = 0;
                } 
                else {
                    uspr2 = 1;
                }
            }  
            if(uphone1 == ""){
                userphone_error.innerHTML = "Please enter phone number";
                document.getElementById('uphone').style.borderColor = "red";
                uspr3 = 0;
            }
            else{
                var regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
                if(regex.test(uphone1) === false){
                    document.getElementById('uphone').style.borderColor = "red";
                    userphone_error.innerHTML = "Please enter correct phone number";
                    uspr3 = 0; 
                }
                else{
                    uspr3 = 1;
                }
            }

            if(uoldpass1 == ""){
                useroldpass_error.innerHTML = "Please enter your username";
                document.getElementById('uoldpass').style.borderColor = "red";
                uspr4 = 0;
            }
            else{
                    uspr4 = 1;
            }

            if(unewpass1 == ""){
                usernewpass_error.innerHTML = "Please enter new password";
                document.getElementById('unewpass').style.borderColor = "red";
                uspr5 = 0;
            }
            else{
                var regex = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
                if(regex.test(unewpass1) === false) {
                    document.getElementById('unewpass').style.borderColor = "red";
                    usernewpass_error.innerHTML = "Please enter within the format-password should contain atleast one number and one special character";
                    uspr5 = 0;
                } 
                else {
                    uspr5 = 1;
                }
            }

            if(uspr1 === 1 && uspr2 === 1 && uspr3 === 1 && uspr4 === 1 && uspr5 === 1){
                return true;  
            }
            else{
                return false;
            }
        }  
            