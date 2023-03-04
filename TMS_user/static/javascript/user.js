let names = [
    "Allianz Arena",
    "Emirates",
    "Bernabeu",
    "Wembley",
  ];
  //Sort names in ascending order
  let sortedNames = names.sort();
  
  //reference
  let input = document.getElementById("form1");
  
  //Execute function on keyup
  input.addEventListener("keyup", (e) => {
    //loop through above array
    //Initially remove all elements ( so if user erases a letter or adds new letter then clean previous outputs)
    removeElements();
    for (let i of sortedNames) {
      //convert input to lowercase and compare with each string
  
      if (
        i.toLowerCase().startsWith(input.value.toLowerCase()) &&
        input.value != ""
      ) {
        //create li element
        let listItem = document.createElement("li");
        //One common class name
        listItem.classList.add("list-items");
        listItem.style.cursor = "pointer";
        listItem.setAttribute("onclick", "displayNames('" + i + "')");
        //Display matched part in bold
        let word = "<b>" + i.substr(0, input.value.length) + "</b>";
        word += i.substr(input.value.length);
        //display the value in array
        listItem.innerHTML = word;
        document.querySelector(".list").appendChild(listItem);
      }
    }
  });
  function displayNames(value) {
    form1.value = value;
    removeElements();
  }
  function removeElements() {
    //clear all the item
    let items = document.querySelectorAll(".list-items");
    items.forEach((form1) => {
      form1.remove();
    });
  }
////////////////////////////////////////////////////////////////////////////

      const btn2 = document.querySelector(".ratebutton2");
      const post2 = document.querySelector(".post2");
      const widget2 = document.querySelector(".star-widget2");
      const editBtn2 = document.querySelector(".edit2");
      btn2.onclick = ()=>{
        widget2.style.display = "block";
        post2.style.display = "block";
        editBtn2.onclick = ()=>{
          widget2.style.display = "block";
          post2.style.display = "none";
        }
        return false;  
      }
      

      