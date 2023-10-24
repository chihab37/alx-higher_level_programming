const fs = require('fs');

// Check if a file path argument was provided
if (process.argv.length < 3) {
    console.log('Please provide a file path as an argument.');
    process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data.trim());  // Using trim() to remove any trailing newline
});

