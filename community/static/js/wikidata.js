function addOption(text,value){
    var select = document.getElementById("wiki-data-select");
    select.options[select.options.length] = new Option(text, value, false, false);
}

function removeAllOptions(){
    var select = document.getElementById("wiki-data-select");
    select.options.length = 0;
}

$( document ).ready(function() {


    var searchInput = document.getElementsByClassName("search")[1];
    var deleteIcon = document.getElementsByClassName('delete icon');

        if (deleteIcon.length > 0) {
            for(var i = 0; i < deleteIcon.length; i++) {
                (function(index) {
                    deleteIcon[index].addEventListener('click', (event) => {
                        console.log(event.target.value);
                    });
                })(i);
            }
        };
    searchInput.addEventListener('input', (event) => {
        let value = event.target.value;
        function callWikiData(){

            return $.ajax({
                        type: 'GET',
                        url: 'https://www.wikidata.org/w/api.php?action=wbsearchentities&limit=10&format=json&language=en&continue=0&search='+value,
                        contentType: 'application/json',
                        dataType:'jsonp',
                        responseType:'application/json',
                        async:false,
                        xhrFields: {
                        withCredentials: true
                        },
                        headers: {
                        'Access-Control-Allow-Credentials' : true,
                        'Access-Control-Allow-Origin':'*',
                        'Access-Control-Allow-Methods':'GET',
                        'Access-Control-Allow-Headers':'application/json',
                        }
                    });
                };

        $.when( callWikiData() ).done(function(response){
            console.log(response.search);
            removeAllOptions();
            for (let index = 0; index < response.search.length; index++) {
                const element = response.search[index];
                addOption(element.id+" ~~ "+element.label+" ~~ "+element.description,JSON.stringify(element).replace(new RegExp("\"", 'g'),"\\\'"));
                // addOption(element.id+" ~~ "+element.label+" ~~ "+element.description,"{\\\'id\\\':\\\'"+element.id+"\\\',\\\'uri\\\':\\\'"+element.concepturi+"\\\',\\\'label\\\':\\\'"+element.label+"\\\',\\\'desc\\\':\\\'"+element.description+"\\\',\\\'match-text\\\':\\\'"+element.match.text+"\\\'}");
            }
        });
    });
});