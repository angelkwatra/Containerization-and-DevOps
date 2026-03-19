const express = require('express');
const app = express();

const PORT = process.env.PORT || 3000;
const DB = process.env.DATABASE_URL || "Not set";

app.get('/', (req, res) => {
    res.send("Hello from Node Docker App 🚀");
});

app.get('/env', (req, res) => {
    res.json({
        database: DB,
        debug: process.env.DEBUG
    });
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
