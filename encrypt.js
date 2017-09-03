const crypto = require('crypto');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const encrypt = (string, password) =>
  crypto.createHmac('sha256', password).update(string).digest('hex');

rl.question('Your text: \n', (string) => {

  rl.question('Your password: \x1b[8m\n', (password) => {

    console.log('\x1b[0m Encrypted text:', encrypt(string, password));
    process.exit();
  })
});
