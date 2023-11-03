var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName = os.hostname();
        serverUptime = formatUptime(os.uptime());
        totalMemory = formatMemory(os.totalmem());
        freeMemory = formatMemory(os.freemem());
        cpuCount = os.cpus().length;

        html = `    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: ${serverUptime}</p>
            <p>Total Memory: ${totalMemory} MB</p>
            <p>Free Memory: ${freeMemory} MB</p>
            <p>Number of CPUs: ${cpuCount}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");

// Function to format server uptime in Days, Hours, Minutes, Seconds
function formatUptime(uptime) {
    const days = Math.floor(uptime / (3600 * 24));
    const hours = Math.floor((uptime % (3600 * 24)) / 3600);
    const minutes = Math.floor((uptime % 3600) / 60);
    const seconds = Math.floor(uptime % 60);

    return `${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}

// Function to format memory in MB
function formatMemory(memory) {
    return (memory / (1024 * 1024)).toFixed(2);
}
