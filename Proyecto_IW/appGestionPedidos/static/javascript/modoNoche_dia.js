function light(){
  document.getElementById('page').classList.add('day-mode');
  document.getElementById('id-moon').classList.remove('active');
  document.getElementById('id-sun').classList.add('active');
  localStorage.setItem("dark-mode", "false");
}

function dark(){
  document.getElementById('page').classList.remove('day-mode');
  document.getElementById('id-sun').classList.remove('active');
  document.getElementById('id-moon').classList.add('active');
  localStorage.setItem("dark-mode", "true");
}

let sun = document.getElementById('id-sun');
sun.addEventListener('click', light);
let moon = document.getElementById('id-moon');
moon.addEventListener('click', dark);

if (localStorage.getItem("dark-mode")=="true") {
  dark();
}
else{
  light();
}