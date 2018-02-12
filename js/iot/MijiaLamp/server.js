const brightness = require('brightness');

const Lamp = require('./entities/lamp');
const Screen = require('./entities/screen');

const lampCredentials = require('./config/config.secure');

(async () => {
  const lamp = new Lamp(lampCredentials);
  const screen = new Screen();

  await lamp.init();

  screen.on('brightnessChanged', async (brightness) => {
    const normalizedBrightness = ((brightness - 0.4) / (0.95 - 0.4) * 100);

    if (normalizedBrightness < -30) {
      if (await lamp.device.power()) {
        // console.log('Power off...');
        await lamp.device.setPower(false);
      }
    } else {
      if (!await lamp.device.power()) {
        // console.log('Power on...');
        await lamp.device.setPower(true);
      }

      // console.log(`brightness: ${normalizedBrightness}`);
      lamp.setBrightness(normalizedBrightness);
    }
  })

  let screenBrightness;
})();
