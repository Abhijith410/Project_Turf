var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
};

var Manturfname_error= document.getElementById('Manturfname');
var Manturfloc_error= document.getElementById('Manturfloc');
var Manturfcost_error= document.getElementById('Manturfcost');
var manturfimg_error= document.getElementById('Manturfimg')

        mgedit1 = 1;
        mgedit2 = 1;
        mgedit3 = 1;
        mgedit4 = 1;
        function manturf(){
            var turfname1 = document.getElementById('turfname').value;
            var turfloc1 = document.getElementById('turfloc').value;
            var turfcost1 = document.getElementById('turfcost').value;
            var file1 = document.getElementById('file').value;
    
            if(turfname1 == ""){
                Manturfname_error.innerHTML = "Please enter Turf name";
                document.getElementById('turfname').style.borderColor = "red";
                mgedit1 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(turfname1) === false) {
                    document.getElementById('turfname').style.borderColor = "red";
                    Manturfname_error.innerHTML = "Please enter correct name";
                    mgedit1 = 0;
                } 
                else {
                    mgedit1 = 1;
                }
            }  

			if(turfloc1 == ""){
                Manturfloc_error.innerHTML = "Please enter turf location";
                document.getElementById('turfloc').style.borderColor = "red";
                mgedit2 = 0;
            }
            else{
                var regex = /^[a-zA-Z\s]+$/;
                if(regex.test(turfloc1) === false) {
                    document.getElementById('turfloc').style.borderColor = "red";
                    Manturfloc_error.innerHTML = "Please enter correct Location";
                    mgedit2 = 0;
                } 
                else {
                    mgedit2 = 1;
                }
            }


            if(turfcost1 == ""){
                Manturfcost_error.innerHTML = "Please enter Turf Description";
                document.getElementById('turfcost').style.borderColor = "red";
                mgedit3 = 0;
            }
            else{
                    mgedit3 = 1;
            }

			if(file1 == null){
                Manturfimg_error.innerHTML = "Please Select an image";
                mgedit4 = 0;
            }
			else{
				mgedit4 = 1;
			}
            
            if(mgedit1 === 1 && mgedit2 === 1 && mgedit3 === 1 && mgedit4 === 1){
                return true;  
            }
            else{
                return false;
            }
        }      