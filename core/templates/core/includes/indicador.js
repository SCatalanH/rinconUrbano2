// Obtener el elemento HTML donde se mostrará el valor del indicador
const exchangeRateElement = document.getElementById('exchange-rate');

// Definir la URL de la API con tu API Key
const apiUrl = 'https://api.stlouisfed.org/fred/series/observations?series_id=DEXCAUS&api_key=9bdb57e83268a2cd8d444b5e4da39e58&file_type=json';

// Realizar una solicitud a la API utilizando fetch
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Obtener el último valor del tipo de cambio
    const latestExchangeRate = data.observations[data.observations.length - 1].value;

    // Actualizar el contenido del elemento HTML con el valor del tipo de cambio
    exchangeRateElement.textContent = `El tipo de cambio GBP/USD es: ${latestExchangeRate}`;
  })
  .catch(error => console.error(error));