
var tableData = [
    { id: 1, name: "Billy Bob", age: "12", gender: "male", height: 1, col: "red", dob: "", cheese: 1 },
    { id: 2, name: "Mary May", age: "1", gender: "female", height: 2, col: "blue", dob: "14/05/1982", cheese: true },
]

var table1 = new Tabulator(".example-table1", {
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

var table2 = new Tabulator(".example-table2", {
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
table1.setHeight(240); //set table height to 500px
table2.setHeight(240); //set table height to 500px
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