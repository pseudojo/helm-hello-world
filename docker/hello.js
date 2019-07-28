var http = require('http');

http.createServer(function (request, response) {  
    response.writeHead(200, {'Content-Type' : 'text/plain'});
    response.write('Hello world with node 12.');
    response.end();
}).listen(8080);

