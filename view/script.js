$(document).ready(function() {
    $('.btn-translate').on('click', function() {
        var inputText = $('.humantext')[0].value;
        $.ajax({
            'url': 'http://localhost:5000/translate',
            'method': 'POST',
            'data': {
                'translateText': inputText,
                'president': 'T' // fix later
            }
        }).done(function(resp) {
            $('.trumptext')[0].value = resp;
        });
    });
});
