let names = [
    "Allianz Arena",
    "Anfield",
    "Emirates",
    "Bernabeu",
    "Wembley",
  ];

  let sortedNames = names.sort();
  

  let input = document.getElementById("form1");
  
  input.addEventListener("keyup", (e) => {removeElements();
    for (let i of sortedNames) {
      if (
        i.toLowerCase().startsWith(input.value.toLowerCase()) &&
        input.value != ""
      ) {
        let listItem = document.createElement("li");
        listItem.classList.add("list-items");
        listItem.style.cursor = "pointer";
        listItem.setAttribute("onclick", "displayNames('" + i + "')");
        let word = "<b>" + i.substr(0, input.value.length) + "</b>";
        word += i.substr(input.value.length);
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
      

      