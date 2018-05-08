$(document).ready(function(){

  $('.category-button').click(function(event) {
    event.preventDefault()
    var btn_value = $(this).text()

    $.ajax({
      'url': 'category/',
      'type': 'GET',
      'data': {
        category_name: btn_value
      },
      'success': function(resp) {
        $('.container-fluid').empty()
        $('.container-fluid').html(resp)
      },

    })
  })
  
  $('option').click(function() {
    if ($(this).is(':selected')) {
      option_value = $(this).text()
      $.ajax({
        'url': 'location/',
        'type': 'GET',
        'data': {
          location_name: option_value
        },
        'success': function(resp) {
          $('.container-fluid').empty()
          $('.container-fluid').html(resp)
        },

      })
    }

  })


$('.myimage').click(function(){
    $('#myModal').css('display', "block")
    $("#modal-con").attr('src',$(this).attr('src'))
    $('#caption').html()= $(this).attr('alt')
})

$('button#details').click(function() {

  $('#modal-details').css('display', 'block')

  img_d = $(this).data("description");

  loc_d = $(this).data("location");

  cat_d = $(this).data("category");


  $(".oneone").text(img_d);

  $(".twotwo").text(loc_d);

  $(".threethree").text(cat_d);


})

$(".close").click(function() {
  $('#myModal').css('display', "none");
  $('#modal-details').css('display', 'none')
})
})
