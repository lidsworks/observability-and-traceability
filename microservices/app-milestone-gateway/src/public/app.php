<?php

use Psr\Http\Message\ResponseInterface as Response;
use Psr\Http\Message\ServerRequestInterface as Request;
use Slim\Factory\AppFactory;
use GuzzleHttp\Client;


require 'vendor/autoload.php';

// Crear una nueva aplicación Slim
$app = AppFactory::create();


// Define tu ruta
$app->get('/questions', function (Request $request, Response $response, $args) {
    // Inicializa un cliente Guzzle
    $client = new Client();

    // Realiza la llamada a la otra API
    $url = 'http://lidm-app-milestone-backend-svc:5000/questions'; // Reemplaza con la URL de tu API
    $responseFromAPI = $client->get($url);

    // Obtiene el cuerpo de la respuesta
    $body = $responseFromAPI->getBody()->getContents();

    // Devuelve la respuesta de la API al cliente
    $response->getBody()->write($body);
    return $response->withHeader('Content-Type', 'application/json');
});

// Definir una ruta
$app->get('/saludo/{nombre}', function (Request $request, Response $response, $args) {
    $nombre = $args['nombre'];
    $mensaje = "¡Hola, $nombre!";
    $response->getBody()->write($mensaje);
    return $response;
});

// Manejar rutas no encontradas
$app->get('/{routes:.+}', function (Request $request, Response $response) {
    $response->getBody()->write(json_encode(['message' => 'nop, nada... 404 amigui!']));
    return $response
        ->withHeader('Content-Type', 'application/json')
        ->withStatus(404);
});

// Ejecutar la aplicación
$app->run();