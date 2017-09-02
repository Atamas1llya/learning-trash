const crypto = require('crypto');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const encrypt = (string, password) =>
  crypto.createHmac('sha256', password).update(string).digest('hex');

process.stdout.write('\033c');

rl.question('Your text: \n', (string) => {
  process.stdout.write('\033c');

  rl.question('Your password: \n', (password) => {
    process.stdout.write('\033c');
    
    console.log(encrypt(string, password));
    process.exit();
  })
});
