const express = require('express');
const { exec } = require('child_process');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
  exec('python3 app/info.py', (err, stdout, stderr) => {
    if (err) {
      res.status(500).send("Error executing Python script");
      return;
    }
    res.type('json').send(stdout);
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
