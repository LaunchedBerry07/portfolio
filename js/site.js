"use strict";

document.documentElement.classList.add("js");

const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector(".primary-nav");

if (menuButton && navigation) {
  const closeMenu = (returnFocus = false) => {
    menuButton.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
    menuButton.querySelector(".menu-toggle-label").textContent = "Menu";
    if (returnFocus) menuButton.focus();
  };

  menuButton.addEventListener("click", () => {
    const isOpen = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!isOpen));
    navigation.classList.toggle("is-open", !isOpen);
    menuButton.querySelector(".menu-toggle-label").textContent = isOpen ? "Menu" : "Close";
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menuButton.getAttribute("aria-expanded") === "true") {
      closeMenu(true);
    }
  });

  document.addEventListener("click", (event) => {
    if (menuButton.getAttribute("aria-expanded") === "true" &&
        !navigation.contains(event.target) && !menuButton.contains(event.target)) {
      closeMenu();
    }
  });
}
