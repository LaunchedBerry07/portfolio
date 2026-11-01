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

  const filterButtons = [...document.querySelectorAll('[data-project-filter]')];
  const clearFiltersButton = document.querySelector('[data-project-filter-clear]');
  const cards = [...document.querySelectorAll('.case-card')];
  const status = document.getElementById('portfolio-filter-status');
  const selectedServices = new Set();

  const renderFilters = () => {
    filterButtons.forEach((button) => {
      const active = button.dataset.projectFilter === 'all' ? selectedServices.size === 0 : selectedServices.has(button.dataset.projectFilter);
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    let visibleCount = 0;
    cards.forEach((card) => {
      const services = (card.dataset.service || '').split(/\s+/).filter(Boolean);
      const visible = selectedServices.size === 0 || services.some((service) => selectedServices.has(service));
      card.hidden = !visible;
      if (visible) visibleCount += 1;
    });
    if (status) status.textContent = `Showing ${visibleCount} of ${cards.length} case studies`;
  };

  filterButtons.forEach((button) => button.addEventListener('click', () => {
    const service = button.dataset.projectFilter;
    if (service === 'all') { selectedServices.clear(); renderFilters(); return; }
    if (selectedServices.has(service)) selectedServices.delete(service);
    else selectedServices.add(service);
    renderFilters();
  }));
  if (clearFiltersButton) clearFiltersButton.addEventListener('click', () => {
    selectedServices.clear();
    renderFilters();
  });
  if (filterButtons.length) renderFilters();
});
