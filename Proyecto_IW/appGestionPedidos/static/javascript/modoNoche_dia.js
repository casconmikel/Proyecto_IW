if (localStorage.getItem('dato') === null) {
  // La variable no está almacenada, asignar un valor por primera vez
  var dato = 1;
 
  // Almacenar la variable en localStorage
  localStorage.setItem('dato', dato);
} else {
  // La variable ya está almacenada, recuperar su valor
  var dato = localStorage.getItem('dato');
  cambioModo();
}

const btn_modonoche = document.getElementById('modoOscuro');

btn_modonoche.addEventListener('click', function(){
  if (dato==0){
    dato += 1;
    cambioModo();
    localStorage.setItem('dato', dato);
  } 
  else {
    dato = 0;
    cambioModo();
    localStorage.setItem('dato', dato);
  }
    
})

function cambioModo (){
  
  if (dato==0) {
    document.body.classList.add('oscuro')
    
  } 
  else {
    document.body.classList.remove('oscuro')
  }
}

