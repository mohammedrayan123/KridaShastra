document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    
    if (!themeToggle) return; // Prevents errors if element is not found
  
    const storedTheme = localStorage.getItem("theme") || "light"; // Default theme
    document.documentElement.setAttribute("data-theme", storedTheme);
    themeToggle.checked = storedTheme === "synthwave";
  
    themeToggle.addEventListener("change", function () {
      const newTheme = themeToggle.checked ? "synthwave" : "light";
      document.documentElement.setAttribute("data-theme", newTheme);
      localStorage.setItem("theme", newTheme); // Save theme choice
    });
  });
  