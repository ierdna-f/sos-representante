const XLSX = require('xlsx-js-style');
const fs = require('fs');
const path = require('path');
const ROOT_DIR = path.join(__dirname, '../..');
const { build } = require('./build-excel-item.js');

function generateExcelWorkbook(fileName, discount = 0.3) {
    const inputPath = path.join(ROOT_DIR, 'input', fileName);
    if (!fs.existsSync(inputPath)) { throw new Error(`File not found: ${inputPath}`) }

    const rawData = JSON.parse(fs.readFileSync(inputPath, 'utf8'));
    
    console.log("[DEBUG] First item from JSON:", rawData[0]);
    const excelData = rawData.map(rawItem => build(rawItem, discount));

    const worksheet = XLSX.utils.json_to_sheet(excelData);

    const range = XLSX.utils.decode_range(worksheet['!ref']);

    for (let C = range.s.c; C <= range.e.c; ++C) {

        const address = XLSX.utils.encode_col(C) + "1";
        if (!worksheet[address]) continue;

        worksheet[address].s = {
            fill: {
                fgColor: { rgb: "E9E9E9" }
            },
            font: {
                bold: true,
                name: "Arial",
                sz: 11
            },
            alignment: {
                horizontal: "center",
                vertical: "center"
            },
            border: {
                bottom: { style: "thin", color: { rgb: "000000" } }
            }
        };
    }
    worksheet['!cols'] = [
        { wch: 25 },
        { wch: 25 },
        { wch: 30 },
        { wch: 35 },
        { wch: 25 }
    ];

    worksheet['!autofilter'] = { ref: XLSX.utils.encode_range(range) };
    worksheet['!freeze'] = { xSplit: 0, ySplit: 1 };
    
    const workbook = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(workbook, worksheet, "Planilha de Promção! $$$");

    return workbook
}

module.exports = { generateExcelWorkbook };