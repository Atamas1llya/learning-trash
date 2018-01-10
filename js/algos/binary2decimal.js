const binary2decimal = (binary) => {
  console.log(binary);
  let decimal = 0;
  binaryArr = binary.split('').reverse();
  binaryArr.forEach((byte, index) => {
    if (+byte) {
      decimal += Math.pow(2, index);
    }
  })
  return decimal;
}

// console.log(binary2decimal(process.argv[2]));
binary2decimal(process.argv[2])
