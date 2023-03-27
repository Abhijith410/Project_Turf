var usererror= document.getElementById('usererror');
var pass_error= document.getElementById('passerror');
var mngr_error = document.getElementById('mngrerror');
var mngr_passerror = document.getElementById('mngrpasserror');

        userlog1 = 1;
        userlog2 = 1;
        function log_user(){
            var user = document.getElementById('username').value;
            var pswd = document.getElementById('password').value;

    
            if(user == ""){
                document.getElementById('username').style.borderColor = "red";
                usererror.innerHTML = "Please enter username";
                userlog1 = 0;
            }
            else{
                userlog1 = 1;
            } 
               
            if(pswd == ""){
                document.getElementById('password').style.borderColor = "red";
                pass_error.innerHTML = "Please enter Password";
                userlog2 = 0;
            }
            else{
                userlog2 = 1;
            }
           
            if(userlog1 === 1 && userlog2 === 1){
                return true;
            }
            else{
                return false;
            }
        }
        
        mglog1 = 1;
        mglog2 = 1;
        function log_manager(){
            var mngr_id = document.getElementById('mngrid').value;
            var mngr_password = document.getElementById('mngrpassword').value;
            if(mngr_id == ""){
                document.getElementById('mngrid').style.borderColor = "red";
                mngr_error.innerHTML = "Please enter Manager ID";
                mglog1 = 0;
            }
            else{
                    mglog1 = 1;
            }
            
            
            if(mngr_password == ""){
                document.getElementById('mngrpassword').style.borderColor = "red";
                mngr_passerror.innerHTML = "Please enter Password";
                mglog2 = 0;
            }
            else{
                mglog2 = 1;
            }
            if(mglog1 === 1 && mglog2 === 1){
                return true;
            }
            else {
                return false;
            }
        }    
        
        
        const rmCheck = document.getElementById("rememberMe"),
        emailInput = document.getElementById("mngrid");

        if (localStorage.checkbox && localStorage.checkbox !== "") {
            rmCheck.setAttribute("checked", "checked");
            emailInput.value = localStorage.username;
        } else {
            rmCheck.removeAttribute("checked");
            emailInput.value = "";
        }

        function lsRememberMe() {
            if (rmCheck.checked && emailInput.value !== "") {
                localStorage.username = emailInput.value;
                localStorage.checkbox = rmCheck.value;
            } else {
                localStorage.username = "";
                localStorage.checkbox = "";
            }
        }        