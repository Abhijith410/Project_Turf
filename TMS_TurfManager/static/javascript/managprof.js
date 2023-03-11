var mgfullname_error= document.getElementById('mgfullname');
var mgemail_error= document.getElementById('mgemail');
var mgphone_error= document.getElementById('mgphone');
var mgoldpass_error= document.getElementById('mgoldpass');
var mgnewpass_error= document.getElementById('mgnewpass');

        mgprofile1 = 1;
        mgprofile2 = 1;
        mgprofile3 = 1;
        mgprofile4 = 1;
        mgprofile5 = 1;
        function managerprofile(){
            var fullName1 = document.getElementById('fullName').value;
            var eMail1 = document.getElementById('eMail').value;
            var phone1 = document.getElementById('phone').value;
            var oldpass1 = document.getElementById('oldpass').value;
            var newpass1 = document.getElementById('newpass').value;
    
            if(fullName1 == ""){
                document.getElementById('fullName').style.borderColor = "red";
                mgfullname_error.innerHTML = "Please enter full name";
                mgprofile1 = 0;
            }
            else{
                    mgprofile1 = 1;
            }  

            if(eMail1 == ""){
                mgemail_error.innerHTML = "Please enter E-mail";
                document.getElementById('eMail').style.borderColor = "red";
                mgprofile2 = 0;
            }
            else{
                    mgprofile2 = 1;
            }  
            if(phone1 == ""){
                mgphone_error.innerHTML = "Please enter phone number";
                document.getElementById('phone').style.borderColor = "red";
                mgprofile3 = 0;
            }
            else{
                    mgprofile3 = 1;
            }

            if(oldpass1 == ""){
                mgoldpass_error.innerHTML = "Please enter Username";
                document.getElementById('oldpass').style.borderColor = "red";
                mgprofile4 = 0;
            }
            else{
                    mgprofile4 = 1;
            }

            if(newpass1 == ""){
                mgnewpass_error.innerHTML = "Please enter new password";
                document.getElementById('newpass').style.borderColor = "red";
                mgprofile5 = 0;
            }
            else{
                    mgprofile5 = 1;
            }

            if(mgprofile1 === 1 && mgprofile2 === 1 && mgprofile3 === 1 && mgprofile4 === 1 && mgprofile5 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      