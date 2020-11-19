var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', (req, res) => {
	res.sendFile(__dirname + '/201802096_client.html');
});

var count = 1;
var client_list = [];
io.on('connection', (socket) => {
	console.log('User connected: ' + socket.id)
	var name = 'user' + count;
	count += 1;
	io.to(socket.id).emit('name', name);
	client_list.push(socket.id);
	socket.on('disconnect', () => {
		console.log('User disconnected: ' + socket.id);
		//client_list.remove(socket.id);
		const idx = client_list.indexOf(socket.id)
		if (idx > -1) client_list.splice(idx, 1)
		io.emit('send list', ''+client_list.join());
	});
	io.emit('send list', ''+client_list.join());
	socket.on('send message', (name, text) => {
		console.log(name+' : '+text);
		io.emit('send message', name+' : '+text);
	});
});

http.listen(3000, () => {
	console.log('server on!');
});
