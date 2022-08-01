document.querySelector(".mobile_nav_button").addEventListener("click", function() {
	document.querySelector(".zanaves").classList.add("open");
	document.querySelector(".mobile_nav").classList.add("open");
})

document.querySelector(".zanaves").addEventListener("click", function() {
	document.querySelector(".zanaves").classList.toggle("open");
	document.querySelector(".mobile_nav").classList.toggle("open");
})