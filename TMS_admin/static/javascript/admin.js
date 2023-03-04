var adminname_error= document.getElementById('adminname');
var adminpass_error= document.getElementById('adminpass');

        a1 = 1;
        a2 = 1;
        function log_admin(){
            var adname1 = document.getElementById('adname').value;
            var adpass1 = document.getElementById('adpass').value;
    
            if(adname1 == ""){
                adminname_error.innerHTML = "Please enter name";
                a1 = 0;
            }
            else{
                    a1 = 1;   
            }  

            if(adpass1 == ""){
                adminpass_error.innerHTML = "Please enter password";
                a2 = 0;
            }
            else{
                    a2 = 1;
            }  
            
            if(a1 === 1 && a2 ===1){
                return true;
            }
            else{
                return false;
            }
        }      