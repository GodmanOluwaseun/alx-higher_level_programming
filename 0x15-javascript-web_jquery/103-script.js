$(document).ready(function() {
  function fetchTranslate() {
    const code = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + code;

    $.getJSON(url,function(data) {
      const greeting = data.hello;
      $('#hello').text(greeting);
    }).fail(function() {
      console.error('Error');
    });
  }


  $('#btn_translate').click(function() {
    fetchTranslate();
  });

  $('#language_code').keypress(function(event) {
    if (event.which === 13) {
      fetchTranslate();
    }
  });
});
