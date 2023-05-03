 // Reemplaza 'TU_API_KEY' con tu clave de API
 const API_KEY = '9bdb57e83268a2cd8d444b5e4da39e58';

 // Indicador económico que deseas obtener (GBP)
 const INDICATOR = 'DEXBZUS';

 // URL de la API con los parámetros necesarios
 const API_URL = `https://api.stlouisfed.org/fred/series/observations?series_id=${INDICATOR}&api_key=${API_KEY}&file_type=json`;

 // Función para obtener el valor del indicador económico
 async function getIndicatorValue() {
   try {
     const response = await fetch(API_URL);
     const data = await response.json();

     // Agrega este console.log para verificar los datos obtenidos
     console.log(data);
     
     // Obtener el valor más reciente del indicador económico
     const indicatorValue = data.observations[0].value;

     // Agregar el valor a la página
     const indicatorValueElement = document.getElementById('indicator-value');
     indicatorValueElement.textContent = indicatorValue;
   } catch (error) {
     console.error(error);
   }
 }

 // Llamada a la función para obtener el valor del indicador económico
 getIndicatorValue();