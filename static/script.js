function obtenerDatos(ruta, opciones) {
    fetch(ruta, opciones)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error en la peticion  ${response.status}`)
            }
            return response.json();
        }).then(data => {
            console.log('Datos recibidos', data);
        }).catch(err => {
            console.error('Error en la peticion', err.message)
        })
}
var table1 = new Tabulator(".example-table1", {
    data: obtenerDatos('http://localhost:5000/conteo_sedes/year',
        opciones = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        }
    ),
    columns: [
        { title: "Nombre de la sede", field: "sede" },
        { title: "Cantidad de cursos creados", field: "cursos" },
    ],
});


var table2 = new Tabulator(".example-table2", {
    data: "pendiente",
    columns: [
        { title: "Name", field: "name" },
        { title: "Age", field: "age" },
        { title: "Gender", field: "gender" },
        { title: "Height", field: "height" },
        { title: "Favourite Color", field: "col" },
        { title: "Date Of Birth", field: "dob" },
        { title: "Cheese Preference", field: "cheese" },
    ],
});
//trigger download of data.csv file
document.querySelector(".download-csv").addEventListener("click", function () {
    table1.download("csv", "data.csv");
    table2.download("csv", "data.csv");
});

//trigger download of data.json file
document.querySelector(".download-json").addEventListener("click", function () {
    table1.download("json", "data.json");
    table2.download("json", "data.json");
});

//trigger download of data.xlsx file
document.querySelector(".download-xlsx").addEventListener("click", function () {
    table1.download("xlsx", "data.xlsx", { sheetName: "My Data" });
    table2.download("xlsx", "data.xlsx", { sheetName: "My Data" });
});

//trigger download of data.pdf file
document.querySelector(".download-pdf").addEventListener("click", function () {
    table1.download("pdf", "data.pdf", {
        orientation: "portrait", //set page orientation to portrait
        title: "Example Report", //add title to report
    });
    table2.download("pdf", "data.pdf", {
        orientation: "portrait", //set page orientation to portrait
        title: "Example Report", //add title to report
    });
});

//trigger download of data.html file
document.querySelector(".download-html").addEventListener("click", function () {
    table1.download("html", "data.html", { style: true });
    table2.download("html", "data.html", { style: true });
});