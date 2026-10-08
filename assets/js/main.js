(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');

  function setNav(open) {
    toggle.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      setNav(toggle.getAttribute('aria-expanded') !== 'true');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) setNav(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        setNav(false);
        toggle.focus();
      }
    });
  }

  // Een "proefrit"-knop bij een model kiest dat model alvast in het formulier.
  var modelSelect = document.getElementById('f-model');
  document.querySelectorAll('[data-model]').forEach(function (link) {
    link.addEventListener('click', function () {
      if (modelSelect) modelSelect.value = link.getAttribute('data-model');
    });
  });

  // Statische hosting heeft geen server: het formulier opent een ingevulde e-mail.
  // Koppel later eventueel Formspree of een Vercel-functie via het action-attribuut.
  var form = document.getElementById('lead-form');
  if (form) {
    var status = form.querySelector('.form-status');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var name = form.elements.naam;
      var phone = form.elements.telefoon;
      var missing = [name, phone].filter(function (f) { return !f.value.trim(); });

      [name, phone].forEach(function (f) { f.setAttribute('aria-invalid', String(missing.indexOf(f) !== -1)); });
      if (missing.length) {
        status.textContent = 'Vul je naam en telefoonnummer in, dan bellen we je terug.';
        missing[0].focus();
        return;
      }

      var model = form.elements.model.value;
      var body = [
        'Naam: ' + name.value.trim(),
        'Telefoon: ' + phone.value.trim(),
        'Woonplaats: ' + form.elements.woonplaats.value.trim(),
        'Interesse in: ' + model
      ].join('\n');
      var subject = 'Proefrit aanvraag: ' + model;
      window.location.href = 'mailto:info@slim-mobiel.nl?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      status.textContent = 'Je e-mailprogramma opent met je aanvraag. Verstuur de e-mail om de proefrit aan te vragen.';
    });
  }

  var year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
