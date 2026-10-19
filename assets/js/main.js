(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('#primary-navigation');
  if (!toggle || !nav) return;
  const label = toggle.querySelector('.visually-hidden');
  toggle.addEventListener('click', () => {
    const isOpen = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!isOpen));
    nav.classList.toggle('is-open', !isOpen);
    if (label) label.textContent = isOpen ? 'Open navigation' : 'Close navigation';
  });
  nav.addEventListener('click', event => {
    if (event.target.closest('a')) {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      if (label) label.textContent = 'Open navigation';
    }
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && nav.classList.contains('is-open')) {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('is-open');
      toggle.focus();
      if (label) label.textContent = 'Open navigation';
    }
  });
  const year = document.querySelector('#current-year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
