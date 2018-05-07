$(document).ready(function () {
    $('button#copylink').on('click', function () {
        // Get the text field
        var copyLink = $('input#imageurl')

        // Select the text field
        copyLink.select()

        // Copy the text inside the text field
        document.execCommand('Copy')

        // Alert the copied text
        alert('Link Copied!')
    })
})

$('.menu-icon').on('click', function () {
    $('nav ul').toggleClass('hidden')
})