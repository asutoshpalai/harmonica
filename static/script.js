$(document).ready( function () {

  var formSubmit = function (e) {
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
        if($.inArray(ret, ['Icorrect Data', 'Incorrect HTTP METHOD', 'Vote Falied', 'Comment Falied'] ) < 0) {
          $('li#track' + tid).html(ret);
          $('li#track' + tid + ' form.vote').on('submit', formSubmit);
          $('li#track' + tid + ' form.comment').on('submit', formSubmit);
        }
        else 
          console.log(ret);
      },
      error: function(xhr, status, error) {
        if( status == 'error' && error.toUpperCase() == 'INTERNAL SERVER ERROR' ) {
          alert('You can\'t vote twice');

        }

      }
    });
  }

  $('form.vote').on('submit', formSubmit);

  $('form.comment').on('submit', formSubmit);

});
