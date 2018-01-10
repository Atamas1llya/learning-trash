const _ = require('lodash');
const euc = require('euclidean-distance');
const dataset = require('./iris.json');

const data = [];
const target = [];

// setosa = 0
// versicolor = 1
// virginica = 2

dataset.forEach((set) => {
  const splitted = _.chunk(Object.values(set), 4);

  data.push(splitted[0]);
  if (splitted[1][0] === 'setosa') {
    target.push(0)
  } else if (splitted[1][0] === 'versicolor') {
    target.push(1)
  } else {
    target.push(2);
  }
})

class ScrappyKNN {
  train(trainX, trainY) {
    this.trainX = trainX;
    this.trainY = trainY;
  }

  predict(dataX) {
    const predictions = [];

    dataX.forEach((x) => {
      predictions.push(this.closest(x));
    })

    return predictions;
  }

  closest(row) {
    let bestDist = euc(row, this.trainX[0]);
    let bestIndex = 0;

    this.trainX.forEach((x, i) => {
      const dist = euc(row, x);
      if (dist < bestDist) {
        bestDist = dist;
        bestIndex = i;
      }
    })

    return this.trainY[bestIndex];
  }
}

const testData = _.pullAt(data, [0, 50, 100]);
const testTarget = _.pullAt(target, [0, 50, 100]);

const clf = new ScrappyKNN();
clf.train(data, target);
console.log(clf.predict(testData));
