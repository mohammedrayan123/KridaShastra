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
  