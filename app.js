const express = require("express");
const app = express();

app.listen(3000);

app.get("/", (req, res) => {
  res.send("<p>Manual de Máquinas!</p>");
});
