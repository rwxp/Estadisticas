document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('selectAnio');
    selectElement.value = '2023';
    fetch("http://localhost:5000/contar_usuarios/")
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-totales').innerHTML = data.total_usuarios + ' usuarios';
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('selectAnio').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarInformacion(selectedYear);
    actualizarGraficos(selectedYear);
});

function actualizarInformacion(anioSeleccionado) {
    fetch("http://localhost:5000/contar_usuarios/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}

function actualizarGraficos(anioSeleccionado) {
    fetch("http://localhost:5000/grafico_usuarios_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
    fetch("http://localhost:5000/grafico_usuarios_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}