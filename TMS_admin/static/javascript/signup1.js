var name_error = document.getElementById('namerror');
var email_error_ = document.getElementById('emailerror_');
var phone_error = document.getElementById('phonerror');
var user_error = document.getElementById('usererror_');
var pass_error_ = document.getElementById('passerror_');
var conf_error = document.getElementById('conferror');

        reguser1 = 1;
        reguser2 = 1;
        reguser3 = 1;
        reguser4 = 1;
        reguser5 = 1;
        reguser6 = 1;
        function reg_validate(){
            var name = document.getElementById('Name').value;
            var mail = document.getElementById('email').value;
            var cnum = document.getElementById('Phonenumber').value;
            var usr = document.getElementById('user_name').value;
            var pwd = document.getElementById('pass_word').value;
            var conf = document.getElementById('repeat password').value;
  
            if(name == ""){
                document.getElementById('Name').style.borderColor = "red";
                name_error.innerHTML = "Please enter your name";
                reguser1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(name) === false) {
                    document.getElementById('Name').style.borderColor = "red";
                    name_error.innerHTML = "Please enter a valid name";
                    reguser1 = 0;
                } 
                else {
                    reguser1 = 1;
                }
            }    

            if(mail == ""){
                document.getElementById('email').style.borderColor = "red";
                email_error_.innerHTML = "Please enter email address";
                reguser2 = 0;
            }
            else{
                var regex = /^\S+@\S+\.\S+$/;
                if(regex.test(mail) === false) {
                    document.getElementById('email').style.borderColor = "red";
                    email_error_.innerHTML = "Please enter a valid Email address";
                    reguser2 = 0;
                } 
                else {
                    reguser2 = 1;
                }
            }    
            
            if(cnum == ""){
                document.getElementById('Phonenumber').style.borderColor = "red";
                phone_error.innerHTML = "Please enter mobile number";
                reguser3 = 0;
            }
            else{
                var regex = /^[1-9]\d{9}$/;
                if(regex.test(cnum) === false){
                    document.getElementById('Phonenumber').style.borderColor = "red";
                    phone_error.innerHTML = "Please enter a valid 10 digit number";
                    reguser3 = 0;
                }
                else{
                    reguser3 = 1;
                }
            }
            
            if(usr == ""){
                document.getElementById('user_name').style.borderColor = "red";
                user_error.innerHTML = "Please enter a username";
                reguser4 = 0;
            }
            else{
                var regex = /^[A-Za-z][A-Za-z0-9_]{7,29}$/;
                if(regex.test(usr) === false){
                    document.getElementById('user_name').style.borderColor = "red";
                    user_error.innerHTML = "Username should start with an alphabet(min 7 characters)";
                    reguser4 = 0;
                }
                else{
                    reguser4 = 1;
                }
            }
            
            if(pwd == ""){
                document.getElementById('pass_word').style.borderColor = "red";
                pass_error_.innerHTML = "Please enter Password";
                reguser5 = 0;
            }
            else{
                var regex = /^(?=.*\d)(?=.*[a-z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,100}$/;
                if(regex.test(pwd) === false) {
                    document.getElementById('pass_word').style.borderColor = "red";
                    pass_error_.innerHTML = "Please enter a valid password(min 8 characters-use letters, numbers, special characters)";
                    reguser5 = 0;
                } 
                else {
                    reguser5 = 1;
                }
            }
            
            if(conf == ""){
                document.getElementById('repeat password').style.borderColor = "red";
                conf_error.innerHTML = "Please re-enter your password";
                reguser6 = 0;
            }
            else{
                if(conf !== pwd ){
                    document.getElementById('repeat password').style.borderColor = "red";
                    conf_error.innerHTML = "Passwords do not match";
                    reguser6 = 0;
                }
                else{
                    reguser6 = 1;
                }
            }

            if(reguser1 === 1 && reguser2 === 1 && reguser3 === 1 && reguser4 === 1 && reguser5 === 1 && reguser6 === 1){
                return true;
            }
            else{
                return false;
            }
        }