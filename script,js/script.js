document.addEventListener("DOMContentLoaded", () => {
  // Hamburger Menu Toggle
  const menuToggle = document.getElementById("menu-toggle");
  const mobileMenu = document.getElementById("mobile-menu");

  if (menuToggle && mobileMenu) {
    menuToggle.addEventListener("click", () => {
      mobileMenu.classList.toggle("hidden");
    });
  }

  // Card Hover Animations
  const cards = document.querySelectorAll(".transform");
  cards.forEach(card => {
    card.addEventListener("mouseover", () => {
      card.classList.add("scale-105");
    });
    card.addEventListener("mouseleave", () => {
      card.classList.remove("scale-105");
    });
  });
});
