//'node server.js'
const port = 8080;//port for the server 80, 443, 8080 test

const express = require('express');
const app = express();
const fs = require('fs');
const path = require('path');
const logs = require('./logger');
const { default: axios } = require('axios');
axios.defaults.baseURL = 'http://localhost:8001';

async function notfoundpage(response, url) {//404 page goes here
    response.writeHead(404);
    response.write('404 page not , code: ' + url);
    logs.info('File not found: ' + url);
}

app.use(express.static('www'))

app.get('/', (request, response) => { })//startingpoint(response) });

app.get('/index.html', (request, response) => { })//startingpoint(response) });

/*Receive code from User */
app.post('/post/code_string', (request, response) => {

    logs.info('Code upload');
    request.on('data', function (data) {
        logs.info('received : ' + data);
        try{
            axios.post('/process/code_string', JSON.parse(data).code_string)
            .then(function (axiosresponse) {
                logs.info(axiosresponse);
            })
            .catch(function (error) {
                logs.error(error) 
            });

        }catch(error){
            logs.error(error);
        }

        response.end(JSON.stringify({ console_put: ["hello", "user"] }));
    });
});

app.listen(port, () => { logs.info('Running on port ' + port) })//Listen for requests, this starts the server

async function startingpoint(response) {//serve index.html
    try {
        response.setHeader('Acess-Control-Allow-Origin', '*');//allow access control from client, this will automatically handle most media files

        response.writeHead(200, { 'Content-type': 'text/html' });//200 ok

        fs.readFile('www/index.html', function (err, databuffer) {
            if (err) {
                logs.error(err);
            } else {
                response.write(databuffer);
            }
            logs.info("User came online " + response);
            response.end();//end response

        });
    } catch (err) {
        logs.error('Catastrophy on index: \n' + err);
    }
}

async function writeresponce(res, filepath) {
    //write files in responses

    try {
        fs.readFile(filepath, function (err, databuffer) {
            if (err) {
                res.writeHead(404);//not okay
                logs.error(err);
            } else {
                res.writeHead(200);//200 ok
                res.write(databuffer);
            }
            res.end();//end response
        })
    } catch (error) {
        logs.error(error);
    }
}
