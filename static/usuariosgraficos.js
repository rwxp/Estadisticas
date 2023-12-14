document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('anioSelect');
    selectElement.value = '2023';
    fetch("http://localhost:5000/contar_usuarios")
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-totales').innerHTML = data.total_usuarios + ' usuarios';
        })
        .catch(error => console.error('Error:', error));
    actualizarGraficosUsusarios(selectElement.value)
});

document.getElementById('anioSelect').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarInformacionUsuarios(selectedYear);
    actualizarGraficosUsusarios(selectedYear);
});

function actualizarInformacionUsuarios(anioSeleccionado) {
    fetch("http://localhost:5000/contar_usuarios/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('usuarios-anuales').innerHTML = data.cantidad_de_usuarios + ' usuarios creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}
function actualizarGraficosUsusarios(anioSeleccionado) {
    // Figura 1
    fetch("http://localhost:5000/conteo_usuarios_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            x_values = data.x_values
            y_values = data.y_values
            chart = document.getElementById('chart3')
            Plotly.newPlot(chart, [{
                type: 'bar',
                x: x_values,
                y: y_values
            }])
        }).catch(error => console.error('Error:', error));
    // Figura 2
    /*
    fetch("http://localhost:5000/conteo_usuarios_facultades/" + anioSeleccionado)
    .then(response => response.json())
    .then(data => {
        x_values = data.x_values
        y_values = data.y_values
        chart = document.getElementById('chart4')
        Plotly.newPlot(chart, [{
            type: 'bar',
            x: x_values,
            y: y_values
        }])
    }).catch(error => console.error('Error:', error));*/
}
