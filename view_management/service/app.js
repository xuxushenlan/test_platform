let express = require('express');
const proxyMiddlewar = require('http-proxy-middleware');
let app = express();

const PORT = 8081;

// 后端Django主机
const djangoHost = 'http://127.0.0.1:8000';
const djangoProxyOption = { target: djangoHost, changeOrigin: true };

//反向代理，把api的请求都转发到8000里面
//将/api/* 代理到 ${HOST}/api/*
app.use('/api/*', proxyMiddlewar(djangoProxyOption));

// 监听
app.listen(PORT, function () {
    console.log('success listen...' + PORT);
});


