
//Grupo 19 todas las notas son guias para no perdernos lo que se hizo en cada parte//

document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault(); //evito que se mande automaticamente el formulario

    var camposIncompletos = validarFormulario(); //validamos todos los campos obligatorios
    if (camposIncompletos.length === 0) { //si un campo esta vacio o con 0 caracteres se considerá incompleto
    if (confirm('¿Está seguro de que desea enviar el formulario?')) { //cuadro que pedira confirmar el envio al usuario
        this.submit(); //si esta OK envia el formulario
        alert('Formulario enviado correctamente!');
        window.location.href = "../index.html"; //aqui volvería al index tras enviar el formulario
        }
    } else {
        // Si hay campos incompletos, mostrar un mensaje de error
        alert('Por favor complete los siguientes campos: \n\n' + camposIncompletos.join('\n'));
    }
});

function validarFormulario() {
    //comenzamos con la zona de variables//
    //buscamos los elementos en el html por su id definido//

    var camposIncompletos = [];

    var nombre = document.getElementById('nombre').value.trim();
    var apellido = document.getElementById('apellido').value.trim();
    var email = document.getElementById('email').value.trim();
    var pais = document.getElementById('pais').value;
    var ciudad = document.getElementById('ciudad').value;
    var comentarios = document.getElementById('comentarios').value.trim();
    var deseaOfertas = document.getElementById('btn-switch').checked;

    //validación de todos los campos

    if (nombre === '') { 
        camposIncompletos.push('Ingrese su nombre');
    }

    if (apellido === '') { 
        camposIncompletos.push('Ingrese su apellido');
    }

    if (email === '') { 
        camposIncompletos.push('Ingrese su e-mail');
    } else if (!validarEmail(email)) {
        return false;
    }

    if (pais === 'Seleccione país') { 
        camposIncompletos.push('Seleccione país');
    }

    if (ciudad === 'Seleccione ciudad') { 
        camposIncompletos.push('Seleccione ciudad');
    }

    if (comentarios === '') { 
        camposIncompletos.push('Dejanos tu omentario');
    }

    if (!deseaOfertas) { 
        camposIncompletos.push('Deseo recibir ofertas y novedades');
    }
    return camposIncompletos; //vuelvo hacia el var camposIncompletos para revisar si todo esta completo ahora
}

function validarEmail(email) { // validar email
    var regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+$/;
    return regex.test(email);
}