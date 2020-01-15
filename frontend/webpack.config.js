"use strict";
const path = require('path'),
    webpack = require('webpack'),
    HtmlWebpackPlugin = require("html-webpack-plugin");
const {CleanWebpackPlugin} = require("clean-webpack-plugin");

module.exports = (env, argv) => ({
    devtool: 'source-map',

    entry: {
        'index': 'index.js',
    },

    output: {
        path: path.resolve('public/build'),
        filename: '[name].[hash].js',
        publicPath: '/'
    },

    resolve: {
        extensions: ["*", ".js", ".jsx", ".scss"],

        modules: [
            "node_modules",
            path.resolve(__dirname, "src/"),
        ]
    },

    module: {
        rules: [
            {
                test: /\.jsx$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.js$/,
                loader: 'babel-loader',
                exclude: /node_modules/,
            },
            {
                test: /\.css$/,
                use: [
                    {
                        loader: 'style-loader',
                    },
                    {
                        loader: 'css-loader',
                        options: {sourceMap: true}
                    },
                    {
                        loader: 'postcss-loader',
                        options: {sourceMap: true}
                    },
                    {
                        loader: "sass-loader",
                        options: {sourceMap: true}
                    }
                ]
            },
            {
                test: /\.(jpe?g|png|gif|ico|svg)$/,
                loader: 'url-loader',
                options: {
                    limit: 10000
                }
            },
            {
                test: /\/fonts\/.*\.(woff2?|ttf|eot|svg)$/,
                loader: 'file-loader',
                options: {
                    name: "fonts/[name].[ext]"
                }
            }
        ],
    },

    plugins: [
        new CleanWebpackPlugin({
            dry: false,
            verbose: true
        }),
        new HtmlWebpackPlugin({
            favicon: 'public/favicon.ico',
            template: "public/index.html"
        }),
    ],

    optimization: {
        moduleIds: 'hashed',
        runtimeChunk: true,
        splitChunks: {
            cacheGroups: {
                vendor: {
                    test: /[\\/]node_modules[\\/]/,
                    name: "vendor",
                    chunks: "all"
                }
            }
        }
    }
});
