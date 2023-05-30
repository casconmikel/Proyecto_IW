const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

(function () {
    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function (e) {
            
            e.preventDefault();
            Swal.fire({
                title: '¿Estas seguro de que quieres borrar el registro?',
                text: "¡No lo podras recuperar!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, Borrar!'
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location = this.href;

                }
                
            })

        })
    })
})();

