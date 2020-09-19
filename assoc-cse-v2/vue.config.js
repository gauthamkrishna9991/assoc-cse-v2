// Configuration for Front-End (Development)

module.exports = {
  devServer: {
    proxy: {
      "^/api": {
        target: "http://localhost:4000",
        ws: true,
        changeOrigin: true
      }
    }
  }
};
