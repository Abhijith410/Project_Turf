var userbookname_error= document.getElementById('userbookname');
var userbookcontact_error= document.getElementById('userbookcontact');
var userbookdate_error= document.getElementById('userbookdate');
var userbooktimefrom_error= document.getElementById('userbooktimefrom');
var userbooktimeto_error= document.getElementById('userbooktimeto');

        usbook1 = 1;
        usbook2 = 1;
        usbook3 = 1;
        usbook4 = 1;
        usbook5 = 1;
        function userbooking(){
            var user_name1 = document.getElementById('user_name').value;
            var user_contact1 = document.getElementById('user_contact').value;
            var user_date1 = document.getElementById('user_date').value;

            
            const getSeconds = s => s.split(":").reduce((acc, curr) => acc * 60 + +curr, 0);
            var seconds1 = getSeconds(document.getElementById("user_timefrom").value);
            var seconds2 = getSeconds(document.getElementById("user_timeto").value);
            var res = Math.abs(seconds2 - seconds1);

            var hours = Math.floor(res / 3600);
            // var minutes = Math.floor(res % 3600 / 60);
            // var seconds = res % 60;
    
            var x = hours ;
            document.getElementById('user_totalcost').value = x * document.getElementById('usercost').value;

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
            

            if(seconds1 == ""){
                userbooktimefrom_error.innerHTML = "Please select start time";
                document.getElementById('user_timefrom').style.borderColor = "red";
                usbook4 = 0;
            }
            else{
                    usbook4 = 1;
            }

            if(seconds2 == ""){
                userbooktimeto_error.innerHTML = "Please select end time";
                document.getElementById('user_timeto').style.borderColor = "red";
                usbook5 = 0;
            }
            else{
                    usbook5 = 1;
            }

            if(usbook1 === 1 && usbook2 === 1 && usbook3 === 1 && usbook4 === 1 && usbook5 === 1){
                
                return true;  
            }
            else{
                return false;
            }
        }      

           