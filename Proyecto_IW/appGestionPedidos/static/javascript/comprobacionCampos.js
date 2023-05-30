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
    if (telefono.length !== 9) {
        e.preventDefault();
        Swal.fire({
            icon: 'warning',
            title: 'Oops...',
            text: 'El telefono debe de tener 9 caracteres.',
          })
    
      return false;
    }
        
  }





    
  