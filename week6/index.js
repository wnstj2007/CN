var express = require('express');
var bodyParser = require('body-parser');
var router = require('./routes/home');
var methodOverride = require('method-override');
var app = express();
var port = 3000

app.set('view engine', 'ejs');
app.use(express.static(__dirname+'/public'));
app.use('/', router);
app.use('/about', router);
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:true}));
app.use(methodOverride('_method'));

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});
