// // Definir el color deseado en formato hexadecimal
//  var color = "#FF0000";

//  // Crear un icono personalizado
//  var customIcon = L.icon({
//      iconUrl: 'path/to/your/icon.png', // Reemplaza con la URL de tu icono personalizado
//      html: '<div style="background-color:' + color + ';" class="marker-pin"></div>'
// });

// Verificar si el navegador soporta la geolocalización
if ("geolocation" in navigator) {
    // Obtener la ubicación del usuario
    navigator.geolocation.getCurrentPosition(function(position) {
      var latitude = position.coords.latitude;
      var longitude = position.coords.longitude;
      
      console.log("Latitud: " + latitude);
      console.log("Longitud: " + longitude);

      var map = L.map('map').setView([latitude, longitude], 15);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}).addTo(map);
      L.marker([latitude, longitude]).addTo(map).bindPopup('Mi ubicacion').openPopup();
      
       // Definir las coordenadas de los centros que deseas mostrar
       var centros = [
        { nombre: "Centro 1", latitud: 6.278658063783507, longitud: -75.56239646160202 },
        { nombre: "Centro 2", latitud: 4.80522150785446, longitud: -75.75643466242147 },
        { nombre: "Centro 2", latitud: 4.804633484994062, longitud: -75.75536180384844 }, 
        // Agregar más centros aquí
      ];

      // Calcular la distancia entre la ubicación del usuario y los centros
      centros.forEach(function(centro) {
        var distancia = calcularDistancia(latitude, longitude, centro.latitud, centro.longitud);

        // Si la distancia está dentro del rango deseado (en metros), muestra el centro en el mapa
        var rango = 5000; // Cambia esto al rango deseado en metros
        if (distancia <= rango) {
          L.marker([centro.latitud, centro.longitud]).addTo(map).bindPopup(centro.nombre).openPopup();
        }
      });
    }), function(error) {
      // Manejar errores aquí
  }, { enableHighAccuracy: true };
  } else {
    console.log("La geolocalización no está disponible en este navegador.");
}

// Función para calcular la distancia entre dos puntos en coordenadas geográficas (en metros)
function calcularDistancia(lat1, lon1, lat2, lon2) {
    var radioTierra = 6371; // Radio de la Tierra en kilómetros
    var dLat = (lat2 - lat1) * (Math.PI / 180);
    var dLon = (lon2 - lon1) * (Math.PI / 180);
    var a =
      Math.sin(dLat / 2) * Math.sin(dLat / 2) +
      Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
      Math.sin(dLon / 2) * Math.sin(dLon / 2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var distancia = radioTierra * c * 1000; // Distancia en metros
    return distancia;
}

// IMPORTANTE: PUEDE HABER VARIABILIDAD EN EL RESULTADO POR LAS SIGUIENTES RAZONES:

// Precisión de la geolocalización: La precisión de la geolocalización puede variar según la disponibilidad de señales GPS y otros factores ambientales. Esto puede llevar a que en algunas ocasiones obtengas una ubicación más precisa y en otras una menos precisa.

// Caché de ubicación: Los navegadores a veces almacenan en caché la ubicación para acelerar la respuesta en futuras solicitudes de geolocalización. Esto significa que en algunas ocasiones podrías obtener la última ubicación conocida en lugar de la ubicación en tiempo real.

// Permiso del usuario: Algunos navegadores pueden solicitar permiso al usuario para acceder a la ubicación. Si el usuario cambia su ubicación después de otorgar el permiso, la ubicación puede ser diferente.

// Actualización de la ubicación: La API de geolocalización puede no proporcionar una ubicación en tiempo real en todo momento. En algunos casos, puede haber una pequeña demora en la actualización de la ubicación.

// Errores de red: Problemas de red pueden afectar la precisión de la geolocalización. Por ejemplo, si el dispositivo tiene problemas para obtener señales GPS o para conectarse a servicios de geolocalización en línea, los resultados pueden variar.