document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('selectAnio');
    selectElement.value = '2023';
    fetch("http://localhost:5000/contar_cursos")
        .then(response => response.json())
        .then(data => {
            document.getElementById('cursos-totales').innerHTML = data.total_cursos + ' cursos';
        })
        .catch(error => console.error('Error:', error));
    actualizarGraficos(selectElement.value)
});

document.getElementById('selectAnio').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarInformacion(selectedYear);
    actualizarGraficos(selectedYear);
});

function actualizarInformacion(anioSeleccionado) {
    fetch("http://localhost:5000/contar_cursos/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            document.getElementById('cursos-anuales').innerHTML = data.cantidad_de_cursos + ' cursos creados en el ' + anioSeleccionado;
        })
        .catch(error => console.error('Error:', error));
}
function actualizarGraficos(anioSeleccionado) {
    // Figura 1 
    fetch("http://localhost:5000/conteo_sedes/" + anioSeleccionado)
        .then(response => response.json())
        .then(data => {
            x_values = data.x_values
            y_values = data.y_values
            chart = document.getElementById('chart1')
            Plotly.newPlot(chart, [{
                type: 'bar',
                x: x_values,
                y: y_values
            }])
        }).catch(error => console.error('Error:', error));
    // Figura 2 
    // fetch("http://localhost:5000/grafico_facultades/" + anioSeleccionado)
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log("El data es ", data)
    //     }).catch(error => console.error('Error:', error));
}