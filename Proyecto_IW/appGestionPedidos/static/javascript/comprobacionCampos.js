document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario").addEventListener('submit', validarFormulario); 
    document.getElementById("formulario2").addEventListener('submit', validarFormulario);
  });
  
  function validarFormulario(e) {
    
    var cif = document.getElementById('cif').value;
    var letraInicial = cif.charAt(0);
    var telefono = document.getElementById('tel').value;

    // comprobacion de que el primer caracter es una letra
    if (!/[ABCDEFGHJKLMNPQRSUVW]/.test(letraInicial)) {
        e.preventDefault();    
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El primer digito del CIF debe de ser una letra mayuscula.',
          })
      
      return false;
    }

    // comprobacion de que el cif tiene 9 caracteres
    if (cif.length !== 9) {
        e.preventDefault();
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'El cif debe de tener 9 caracteres.',
          })
    
      return false;
    }
    // comporbacion de que el cif no tiene ningun caracter extraño
    var caracteres = cif.substr(1,8);
    if (!/^\d+$/.test(caracteres)) {
      e.preventDefault();
      Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'El cif debe estar compuesto por numeros.',
        })
  
    return false;
    }
  
    
    if (telefono.length !== 9) {
        e.preventDefault();
        Swal.fire({
            icon: 'warning',
            title: 'Oops...',
            text: 'El telefono debe de tener 9 caracteres.',
          })
    
      return false;
    }
    var car_tel = cif.substr(0,8);
    if (!/^\d+$/.test(car_tel)) {
      e.preventDefault();
      Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'El telefono debe estar compuesto por números.',
        })
  
    return false;
    }
        
  }





    
  