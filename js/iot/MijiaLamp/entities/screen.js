const brightness = require('brightness');
const EventEmitter = require('events');

module.exports = class Screen extends EventEmitter {
  constructor() {
    super();
    this.brightness = 0;

    setInterval(async () => {
      const screenBrightness = await brightness.get();

      if (this.brightness !== screenBrightness) {
        this.emit('brightnessChanged', screenBrightness);
        this.brightness = screenBrightness;
      }
    }, 500);
  }
}
