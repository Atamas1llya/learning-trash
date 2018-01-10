const fs = require('fs');
const { execSync } = require('child_process');

const devDependencies = 'express webpack babel-cli babel-core babel-preset-stage-0 babel-preset-react babel-preset-es2015';
const dependencies = 'react react-router less less-loader style-loader css-loader';

// ==================
// Functions
// ==================

const createFolder = (url) => {
  fs.mkdirSync(url);
}

const createFile = (url, data) => {
  fs.writeFileSync(url, data);
}

const unlink = (path) => {
  if (fs.existsSync(path)) {
    fs.readdirSync(path).forEach((file, index) => {
      const curPath = `${path}/${file}`;
      if (fs.lstatSync(curPath).isDirectory()) {
        unlink(curPath);
      } else {
        fs.unlinkSync(curPath);
      }
    });
    fs.rmdirSync(path);
  }
}

const createProject = (name) => {
  createFolder(`./${name}`)
  createFolder(`./${name}/app`);
  createFile(`./${name}/app/App.js`);
  createFile(`./${name}/app/index.js`);

  createFolder(`./${name}/app/components`);

  createFolder(`./${name}/app/less`);
  createFile(`./${name}/app/less/index.less`);

  createFolder(`./${name}/dist`);

  createFile(`./${name}/index.html`, content.html);

  createFile(`./${name}/server.js`, content.server);
  createFile(`./${name}/config.js`, content.config);
  createFile(`./${name}/webpack.config.js`, content.webpackConfig);

  execSync(`cd ${name} && npm init -y`, { stdio: [ 0,1,2] });
  execSync(`cd ${name} && npm i --save-dev ${devDependencies}`, { stdio: [ 0,1,2] });

  execSync(`cd ${name} && npm i --save ${dependencies}`, { stdio: [ 0,1,2] });
}

// ==================
// File contains
// ==================

const content = {
  webpackConfig: `
    const path = require('path');
    const webpack = require('webpack');

    module.exports = {

      entry: './app/index.js',
      output: {
        path: path.join(__dirname, 'dist'),
        filename: 'bundle.js',
      },
      watchOptions: {
        aggregateTimeout: 100,
      },
      devtool: 'cheap-module-source-map',
      module: {
        loaders: [

          {
            test: /.jsx?$/,
            exclude: /\/node_modules\//,
            loader: 'babel-loader',
          },

          {
            test: /.less$/,
            loaders: ['style-loader', 'css-loader', 'less-loader'],
          },

        ],
      },
      plugins: [
        new webpack.NoEmitOnErrorsPlugin(),
      ],

      resolve: {
        extensions: ['.js', '.jsx'],
      },

    };
  `,
  server: `
    import express from 'express';
    import path from 'path';
    import { port } from './config';

    const app = express();

    app.use(express.static(__dirname));

    app.listen(port, () => {
      console.log(\`Listening at \${port}...\`);
    });

    // for ReactJS
    app.get('*', (req, res) => {
      res.sendFile(path.resolve(__dirname, 'index.html'));
    });
  `,
  config: `
    module.exports = {
      port: 3000,
    };
  `,
  html: `
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css">
      <title>Node-React-App</title>
    </head>
    <body>
      <div id="root">

      </div>
      <script src='/dist/bundle.js'></script>
    </body>
    </html>
  `
};

// ==================
// Executor
// ==================

(() => {
  try {
    const projectName = process.argv[2];
    createProject(projectName);
  } catch (e) {
    console.error(e);
    throw new Error('Failed to create project!');
  };

  console.log('Project created!');
})();

// Created by Atamas1llya for Atamas1llya
