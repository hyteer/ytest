(function(){
  $('.menu-left').click(function(){
    $('header').toggleClass('active')
    $('.intro').toggleClass('active')
    $('section').toggleClass('active')
    $('#menu-left').toggleClass('active')
    $('footer').toggleClass('active')
  })
  $('.menu-right').click(function(){$('#menu-right').toggleClass('active')})
})()