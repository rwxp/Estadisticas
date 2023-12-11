document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('anioSelect');
    selectElement.value = '2023';
    fetch("http://localhost:5000/contar_usuarios/")
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-totales').innerHTML = data.total_usuarios + ' usuarios';
        })
        .catch(error => console.error('Error:', error));
});

document.getElementById('anioSelect').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarInformacionUsuarios(selectedYear);
    actualizarGraficosUsusarios(selectedYear);
});

function actualizarInformacionUsuarios(anioSeleccionado) {
    fetch("http://localhost:5000/contar_usuarios/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => { console.log(data.cantidad_de_usuarios)
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}
/*
function actualizarGraficosUsusarios(anioSeleccionado) {
    fetch("http://localhost:5000/grafico_usuarios_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios //+ ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
    fetch("http://localhost:5000/grafico_usuarios_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}*/