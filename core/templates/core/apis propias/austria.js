const express = require('express');
const app = express();
const port = 3000;

const austriaData = [
  {
    id: 1,
    name: "Palacio de Schönbrunn",
    description: "Uno de los monumentos históricos y culturales más importantes de Austria, ubicado en Viena.",
    image: "https://www.schoenbrunn.at/fileadmin/schoenbrunn/Pool_Bilder/Galerie/normal/48-2012-04-03-Schoenbrunn-Sommer.jpg",
    location: {
      lat: 48.185698,
      lng: 16.312068
    }
  },
  {
    id: 2,
    name: "Salzburgo",
    description: "Una de las ciudades más bellas de Austria, famosa por su arquitectura barroca y la música clásica.",
    image: "https://www.austria.info/media/11773/thumbnails/salzburg-mirabell-garten-schloss-mirabell.jpg.3141488.jpg",
    location: {
      lat: 47.800276,
      lng: 13.044722
    }
  },
  {
    id: 3,
    name: "El Tirol",
    description: "Una región montañosa en el oeste de Austria, famosa por sus paisajes alpinos y sus estaciones de esquí.",
    image: "https://www.austria.info/media/11645/thumbnails/Abendstimmung-in-Leutasch-in-Tirol-Oesterreich.jpg.3141488.jpg",
    location: {
      lat: 47.258333,
      lng: 11.395833
    }
  },
  {
    id: 4,
    name: "Vienna State Opera",
    description: "Uno de los edificios más emblemáticos de Viena y uno de los principales teatros de ópera del mundo.",
    image: "https://www.wiener-staatsoper.at/fileadmin/user_upload/Wiener_Staatsoper/Seitenbereiche/About_us/Front_of_the_house/170117_C_Ballett_Roman_Novitzky_6978.jpg",
    location: {
      lat: 48.2025,
      lng: 16.368889
    }
  },
  {
    id: 5,
    name: "Graz",
    description: "La segunda ciudad más grande de Austria, conocida por su arquitectura medieval y su ambiente universitario.",
    image: "https://www.austria.info/media/12662/thumbnails/graz-panorama-abends.jpg.3141488.jpg",
    location: {
      lat: 47.066667,
      lng: 15.45
    }
  }
];

app.get('/places', (req, res) => {
  res.json(austriaData);
});

app.get('/places/:id', (req, res) => {
  const placeId = parseInt(req.params.id);
  const place = austriaData.find(place => place.id === placeId);
  
  if (place) {
    res.json(place);
  } else {
    res.status(404).send('Place not found');
  }
});

app.listen(port, () => {
  console.log(`API listening at http://localhost:${port}`);
});