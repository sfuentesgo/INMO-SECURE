# InmoSecure-MVP

Este repositorio contiene un prototipo básico y funcional (MVP) de un sistema inmobiliario desarrollado para la asignatura Seguridad en Software de la Corporación Universitaria Tecnológica del Oriente. 

Laboratorio práctico para la implementación, configuración y validación de seguridad en la capa de transporte mediante el uso de certificados digitales SSL/TLS (HTTPS).

## Especificaciones Técnicas
* Lenguaje: Python 3
* Framework: Flask
* Seguridad: Certificado auto-firmado X.509 generado localmente con OpenSSL (RSA 4096 bits).

## Instrucciones de Instalación y Despliegue

Siga estos pasos para replicar el entorno seguro en su máquina :

### 1. Clonar el repositorio y preparar carpetas
Ejecute los siguientes comandos en su terminal para clonar el proyecto y crear el directorio de seguridad:

git clone https://github.com/sfuentesgo/INMO-SECURE.git

cd INMO-SECURE

mkdir certificados

### 2. Generar los Certificados Digitales (OpenSSL)
Abra una terminal de PowerShell dentro de la raíz del proyecto y ejecute los siguientes comandos para configurar la ruta de OpenSSL y generar la clave privada junto al certificado público (asegúrese de escribir localhost en el campo Common Name):

$env:OPENSSL_CONF = "C:\Program Files\Git\usr\ssl\openssl.cnf"

openssl req -x509 -newkey rsa:4096 -keyout certificados/key.pem -out certificados/cert.pem -days 365 -nodes

### 3. Instalar dependencias y ejecutar
Instale la librería Flask e inicialice el servidor web local con soporte SSL/TLS:

pip install flask

python inmo.py

### 4. Acceder al entorno
Abra su navegador web de preferencia e ingrese de forma segura a través de la siguiente dirección URL:

https://localhost:5000
