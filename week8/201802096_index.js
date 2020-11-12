var express = require('express');
var app = express();
var passport = require('passport');
var session = require('express-session');

app.set('view engine', 'ejs');
app.use(session({secret:'MySecret', resave:false, saveUninitialized:true}));

app.use(passport.initialize());
app.use(passport.session());

app.use('/', require('./routes/201802096_main'));
app.use('/auth', require('./routes/201802096_oauth'));

var port = 443;
var https = require('https');
var fs = require('fs');
var opt = {
    key: fs.readFileSync('./key.pem'),
    cert: fs.readFileSync('./cert.pem')
};

https.createServer(opt, app).listen(port, () => {});
