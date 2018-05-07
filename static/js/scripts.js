$(document).ready(function(){

// var modal = ;

// Get the image and insert it inside the modal - use its "alt" text as a caption
// var img = ;
// var modalImg = 
// var captionText = 
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


  $(".one").text(img_d);

  $(".two").text(loc_d);

  $(".three").text(cat_d);


})
// Get the <span> element that closes the modal
// var span = ;

// When the user clicks on <span> (x), close the modal
$(".close").click(function() {
//   modal.style.display = "none";
  $('#myModal').css('display', "none");
  $('#modal-details').css('display', 'none')
})
})

