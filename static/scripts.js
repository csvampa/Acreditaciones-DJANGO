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


        });
    }
    // Agregar un evento de escucha al campo de búsqueda
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', searchDatabase);
});


