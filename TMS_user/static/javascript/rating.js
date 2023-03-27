var name_error= document.getElementById('nameerror');
var contact_error= document.getElementById('contacterror');
var message_error= document.getElementById('messageerror');

        userrev1 = 1;
        userrev2 = 1;
        userrev3 = 1;
        function userreview(){
            var name = document.getElementById('message-text name').value;
            var contact = document.getElementById('message-text contact').value;
            var message = document.getElementById('message-text message').value;
    
            if(name == ""){
                document.getElementById('message-text name').style.borderColor = "red";
                document.getElementById('message-text name').style.borderWidth = "1.5px";
                name_error.innerHTML = "Please enter your name";
                userrev1 = 0;
            }
            else{
                userrev1 = 1;
            }   
            
            if(contact == ""){
                contact_error.innerHTML = "Please enter phone number";
                document.getElementById('message-text contact').style.borderColor = "red";
                document.getElementById('message-text contact').style.borderWidth = "1.5px";
                userrev2 = 0;
            }
            else{
                userrev2 = 1;
            }

            if(message == ""){
                message_error.innerHTML = "Please enter any message";
                document.getElementById('message-text message').style.borderColor = "red";
                document.getElementById('message-text message').style.borderWidth = "1.5px";
                userrev3 = 0;
            }
            else{
                userrev3 = 1;
            }

            if(userrev1 === 1 && userrev2 === 1 && userrev3 === 1){
                return true;  
            }
            else{
                return false;
            }
        } 