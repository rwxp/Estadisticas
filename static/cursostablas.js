document.addEventListener('DOMContentLoaded', function () {
    var selectElement = document.getElementById('selectAnio');
    selectElement.value = '2023';
    actualizarSedes(selectElement.value)
    actualizarFacultades(selectElement.value)
});

document.getElementById('selectAnio').addEventListener('change', function () {
    var selectedYear = this.value;
    actualizarSedes(selectedYear);
    actualizarFacultades(selectedYear);
});

async function obtenerDatos(ruta, opciones, tipo) {
    try {
        const response = await fetch(ruta, opciones);

        if (!response.ok) {
            throw new Error(`Error en la peticion ${response.status}`);
        }
        var datos
        const data = await response.json();
        if (tipo == 'sedes') {
            datos = data.x_values.map((x_value, i) => ({
                sede: x_value,
                cursos: data.y_values[i],
            }));
        } else {
            datos = data.x_values.map((x_value, i) => ({
                facultad: x_value,
                cursos: data.y_values[i],
            }));
        }
        return datos;
    } catch (err) {
        console.error('Error en la peticion', err.message);
        throw err; // Re-lanzar el error para que pueda ser capturado por la función llamadora
    }
}

async function actualizarSedes(year) {
    const datos = await obtenerDatos(
        `http://localhost:5000/conteo_sedes/${year}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        }
        , 'sedes')
    var tableSedes = new Tabulator(".tabla-sedes", {
        data: datos,
        columns: [
            { title: "Nombre de la sede", field: "sede" },
            { title: "Cantidad de cursos creados", field: "cursos" },
        ],
    })
    agregarBotones(tableSedes);
}

async function actualizarFacultades(year) {
    const datos = await obtenerDatos(
        `http://localhost:5000/conteo_facultades/${year}`,
        {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        }
        , 'facultades')
    var tableFacultades = new Tabulator(".tabla-facultades", {
        data: datos,
        columns: [
            { title: "Nombre de la facultad", field: "facultad" },
            { title: "Cantidad de cursos creados", field: "cursos" },
        ],
    })
    agregarBotones(tableFacultades);
}

function agregarBotones(table) {
    //trigger download of data.csv file
    document.querySelector(".download-csv").addEventListener("click", function () {
        table.download("csv", "data.csv");
    });

    //trigger download of data.json file
    document.querySelector(".download-json").addEventListener("click", function () {
        table.download("json", "data.json");
    });

    //trigger download of data.xlsx file
    document.querySelector(".download-xlsx").addEventListener("click", function () {
        table.download("xlsx", "data.xlsx", { sheetName: "My Data" });
    });

    //trigger download of data.pdf file
    document.querySelector(".download-pdf").addEventListener("click", function () {
        table.download("pdf", "data.pdf", {
            orientation: "portrait", //set page orientation to portrait
            title: "Example Report", //add title to report
        });
    });

    //trigger download of data.html file
    document.querySelector(".download-html").addEventListener("click", function () {
        table.download("html", "data.html", { style: true });
    });
}