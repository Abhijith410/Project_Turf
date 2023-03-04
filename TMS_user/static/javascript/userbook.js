var userbookname_error= document.getElementById('userbookname');
var userbookcontact_error= document.getElementById('userbookcontact');
var userbookdate_error= document.getElementById('userbookdate');
var userbooktime_error= document.getElementById('userbooktime');

        usbook1 = 1;
        usbook2 = 1;
        usbook3 = 1;
        usbook4 = 1;
        function userbooking(){
            var user_name1 = document.getElementById('user_name').value;
            var user_contact1 = document.getElementById('user_contact').value;
            var user_date1 = document.getElementById('user_date').value;
            var user_time1 = document.getElementById('user_time').value;
    
            if(user_name1 == ""){
                userbookname_error.innerHTML = "Please enter name";
                document.getElementById('user_name').style.borderColor = "red";
                usbook1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(user_name1) === false) {
                    document.getElementById('user_name').style.borderColor = "red";
                    userbookname_error.innerHTML = "Please enter correct name";
                    usbook1 = 0;
                } 
                else {
                    usbook1 = 1;
                }
            }  
  
            if(user_contact1 == ""){
                userbookcontact_error.innerHTML = "Please enter contact number";
                document.getElementById('user_contact').style.borderColor = "red";
                usbook2 = 0;
            }
            else{
                var regex = /^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$/;
                if(regex.test(user_contact1) === false){
                    document.getElementById('user_contact').style.borderColor = "red";
                    userbookcontact_error.innerHTML = "Please enter proper contact number";
                    usbook2 = 0; 
                }
                else{
                    usbook2 = 1;
                }
            }

            if(user_date1 == ""){
                userbookdate_error.innerHTML = "Please select date";
                document.getElementById('user_date').style.borderColor = "red";
                usbook3 = 0;
            }
            else{
                usbook3 = 1;
            }
            

            if(user_time1 == ""){
                userbooktime_error.innerHTML = "Please enter booking time in the format(HH:MM-HH:MM AM/PM)";
                document.getElementById('user_time').style.borderColor = "red";
                usbook4 = 0;
            }
            else{
                var regex = /^\(?([1-9]|0[1-9]|1[0-2]):([0-5][0-9])\)?[-. ]?([1-9]|0[1-9]|1[0-2]):([0-5][0-9])[\-\s]?((AM)|(PM))$/g;
                if(regex.test(user_time1) === false) {
                    document.getElementById('user_time').style.borderColor = "red";
                    userbooktime_error.innerHTML = "Please enter time properly (eg 08:00-09:00 PM)";
                    usbook4 = 0;
                } 
                else {
                    usbook4 = 1;
                }
            }

            if(usbook1 === 1 && usbook2 === 1 && usbook3 === 1 && usbook4 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      