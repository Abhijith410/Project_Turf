const btn3 = document.querySelector(".ratebutton3");
const post3 = document.querySelector(".post3");
const widget3 = document.querySelector(".star-widget3");
const editBtn3 = document.querySelector(".edit3");
btn3.onclick = ()=>{
  widget3.style.display = "block";
  post3.style.display = "block";
  editBtn3.onclick = ()=>{
    widget3.style.display = "block";
    post3.style.display = "none";
  }
  return false;
}