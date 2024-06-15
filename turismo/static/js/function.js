$(document).ready(function() {
    $("#trabajoForm").on("submit", function(event) {
        event.preventDefault();

        let isValid = true;

        const user = $("#User").val();
        const clave = $("#Clave").val();

        if (clave.length < 8) {
            alert("La clave debe tener mínimo 8 caracteres");
            isValid = false;
        }

        if (user.length < 3 || user.length > 20) {
            alert("El Nombre de usuario debe tener entre 3 y 20 caracteres.");
            isValid = false;
        }

        if (isValid) {
            alert("Usuario y clave correctas")
            this.submit();
        }
    }); 
});