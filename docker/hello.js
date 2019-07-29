var http = require('http');

const hostname = process.env.HOSTNAME;

http.createServer(function (request, response) {  
    response.writeHead(200, {'Content-Type' : 'text/plain'});
    response.write('Hello world with node 12. hostname is [ ${hostname} ].\r\n');
    response.end();
}).listen(8080);

