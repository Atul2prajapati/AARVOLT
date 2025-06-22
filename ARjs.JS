
  console.log("ARjs.JS is loaded");
  
  document.addEventListener("DOMContentLoaded", function () {
  console.log("ARjs.JS is loaded");

  const icon = document.getElementById("searchIcon");
  const input = document.getElementById("searchInput");

  if (icon && input) {
    icon.addEventListener("click", function () {
      const query = input.value.trim();
      alert("You searched for: " + query);
    });
  } else {
    console.error("Search icon or input not found in DOM");
  }
});