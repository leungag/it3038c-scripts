const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');
const { parse } = require('querystring');

// Append a log entry for "Application started"
const appStartEntry = `[${new Date().toISOString()}] INFO: Application started\n`;
fs.appendFile("C:\\it3038c-scripts\\project2\\log.txt", appStartEntry, (err) => {
    if (err) {
        console.error('Error appending to log file:', err);
    } else {
        console.log('Log entry appended to log.txt:', appStartEntry);
    }
});


const server = http.createServer(function(req, res) {
    if (req.url === "/") {
        // Serve the existing index.html file
        fs.readFile("./public/index.html", "UTF-8", function(err, body) {
            if (err) {
                console.error('Error reading index.html:', err);
                res.writeHead(500, { "Content-Type": "text/html" });
                res.end(`Error reading index.html: ${err}`);
            } else {
                console.log('Served index.html');
                res.writeHead(200, { "Content-Type": "text/html" });
                res.end(body);
            }
        });
    } else if (req.url === "/log") {
        // Read the log file
        fs.readFile("C:\\it3038c-scripts\\project2\\log.txt", "UTF-8", function(err, logData) {
            if (err) {
                console.error('Error reading log file:', err);
                res.writeHead(500, { "Content-Type": "text/html" });
                res.end(`Error reading log file: ${err}`);
            } else {
                console.log('Served log content');
                res.writeHead(200, { "Content-Type": "text/html" });
                res.end(logData.replace(/\n/g, "<br>"));
            }
        });
    } else if (req.url === "/appendlog" && req.method === "POST") {
        let requestBody = '';
        req.on('data', chunk => {
            requestBody += chunk.toString();
        });
        req.on('end', () => {
            const { logEntry } = parse(requestBody);

            if (logEntry) {
                // Append the log entry to the log.txt file
                const timestamp = new Date().toISOString();
                const entry = `[${timestamp}] ${logEntry}\n`;

                fs.appendFile("C:\\it3038c-scripts\\project2\\log.txt", entry, (err) => {
                    if (err) {
                        console.error('Error appending to log file:', err);
                        res.writeHead(500, { "Content-Type": "text/html" });
                        res.end(`Error appending to log file: ${err}`);
                    } else {
                        console.log('Log entry appended to log.txt:', entry);
                        res.writeHead(302, { 'Location': '/' });
                        res.end();
                    }
                });

            } else {
                console.log('Received a request to append an empty log entry');
                res.writeHead(400, { "Content-Type": "text/html" });
                res.end('Bad Request: Log entry is empty.');
            }
        });
    } else if (req.url.match("/sysinfo")) {
        // Add log entry for system information request
        const timestamp = new Date().toISOString();
        const entry = `[${timestamp}] INFO: System information requested\n`;

        fs.appendFile("C:\\it3038c-scripts\\project2\\log.txt", entry, (err) => {
            if (err) {
                console.error('Error appending to log file:', err);
            } else {
                console.log('Log entry appended to log.txt:', entry);
            }
        });

        // Your existing sysinfo code remains unchanged
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
        res.writeHead(200, { "Content-Type": "text/html" });
        res.end(html);
    } else {
        res.writeHead(404, { "Content-Type": "text/html" });
        res.end(`404 File Not Found at ${req.url}`);
    }
});

server.listen(3000);

console.log("Server listening on port 3000");

function formatUptime(uptime) {
    const days = Math.floor(uptime / (3600 * 24));
    const hours = Math.floor((uptime % (3600 * 24)) / 3600);
    const minutes = Math.floor((uptime % 3600) / 60);
    const seconds = Math.floor(uptime % 60);

    return `${days} Days, ${hours} Hours, ${minutes} Minutes, ${seconds} Seconds`;
}

function formatMemory(memory) {
    return (memory / (1024 * 1024)).toFixed(2);
}
