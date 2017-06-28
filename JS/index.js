var path = require('path'),
    request = require('request'),
    express = require('express'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    passport = require('passport'),
    cors = require('cors');

var app = express();
app.set('port', (process.env.PORT || 4007));
app.set('view engine', 'pug');
app.use(cors());
app.use(session({ secret: 'anything', resave: true, saveUninitialized: true })); 
app.use(passport.initialize()); app.use(passport.session()); 
app.use(express.static(path.join(__dirname, 'public'))); app.use(bodyParser.json()); 

app.use(bodyParser.urlencoded({extended: true}));
app.locals.site = {
  title: 'Home'
};

app.listen(app.get('port'), function() {
  console.log('Server started: http://localhost:' + app.get('port') + '/');
});

app.post('/search', function(req, res){
  console.log(req.body);
  var url = "http://search.sep.gob.mx/solr/cedulasCore/select?fl=%2A%2Cscore&q="+encodeURI(req.body.name)+"&start=0&rows=100&facet=true&indent=on&wt=json";
  request(url, function (err, data, body) {
    if (err){ res.send(err); throw err; }
    res.send(body);
  });
});
