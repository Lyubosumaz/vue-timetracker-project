// const { defineConfig } = require("@vue/cli-service");
// module.exports = defineConfig({
//   transpileDependencies: true,
// });

// const { defineConfig } = require("@vue/cli-service");
// const BundleTracker = require("webpack-bundle-tracker");

// module.exports = defineConfig({
//   publicPath: "http://0.0.0.0:8080/",
//   outputDir: "./dist/",
//   transpileDependencies: true,
//   runtimeCompiler: true,

//   pages: {
//     main: {
//       entry: "src/main.ts",
//     },
//   },

//   chainWebpack: (config) => {
//     config.optimization.splitChunks(false);

//     config
//       .plugin("BundleTracker")
//       .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

//     config.resolve.alias.set("__STATIC__", "static");

//     config.devServer
//       .host("0.0.0.0")
//       .port(8080)
//       .hot("only")
//       // .watchOptions({ poll: 1000 })
//       .https(false)
//       .headers({ "Access-Control-Allow-Origin": ["*"] });
//   },
// });

const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  /* your config */
  configureWebpack: {
    optimization: {
      runtimeChunk: "single",
    },
  },
  devServer: {
    // we need this for apollo to work properly
    proxy: `https://${process.env.SANDBOX_HOSTNAME}/`,
    host: "0.0.0.0",
    allowedHosts: "all",
  },
});
