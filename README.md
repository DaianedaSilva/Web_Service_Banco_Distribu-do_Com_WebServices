# Web_Service_Banco_Distribu-do_Com_WebServices
Aplicação web com python e flask


https://graduacao.mackenzie.br/pluginfile.php/589870/mod_resource/content/1/Banco%20Distribu%C3%ADdo%20com%20Webservices.pdf


## Intalação do flask

Utilize o comando: `python3-flask` 

## Para rodar asaplicações
Utilize o comando: `FLASK_APP=<arquivo_da_aplicação> FLASK_RUN_PORT=<porta> flask run`

## configuração de portas

 - Servidor de dados: localhost:5000
 - Servidor de negócio 1: localhost:5001
 - Servidor de negócio 2: localhost:5002
 - Servidor de negócio 3: localhost:5003

## Realizar requests
Para realizar um request adicione o campo `x-api-key` no header do seu pacote, passando como valor um toke válido  