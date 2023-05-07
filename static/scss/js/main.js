let menu = document.querySelector('#menu-bars');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle("fa-xmark");
    navbar.classList.toggle("active");
}
window.onscroll = () =>{
    menu.classList.remove("fa-xmark");
    navbar.classList.remove("active");
}

//slider

var swiper = new Swiper(".home-slider", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    loop: true
  });


var swiper = new Swiper(".review-slider", {
    spaceBetween: 20,
    centeredSlides: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    loop: true,
    breakpoints: {
      // when window width is >= 0px comma chai na birsine :<
      0: {
        slidesPerView: 1,
      },
      // when window width is >= 480px
      480: {
        slidesPerView: 2,
      },
      // when window width is >= 991px
      1024: {
        slidesPerView: 3,
      }
    }
   
  });
  
//quantity
$document.ready(function(){

  var quantitiy=0;
     $('.quantity-right-plus').click(function(e){

          // Stop acting like a button
          e.preventDefault();
          // Get the field name
          var quantity = parseInt($('#quantity').val());

          // If is not undefined

              $('#quantity').val(quantity + 1);


              // Increment

      });

       $('.quantity-left-minus').click(function(e){
          // Stop acting like a button
          e.preventDefault();
          // Get the field name
          var quantity = parseInt($('#quantity').val());

          // If is not undefined

              // Increment
              if(quantity>0){
              $('#quantity').val(quantity - 1);
              }
      });

  });
// for category food div clickable
// var element = document.getElementsByClassName("category-pick"); //grab the element
// element.onclick = function() { alert('1')
// }

// var myDiv = document.getElementsByClassName("category-pick");
function disp_alert()
{
  if (document.getElementsByClassName("abc")[0].innerText =='Logout'){
    alert("you are logged out");
  }
  else if(document.getElementsByClassName("abc")[0].innerText === 'Sign In'){
    alert("you are signed in");
    
  }
}
