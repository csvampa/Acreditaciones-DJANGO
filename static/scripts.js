window.addEventListener('DOMContentLoaded', () => {

// Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
            document.body.classList.toggle('sb-sidenav-toggled');
        }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

// MENU DESPLEGABLE
    // Obtén una referencia al elemento que desencadenará el menú desplegable
    const dropdownToggle = document.getElementById('navbarDropdown');

    // Escucha el evento clic en el enlace del usuario
    dropdownToggle.addEventListener('click', function (event) {
        // Previene la acción predeterminada del enlace
        event.preventDefault();

        // Encuentra el menú desplegable asociado
        const dropdownMenu = document.querySelector('#navbarDropdown + ul.dropdown-menu');

        // Abre o cierra el menú desplegable
        if (dropdownMenu) {
            if (dropdownMenu.style.display === 'block') {
                dropdownMenu.style.display = 'none';
            } else {
                dropdownMenu.style.display = 'block';
            }
        }
    })

})

// BUSCADOR
document.addEventListener('DOMContentLoaded', function() {

    const allRows = document.querySelectorAll('#miTabla tbody tr');

    function searchDatabase() {
        const searchInput = document.getElementById('searchInput');
        const searchTerm = searchInput.value.trim().toLowerCase();

        // Iterar sobre las filas y mostrar/ocultar según la coincidencia con el término de búsqueda
        allRows.forEach(row => {
            const dniCell = row.querySelector('td:nth-child(3)');

            if (dniCell) {
                const dni = dniCell.textContent.trim();
                const rowData = row.textContent.trim().toLowerCase();

                if (rowData.includes(searchTerm) || dni.includes(searchTerm)) {
                    row.style.display = 'table-row';
                } else {
                    row.style.display = 'none';
                }
            }

            // const rowData = row.textContent.trim().toLowerCase();
            // const rowDataNumber = parseFloat(rowData);

            // // Verificar si el término de búsqueda es un número y comienza con el número ingresado
            // if (!isNaN(searchTerm) && (rowDataNumber === parseFloat(searchTerm))) {
            //     row.style.display = 'table-row';
            // }
            // else if (isNaN(searchTerm) && rowData.includes(searchTerm)) {
            //     row.style.display = 'table-row';
            // } else {
            //     row.style.display = 'none';
            // }
            // console.log('rowDataNumber:', rowDataNumber);
        });
    }
    // Agregar un evento de escucha al campo de búsqueda
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', searchDatabase);
});

// function editarPersona(button) {
    
//     var row = button.closest('tr');

//     var csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0].value;

//     // Obtener los valores de las celdas de la fila actual
//     var personaId = row.querySelector('input[name="persona_id"]').value;
//     var dni = row.querySelector('td:nth-child(3)').textContent.trim();
//     var nombreyapellido = row.querySelector('td:nth-child(4)').textContent.trim();
//     var empresa = row.querySelector('td:nth-child(5)').textContent.trim();
//     console.log('Valor de empresa en HTML:', row.querySelector('td:nth-child(5)').textContent.trim());
//     var acceso = row.querySelector('td:nth-child(6)').textContent.trim();
//     var observaciones = row.querySelector('td:nth-child(7)').textContent.trim();
//     var asistencia = row.querySelector('input[name="asistencia"]').checked;

//     // Crear un formulario invisible para enviar los datos al view cargaIndividual
//     var form = document.createElement("form");
//     form.setAttribute("method", "post");
//     form.setAttribute("action", "cargaIndividual");

//     // Crear campos ocultos con los datos de la persona
//     var csrfInput = document.createElement("input");
//     csrfInput.setAttribute("type", "hidden");
//     csrfInput.setAttribute("name", "csrfmiddlewaretoken");
//     csrfInput.setAttribute("value", csrfToken);
//     form.appendChild(csrfInput);

//     var personaIdInput = document.createElement("input");
//     personaIdInput.setAttribute("type", "hidden");
//     personaIdInput.setAttribute("name", "persona_id");
//     personaIdInput.setAttribute("value", personaId);
//     form.appendChild(personaIdInput);

//     var dniInput = document.createElement("input");
//     dniInput.setAttribute("type", "hidden");
//     dniInput.setAttribute("name", "dni");
//     dniInput.setAttribute("value", dni);
//     form.appendChild(dniInput);

//     var nombreyapellidoInput = document.createElement("input");
//     nombreyapellidoInput.setAttribute("type", "hidden");
//     nombreyapellidoInput.setAttribute("name", "nombreyapellido");
//     nombreyapellidoInput.setAttribute("value", nombreyapellido);
//     form.appendChild(nombreyapellidoInput);

//     var empresaInputHidden = document.createElement("input");
//     empresaInputHidden .setAttribute("type", "hidden");
//     empresaInputHidden .setAttribute("name", "empresa");
//     empresaInputHidden .setAttribute("value", empresa);
//     form.appendChild(empresaInputHidden);

//     var accesoInput = document.createElement("input");
//     accesoInput.setAttribute("type", "hidden");
//     accesoInput.setAttribute("name", "acceso");
//     accesoInput.setAttribute("value", acceso);
//     form.appendChild(accesoInput);

//     var observacionesInput = document.createElement("input");
//     observacionesInput.setAttribute("type", "hidden");
//     observacionesInput.setAttribute("name", "observaciones");
//     observacionesInput.setAttribute("value", observaciones);
//     form.appendChild(observacionesInput);

//     var asistenciaInput = document.createElement("input");
//     asistenciaInput.setAttribute("type", "hidden");
//     asistenciaInput.setAttribute("name", "asistencia");
//     asistenciaInput.setAttribute("value", asistencia);
//     form.appendChild(asistenciaInput);

//     // Agregar el formulario al body y enviarlo
//     document.body.appendChild(form);
//     form.submit();
// }
