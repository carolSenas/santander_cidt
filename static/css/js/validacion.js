    function validarFormulario() {
        var username = document.getElementById("username-a30d").value;
        var password = document.getElementById("password-a30d").value;

        if (username === "" || password === "") {
            alert("Por favor, completa todos los campos obligatorios.");
            return false; // Evita que el formulario se envíe
        }

        // Puedes agregar más validaciones aquí si es necesario

        return true; // Envía el formulario si todas las validaciones son exitosas
    }
