const express = require('express');
const app = express();

const airlines = [
  { name: "Delta Air Lines", country: "United States", code: "DL", hub: "Atlanta Hartsfield-Jackson International Airport" },
  { name: "Emirates", country: "United Arab Emirates", code: "EK", hub: "Dubai International Airport" },
  { name: "Lufthansa", country: "Germany", code: "LH", hub: "Frankfurt Airport" },
  { name: "Qantas", country: "Australia", code: "QF", hub: "Sydney Airport" },
  { name: "Air France", country: "France", code: "AF", hub: "Charles de Gaulle Airport" }
];

app.get('/airlines', (req, res) => {
  res.json(airlines);
});

app.get('/airlines/:code', (req, res) => {
  const code = req.params.code;
  const airline = airlines.find(a => a.code === code);
  if (!airline) {
    res.status(404).send('Airline not found');
  } else {
    res.json(airline);
  }
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});