document.addEventListener('DOMContentLoaded', function() {
    // Example: Simple alert on form submission (you can expand this)
    const form = document.querySelector('.contact-form form');
    if (form) {
      form.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('Thank you for contacting us. We will get back to you soon.');
        form.reset();
      });
    }
  });


  document.addEventListener("DOMContentLoaded", function() {
    const searchBtn = document.getElementById("searchBtn");
    const searchContainer = document.getElementById("searchContainer");
    const searchInput = document.getElementById("searchInput");
    const notificationBtn = document.getElementById("notificationBtn");
    const notificationDropdown = document.getElementById("notificationDropdown");
    const mobileMenuBtn = document.querySelector(".dropdown [role='button']");
    const mobileMenu = document.getElementById("mobileMenu");

    // Toggle search input visibility
    searchBtn.addEventListener("click", function() {
        searchContainer.classList.toggle("hidden");
        if (!searchContainer.classList.contains("hidden")) {
            searchInput.focus(); // Auto-focus on input
        }
    });

    // Close search when clicking outside
    document.addEventListener("click", function(event) {
        if (!searchContainer.contains(event.target) && !searchBtn.contains(event.target)) {
            searchContainer.classList.add("hidden");
        }
    });

    // Toggle notification dropdown
    notificationBtn.addEventListener("click", function() {
        notificationDropdown.classList.toggle("hidden");
    });

    // Close notifications when clicking outside
    document.addEventListener("click", function(event) {
        if (!notificationDropdown.contains(event.target) && !notificationBtn.contains(event.target)) {
            notificationDropdown.classList.add("hidden");
        }
    });

    // Toggle mobile menu
    mobileMenuBtn.addEventListener("click", function() {
        mobileMenu.classList.toggle("hidden");
    });

    // Close mobile menu when clicking outside
    document.addEventListener("click", function(event) {
        if (!mobileMenu.contains(event.target) && !mobileMenuBtn.contains(event.target)) {
            mobileMenu.classList.add("hidden");
        }
    });
});

  