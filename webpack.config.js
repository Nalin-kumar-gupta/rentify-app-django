const port = process.env.port || 8080;
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const historyApiFallback = require('connect-history-api-fallback');
// const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');


module.exports = {
    mode: 'development',
    entry: {
        bundle: path.resolve(__dirname, 'src/index.js'),
    },
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: '[name].[contenthash].js',
        clean: true,
        assetModuleFilename: '[name].[ext]'
    },
    devtool: 'source-map',
    devServer : {
        host: '0.0.0.0',
        static: {
            directory: path.resolve(__dirname, 'dist'),
        },
        port: port,
        open: true,
        hot: true,
        compress: true,
        historyApiFallback: true,
    },                                                                                                    
    module: {
        rules: [
            {
                test: /\.(css|scss)$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader',
                ],
            },
            {
                test: /\.html$/,
                use: [
                    {
                        loader: 'html-loader'
                    }
                ]
            },
            {
                test: /\.(js|jsx)$/,
                exclude: /node_moduls/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env'],
                    },
                },
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                use: {
                    loader: 'file-loader',
                    options: {
                        name: '[name].[hash].[ext]',
                        outputPath: 'images'
                    }
                },
                type: 'asset/resource',
            },
        ],
    },
    plugins: [
        new HtmlWebpackPlugin({
            title: 'rentify-app-django"',
            filename: 'index.html',
            template: 'src/index.html',
        }),
        // new BundleAnalyzerPlugin(),
    ]
}