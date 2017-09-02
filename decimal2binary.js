const decimalToBinary = (decimal) => {
  let bytes = ['0'];
  let rest = decimal;

  while (rest > 0) {
    if (rest === 1) {
      bytes[bytes.length - 1] = '1';
      rest = 0;
    }
    
    for (let i = 1; Math.pow(2, i) <= decimal; i++) {
      if (decimal < Math.pow(2, i + 1)) {
        bytes[i] = '1';
        for (let x = i - 1; x >= 0; x--) {
          bytes[x] = '0';
        }

        rest = decimal - Math.pow(2, i);
      }
    }

    for (let i = bytes.length; i >= 0; i--) {
      if (Math.pow(2, i) === decimal) {
        bytes[i] = '1';
      }
    }

    decimal = rest;
  }
  return bytes.reverse().join('');
}

console.log(decimalToBinary(+process.argv[2]));
