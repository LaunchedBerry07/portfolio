document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.current-year').forEach((node) => {
    node.textContent = String(new Date().getFullYear());
  });

  const menuButton = document.querySelector('.site-nav__toggle');
  const menu = document.getElementById('primary-navigation');
  if (menuButton && menu) {
    menuButton.addEventListener('click', () => {
      const expanded = menuButton.getAttribute('aria-expanded') === 'true';
      menuButton.setAttribute('aria-expanded', String(!expanded));
      menuButton.setAttribute('aria-label', expanded ? 'Open navigation menu' : 'Close navigation menu');
      menu.classList.toggle('is-open', !expanded);
      const icon = menuButton.querySelector('i');
      if (icon) icon.className = expanded ? 'fa-solid fa-bars' : 'fa-solid fa-xmark';
    });
    menu.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => {
      menu.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.setAttribute('aria-label', 'Open navigation menu');
      const icon = menuButton.querySelector('i');
      if (icon) icon.className = 'fa-solid fa-bars';
    }));
  }

  const filterButtons = document.querySelectorAll('[data-project-filter]');
  const cards = document.querySelectorAll('.case-card');
  const applyFilter = (category) => {
    filterButtons.forEach((button) => {
      const active = button.dataset.projectFilter === category;
      button.classList.toggle('bg-navy', active);
      button.classList.toggle('text-white', active);
      button.classList.toggle('bg-white', !active);
      button.classList.toggle('text-navy', !active);
      button.setAttribute('aria-pressed', String(active));
    });
    cards.forEach((card) => {
      const visible = category === 'all' || card.dataset.category === category;
      card.hidden = !visible;
    });
  };
  filterButtons.forEach((button) => button.addEventListener('click', () => applyFilter(button.dataset.projectFilter)));
});
