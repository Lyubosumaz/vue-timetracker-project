module.exports = {
  module: {
    rules: [
      {
        test: /\.s(c|a)ss$/,
        use: [
          "vue-style-loader",
          "css-loader",
          {
            loader: "css-loader",
            options: {
              minimize: true,
              importLoaders: 1,
              sourceMap: true,
              alias: {
                "/static": join(this.options.srcDir, "static"),
                "/assets": join(this.options.srcDir, "assets")
              }
            }
          }
        ]
      }
    ]
  }
};
