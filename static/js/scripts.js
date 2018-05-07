$(document).ready(function(){

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

