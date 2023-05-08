const apiKey = "c1bb4c22a8fa3e75e2ea0e99ee3bbb69";

fetch(`https://api.openweathermap.org/data/2.5/weather?q=Madrid&appid=${apiKey}&units=metric`)
    .then(response => response.json())
    .then(data => {
        const weather = data.weather[0].description;
        const temp = data.main.temp;
        const humidity = data.main.humidity;
        const wind = data.wind.speed;

        const climaInfo = document.getElementById("clima-info");
        climaInfo.innerHTML = `El clima en Madrid es ${weather} con una temperatura de ${temp}°C, humedad del ${humidity}% y viento a una velocidad de ${wind} km/h.`;
    })
    .catch(error => console.log(error));