const express = require('express');
const XLSX = require('xlsx-js-style')
const path = require('path');
const fs = require('fs');
const { generateExcelWorkbook } = require('../service/generate-excel-sheet.js');
const app = express();

app.get('/api/excel', (req, res) => {
    try {
        const { filename, discount } = req.query;

        if (!filename) {
            return res.status(400).send("Missing filename parameter");
        }

        const rawDiscount = parseInt(discount);
        const decimalDiscount = rawDiscount / 100;


        const workbook = generateExcelWorkbook(filename, decimalDiscount);
        const outputDir = path.join(__dirname, '../output/excel');
        const outputPath = path.join(outputDir, `${filename.replace('.json', '')}.xlsx`);
        
        if (!fs.existsSync(outputDir)) {
            fs.mkdirSync(outputDir, { recursive: true });
        }

        XLSX.writeFile(workbook, outputPath);
        
        console.log("[INFO] Success Workbook generated and saved.");
        res.status(200).json({ 
            status: "success", 
            message: `Workbook generated and saved to folder: ${outputPath}` 
        });

    } catch (error) {
        console.error("[ERROR]", error.message);
        res.status(500).send(error.message);
    }
});

app.listen(3000, () => console.log("API up and healthy on port 3000"));