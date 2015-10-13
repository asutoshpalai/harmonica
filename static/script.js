$(document).ready( function () {

  $('form.vote').on('submit', function (e) {
    e.preventDefault();

    var form = $(this);
    var postData = form.serializeArray();
    var url = form.attr('action');
    var tid = this.track.value;
    console.log(tid);

    $.ajax({
      url: url,
      type: 'post',
      data: postData,
      success: function(ret){
        if($.inArray(ret, ['Icorrect Data', 'Incorrect HTTP METHOD', 'Vote Falied'] ) < 0) {         
          $('li#track' + tid).html(ret);
        }
        else 
          console.log(ret);
      }

    });


  });
  
});
