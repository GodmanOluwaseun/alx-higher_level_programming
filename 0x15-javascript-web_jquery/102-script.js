$(document).ready(function() {
  $('#btn_translate').click(function() {
    const code = $('#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + code;

    $.getJSON(url,function(data) {
      const greeting = data.hello;
      $('#hello').text(greeting);
    }).fail(function() {
      console.error('Error');
    });
  });
});
