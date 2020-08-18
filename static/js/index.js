$(document).ready(function () {
    

	$(window).scroll(function () {
	  var scrollPos = $('body').scrollTop();
	  if (scrollPos > 0) {
		$('.navbar-one').addClass('show-color');
		$('.scrollTop').addClass('show-button');
		$('.logo').addClass('logo-dis-none');
	  } else {
		$('.navbar-one').removeClass('show-color');
		$('.scrollTop').removeClass('show-button');
		$('.logo').removeClass('logo-dis-none');
	  }
  
	});
  });

  $(document).ready(function(){
	$('#nav-icon2').click(function(){
		  $(this).toggleClass('collapsed');
		  if ($(this).hasClass('collapsed')) {
				$('nav').addClass('show-color')
				$('.logo').addClass('logo-dis-none');
		  } else {
				$('nav').removeClass('show-color')
				$('.logo').removeClass('logo-dis-none');
		  }
	});
});
//////////////////////////////////////////////////////////////////////////////////






$("#newUser").click(function () {
	$("#reg-h").text("Registration");
	$(".logo-f").css({
	  "width": "120px",
	  "height": "120px",
	  "top": "10px" });
  
	$("#login-form").fadeOut(200);
	$("#registration-form").delay(300).fadeIn(500);
	$(".other-options").fadeOut(200);
  });
  
  $("#signup-btn,#getpass-btn").click(function () {
	$("#reg-h").text("Log in");
	$(".logo-f").css({
	  "width": "150px",
	  "height": "150px",
	  "top": "30px" });
  
  
	$("#registration-form,#fpass-form").fadeOut(200);
	$("#login-form").delay(300).fadeIn(500);
	$(".other-options").fadeIn(300);
  });
  
  $("#fPass").click(function () {
	$("#reg-h").text("Forgotten password");
	$(".logo-f").css({
	  "width": "190px",
	  "height": "190px",
	  "top": "40px" });
  
  
	$("#login-form").fadeOut(200);
	$("#fpass-form").delay(300).fadeIn(500);
	$(".other-options").fadeOut(200);
  });
  
  
  
  
  
  
  
  document.getElementById("form-open").addEventListener("click",function(){
	document.querySelector(".screen").style.display = "block";
  
  })
  
  document.querySelector(".close").addEventListener("click",function(){
	document.querySelector(".screen").style.display = "none";
  })
  


  document.getElementById("nav-form-open").addEventListener("click",function(){
	document.querySelector(".screen").style.display = "block";
  
  })
  

  ///////////////// log in only/////////////////////

  document.getElementById("nav-login-form-open").addEventListener("click",function(){
	document.querySelector(".screen-one").style.display = "block";
  
  })
  
  document.querySelector(".close-one").addEventListener("click",function(){
	document.querySelector(".screen-one").style.display = "none";
  })
  



  $("#newUser-one").click(function () {
	$("#reg-h-one").text("Log in");
	$(".logo-f-one").css({
	  "width": "120px",
	  "height": "120px",
	  "top": "10px" });
  
	$("#fpass-form-one").fadeOut(200);
	$("#login-form-one").delay(300).fadeIn(500);

  });
  
  $("#signup-btn-one,#getpass-btn-one").click(function () {
	$("#reg-h-one").text("Log in");
	$(".logo-f-one").css({
	  "width": "150px",
	  "height": "150px",
	  "top": "30px" });
  
  
	$("#registration-form-one,#fpass-form-one").fadeOut(200);
	$("#login-form-one").delay(300).fadeIn(500);
	$(".other-options-one").fadeIn(300);
  });
  
  $("#fPass-one").click(function () {
	$("#reg-h-one").text("Forgotten password");
	$(".logo-f-one").css({
	  "width": "190px",
	  "height": "190px",
	  "top": "40px" });
  
  
	$("#login-form-one").fadeOut(200);
	$("#fpass-form-one").delay(300).fadeIn(500);
	$(".other-options-one").fadeOut(200);
  });
  
  ///////////////////////////////choose file cv ////////////////

  var loader = function(e){
	  let file = e.target.files;
	  let show="<span>Selected file : </span>" + file[0]

	  let output = document.getElementById("selector");
	  output.innerHTML = show;
	  output.classList.add("active");
	  
  };


  // event listner for input

  let fileInput = document.getElementById("file");
  fileInput.addEventListener("change", loader);


  ///////////////////////////////choose file image ////////////////

  var loader = function(e){
	let image = e.target.files;
	let show="<span>Selected file : </span>" + image[0]

	let output = document.getElementById("pic");
	output.innerHTML = show;
	output.classList.add("active");
	
};


// event listner for input

let imageInput = document.getElementById("image");
imageInput.addEventListener("change", loader);

/////////////////////////////////////////////////////////scroll to top//////////////////


$(function(){
    $("#back-to-top").hide();
    $(window).scroll(function(){
      if($(this).scrollTop() > 60){
        $("#back-to-top").fadeIn();
      }
      else{
         $("#back-to-top").fadeOut();
      }
    });
    $("#back-to-top").click(function(){
      $("html,body").animate({
        scrollTop : 0
      },500);
      return false;
    });
  });
