/* irock - v1.0.0 - 2017-06-21*/
var url = 'http://irock.enroute.xyz:4000/search';

function search(url, callback) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        resolve(JSON.parse(xhr.response).response.docs);
      }
    }

    xhr.open('POST', url, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.send('name='+searchInput.value);
  });
}

var section = null,
    searchInput = null
    searchButton = null;

var handle_data = function(data){
  console.log(data);
  section.innerHTML = "";
  data.forEach(function(element){
    var article = document.createElement('article');

    var title = document.createElement('h3');
    title.innerHTML = element.nombre + (' '+element.paterno||'') + (' '+element.materno||'');

    var p = document.createElement('p');
    p.innerHTML = element.titulo;

    var p_two = document.createElement('p');
    p_two.innerHTML = element.numCedula;

    article.append(title);
    article.append(p);
    article.append(p_two);

    section.append(article);
  });
}

var search_function = function(){
  search(url).then(handle_data);
}

var init = function(){
  section = document.getElementById('section');
  searchInput = document.getElementById('search-input');
  searchButton = document.getElementById('search-button');
  searchButton.addEventListener('click', search_function);
}
