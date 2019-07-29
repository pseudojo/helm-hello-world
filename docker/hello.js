var http = require('http');
var os = require('os');


http.createServer(function (request, response) {  
    const hostname = process.env.HOSTNAME;

    response.writeHead(200, {'Content-Type' : 'text/plain'});
    response.write(`Hello world with node 12. hostname is [ ${hostname} ].\r\n`);
    response.end();
}).listen(8080);

