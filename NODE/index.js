var path = require('path'),
    request = require('request'),
    express = require('express'),
    session = require('express-session'),
    bodyParser = require('body-parser'),
    passport = require('passport'),
    cors = require('cors');
    mysql= require('mysql');
    pug = require('pug');
    var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'mbriseno',
    password : 'm4r10Br1s3n0!',
    database : 'Mario'
    });



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
    if (err){ res.send(err); throw err;
}
    res.send(body);
  });
});

app.get('/',function(req,res){
var url2 =pug.renderFile('loggin.js',{});
res.send(url2);
});


app.post('/hello', function(req, res){
  var url3 =pug.renderFile('hello.js',{});
  console.log(req.body);
});


app.get('/register',function(req,res){
var url4 =pug.renderFile('register.js',{});
res.send(url4);
});






 

