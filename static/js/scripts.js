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

// Get the <span> element that closes the modal
// var span = ;

// When the user clicks on <span> (x), close the modal
$(".close").click(function() {
//   modal.style.display = "none";
  $('#myModal').css('display', "none");
})
})

