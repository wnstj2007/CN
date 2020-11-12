var passport = require('passport');
var GoogleStrategy = require('passport-google-oauth2').Strategy;

passport.serializeUser(function(user, done) {
	done(null, user);
});

passport.deserializeUser(function(obj, done) {
	done(null, obj);
});

passport.use(new GoogleStrategy(
	{
		clientID : '614781975294-oht6irncdfoib4rhk1cfga95k42osa8i.apps.googleusercontent.com',
		clientSecret : 'yzKxqkgcumUI1yAVKubply21',
		callbackURL : '/auth/google/callback',
		passReqToCallback : true
	}, function(request, accessToken, refreshToken, profile, done) {
		console.log('profile: ', profile);
		var user = profile;
		
		done(null, user);
	}
));

module.exports = passport;
