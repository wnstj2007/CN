var express = require('express');
var router = express.Router();
var passport = require('../config/201802096_passport.js');

router.get('/login', (req, res) => {
	res.render('auth/login');
});

router.get('/logout', (req, res) => {
	req.logout();
	res.redirect('/');
});

router.get('/google',
	passport.authenticate('google', { scope : ['profile'] })
);

router.get('/google/callback',
	passport.authenticate('google'), authSuccess
);

function authSuccess(req, res) {
	res.redirect('/');
}

module.exports = router;
