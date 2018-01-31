const bluebird = require('bluebird');
const miio = require('miio');

module.exports = class Lamp {
  constructor({ address, token }) {
    this.credentials = { address, token };
  }

  async init () {
    this.device = await miio.device(this.credentials);

    return this.device;
  }

  togglePower () {
    return this.device.togglePower();
  }

  setBrightness(brightness) {
    this.device.setBrightness(Math.max(Math.min(brightness, 100), 1))
  }

  addEventListener (event, cb) {
    return device.on(event, cb);
  }
}

// setInterval(() => {
//   als((err, data) => {
//     const luminocity = (data.computedValue / 0.5).toFixed(2);
//
//     console.log(luminocity);
//   });
// }, 500);
