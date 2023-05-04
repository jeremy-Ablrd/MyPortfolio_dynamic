// Get the current page URL
const currentPage = window.location.href;

// Get all of the links in the navigation bar
const navLinks = document.querySelectorAll(".nav_link_page a");

// Loop through the links and check if the URL matches the current page
navLinks.forEach((link) => {
	if (link.href === currentPage) {
		// If the link matches the current page, add the 'active' class
		link.classList.add("active");
	} else {
		// Otherwise, remove the 'active' class
		link.classList.remove("active");
	}
});
