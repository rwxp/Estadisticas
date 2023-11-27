
var tableData = [
    { id: 1, name: "Billy Bob", age: "12", gender: "male", height: 1, col: "red", dob: "", cheese: 1 },
    { id: 2, name: "Mary May", age: "1", gender: "female", height: 2, col: "blue", dob: "14/05/1982", cheese: true },
]

var table = new Tabulator("#example-table", {
    data: tableData, //set initial table data
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
document.getElementById("download-csv").addEventListener("click", function () {
    table.download("csv", "data.csv");
});

//trigger download of data.json file
document.getElementById("download-json").addEventListener("click", function () {
    table.download("json", "data.json");
});

//trigger download of data.xlsx file
document.getElementById("download-xlsx").addEventListener("click", function () {
    table.download("xlsx", "data.xlsx", { sheetName: "My Data" });
});

//trigger download of data.pdf file
document.getElementById("download-pdf").addEventListener("click", function () {
    table.download("pdf", "data.pdf", {
        orientation: "portrait", //set page orientation to portrait
        title: "Example Report", //add title to report
    });
});

//trigger download of data.html file
document.getElementById("download-html").addEventListener("click", function () {
    table.download("html", "data.html", { style: true });
});