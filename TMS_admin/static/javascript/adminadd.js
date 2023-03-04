var adturfmanagername_error= document.getElementById('adturfmanagername');
var adturfname_error= document.getElementById('adturfname');
var adturfloc_error= document.getElementById('adturfloc');
var adturfcost_error= document.getElementById('adturfcost');

        adtf1 = 1;
        adtf2 = 1;
        adtf3 = 1;
        adtf4 = 1;
        function addturf(){
            var managername1 = document.getElementById('managername').value;
            var turfname1 = document.getElementById('turfname').value;
            var turflocation1 = document.getElementById('turflocation').value;
            var turfcost1 = document.getElementById('turfcost').value;
    
            if(managername1 == ""){
                adturfmanagername_error.innerHTML = "Please enter name";
                document.getElementById('managername').style.borderColor = "red";
                adtf1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(managername1) === false) {
                    document.getElementById('managername').style.borderColor = "red";
                    adturfmanagername_error.innerHTML = "Please enter a Proper name";
                    adtf1 = 0;
                } 
                else {
                    adtf1 = 1;
                }
            }  

            if(turfname1 == ""){
                adturfname_error.innerHTML = "Please enter Turf Name";
                document.getElementById('turfname').style.borderColor = "red";
                adtf2 = 0;
            }
            else{
                var regex = /^[A-Za-z][A-Za-z0-9_]{3,29}$/;
                if(regex.test(turfname1) === false){
                    document.getElementById('turfname').style.borderColor = "red";
                    adturfname_error.innerHTML = "Please enter Proper Turf name";
                    adtf2 = 0; 
                }
                else{
                    adtf2 = 1;
                }
            }

            if(turflocation1 == ""){
                adturfloc_error.innerHTML = "Please enter turf location";
                document.getElementById('turflocation').style.borderColor = "red";
                adtf3 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(turflocation1) === false) {
                    document.getElementById('turflocation').style.borderColor = "red";
                    adturfloc_error.innerHTML = "Please enter correct Location";
                    adtf3 = 0;
                } 
                else {
                    adtf3 = 1;
                }
            }

            if(turfcost1 == ""){
                adturfcost_error.innerHTML = "Please enter turf cost";
                document.getElementById('turfcost').style.borderColor = "red";
                adtf4 = 0;
            }
            else{
                var regex = /^(\d*([.,](?=\d{3}))?\d+)+((?!\2)[.,]\d\d)?$/;
                if(regex.test(turfcost1) === false) {
                    document.getElementById('turfcost').style.borderColor = "red";
                    adturfcost_error.innerHTML = "Please enter precise cost";
                    adtf4 = 0;
                } 
                else {
                    adtf4 = 1;
                }
            }

            if(adtf1 === 1 && adtf2 === 1 && adtf3 === 1 && adtf4 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      
///////////////////////////////////////////////////



