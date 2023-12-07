document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('selectAnio');
    selectElement.value = '2023';
    fetch("http://localhost:5000/contar_cursos/")
        .then(response => response.json())
        .then(data => {
            document.getElementById('cursos-totales').innerHTML = data.total_usuarios + ' cursos';
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('selectAnio').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarInformacion(selectedYear);
});

function actualizarInformacion(anioSeleccionado) {
    fetch("http://localhost:5000/contar_usuarios/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_cursos + ' usuarios creados en el ' + anioSeleccionado;
        })
}