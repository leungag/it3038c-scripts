# Project 2
This project use the existing code from Lab 6.
The project use node.js to display the contents of log file to a web page.

Create a log.txt file in the same directory as the project file.

In the index.html file this JavaScript that will fetch and disply log content.
```Javascript
<!-- Code for project2-->
    <h2>Log Content</h2>
    <div id="logContent">
      <!-- Log content will be inserted here -->
    </div>

    <script>
      // JavaScript code to fetch and display system information
      fetch('/sysinfo')
        .then(response => response.text())
        .then(data => {
          document.getElementById('systemInfo').innerHTML = data;
        })
        .catch(error => {
          console.error('Error fetching system information:', error);
          document.getElementById('systemInfo').innerHTML = 'Error fetching system information.';
        });

      // JavaScript code to fetch and display log content
      fetch('/log')
        .then(response => response.text())
        .then(data => {
          document.getElementById('logContent').innerHTML = data;
        })
        .catch(error => {
          console.error('Error fetching log content:', error);
          document.getElementById('logContent').innerHTML = 'Error fetching log content.';
        });
    </script>
```
If the JavaScript is not running, while the index.html is running, an error will be displayed saying "Error fetching log content". See image below.

![image](https://github.com/leungag/it3038c-scripts/assets/142808905/068f2986-3355-4b1e-9481-cdfbbbbdd857)



Inside the JavaScript project file there are some codes that will fetch and display log entry. The first log entry is the "Application stated" which will display when both index and project file are running.
```JavaScript
const appStartEntry = `[${new Date().toISOString()}] INFO: Application started\n`;
fs.appendFile("C:\\it3038c-scripts\\project2\\log.txt", appStartEntry, (err) => {
    if (err) {
        console.error('Error appending to log file:', err);
    } else {
        console.log('Log entry appended to log.txt:', appStartEntry);
    }
});
```

The next portion of the code are the log files that will append into the log.txt file. 
This part of the code will append into the log.txt file when a request is made. Refreshing the page or clicking on the link will generate this log. This mean that the code is runnning with no errors.
```javascript
else if (req.url.match("/sysinfo")) {
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

```

To test it run the command in powershell
```powershell
node project2.js
```

Then open a web browser and enter in the URL
```
http://localhost:3000/
```
The output should look like this

![image](https://github.com/leungag/it3038c-scripts/assets/142808905/9b8952ce-b6c3-4d86-b7c8-b832df53fc2d)


