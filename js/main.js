/* ═══════════════════════════════════════════════════════════
   main.js — Portfolio Interactions
   Nav, Typewriter, Scroll Reveal, 3D Tilt, Timeline,
   Project Filter, Contact Form, Back-to-top
   ═══════════════════════════════════════════════════════════ */

(function () {
  'use strict';

  /* ──────────────────────────────────
     1. Navigation
  ────────────────────────────────── */
  const nav        = document.getElementById('nav');
  const navToggle  = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  const navLinks   = document.querySelectorAll('.nav-link');
  let menuOpen     = false;

  // Scroll blur
  window.addEventListener('scroll', () => {
    nav.classList.toggle('scrolled', window.scrollY > 60);
    updateActiveLink();
  }, { passive: true });

  // Mobile toggle
  navToggle.addEventListener('click', () => {
    menuOpen = !menuOpen;
    navToggle.setAttribute('aria-expanded', menuOpen);
    mobileMenu.setAttribute('aria-hidden', !menuOpen);
    mobileMenu.classList.toggle('open', menuOpen);
    document.body.style.overflow = menuOpen ? 'hidden' : '';
  });
  // Close on mobile link click
  document.querySelectorAll('.mobile-link').forEach(l => {
    l.addEventListener('click', () => {
      menuOpen = false;
      mobileMenu.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  // Active link on scroll
  const sections = document.querySelectorAll('section[id]');
  function updateActiveLink() {
    const scroll = window.scrollY + 120;
    sections.forEach(sec => {
      const top = sec.offsetTop;
      const bottom = top + sec.offsetHeight;
      const id = sec.getAttribute('id');
      const link = document.querySelector(`.nav-link[href="#${id}"]`);
      if (link) link.classList.toggle('active', scroll >= top && scroll < bottom);
    });
  }
  updateActiveLink();

  /* ──────────────────────────────────
     2. Hero Typewriter
  ────────────────────────────────── */
  const roleEl = document.getElementById('hero-role');
  const roles  = [
    'Web Developer',
    'AI Developer',
    'Chatbot & Voice Agent Builder',
    'SaaS Product Developer',
    'Electronics & Telecom Engineer',
  ];
  let roleIdx  = 0;
  let charIdx  = 0;
  let deleting = false;
  let delay    = 120;

  function typeRole() {
    const current = roles[roleIdx];
    if (!deleting) {
      roleEl.textContent = current.slice(0, charIdx + 1);
      charIdx++;
      if (charIdx === current.length) {
        deleting = true;
        delay = 2000; // pause at end
      } else {
        delay = 80 + Math.random() * 40;
      }
    } else {
      roleEl.textContent = current.slice(0, charIdx - 1);
      charIdx--;
      if (charIdx === 0) {
        deleting = false;
        roleIdx  = (roleIdx + 1) % roles.length;
        delay    = 400;
      } else {
        delay = 45;
      }
    }
    setTimeout(typeRole, delay);
  }
  setTimeout(typeRole, 800);

  /* ──────────────────────────────────
     3. Scroll Reveal (IntersectionObserver)
  ────────────────────────────────── */
  const reveals = document.querySelectorAll('[data-reveal]');
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  reveals.forEach(el => revealObs.observe(el));

  /* ──────────────────────────────────
     4. Timeline line draw
  ────────────────────────────────── */
  const timeline = document.getElementById('timeline');
  if (timeline) {
    const tlObs = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        timeline.classList.add('animated');
        tlObs.disconnect();
      }
    }, { threshold: 0.2 });
    tlObs.observe(timeline);
  }

  /* ──────────────────────────────────
     5. Project Card 3D Tilt
  ────────────────────────────────── */
  const projectCards = document.querySelectorAll('.pcard');
  const MAX_TILT = 8; // degrees for visible 3D pop

  projectCards.forEach(card => {
    // Inject card sheen div programmatically
    if (!card.querySelector('.card-sheen')) {
      const sheen = document.createElement('div');
      sheen.className = 'card-sheen';
      card.appendChild(sheen);
    }
    card.addEventListener('mousemove', onTiltMove);
    card.addEventListener('mouseleave', onTiltLeave);
  });

  function onTiltMove(e) {
    const card  = e.currentTarget;
    const rect  = card.getBoundingClientRect();
    const cx    = rect.left + rect.width  / 2;
    const cy    = rect.top  + rect.height / 2;
    const dx    = (e.clientX - cx) / (rect.width  / 2);
    const dy    = (e.clientY - cy) / (rect.height / 2);
    const rotX  = -dy * MAX_TILT;
    const rotY  =  dx * MAX_TILT;
    card.style.transform = `perspective(1000px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.025)`;
    card.style.transition = 'transform 0.08s ease-out';

    // Lighting/Sheen position mapping
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const px = (x / rect.width) * 100;
    const py = (y / rect.height) * 100;
    card.style.setProperty('--sheen-x', `${px}%`);
    card.style.setProperty('--sheen-y', `${py}%`);
  }

  function onTiltLeave(e) {
    const card = e.currentTarget;
    card.style.transform = '';
    card.style.transition = 'transform 0.6s cubic-bezier(0.25,0.8,0.25,1)';
  }

  /* ──────────────────────────────────
     6. Portrait 3D Tilt
  ────────────────────────────────── */
  const portraitTilt = document.getElementById('portrait-tilt');
  if (portraitTilt) {
    if (!portraitTilt.querySelector('.card-sheen')) {
      const sheen = document.createElement('div');
      sheen.className = 'card-sheen';
      portraitTilt.appendChild(sheen);
    }
    portraitTilt.addEventListener('mousemove', (e) => {
      const rect = portraitTilt.getBoundingClientRect();
      const cx   = rect.left + rect.width  / 2;
      const cy   = rect.top  + rect.height / 2;
      const dx   = (e.clientX - cx) / (rect.width  / 2);
      const dy   = (e.clientY - cy) / (rect.height / 2);
      portraitTilt.style.transform = `perspective(800px) rotateX(${-dy * 7}deg) rotateY(${dx * 7}deg) scale(1.02)`;
      portraitTilt.style.transition = 'transform 0.08s ease-out';

      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const px = (x / rect.width) * 100;
      const py = (y / rect.height) * 100;
      portraitTilt.style.setProperty('--sheen-x', `${px}%`);
      portraitTilt.style.setProperty('--sheen-y', `${py}%`);
    });
    portraitTilt.addEventListener('mouseleave', () => {
      portraitTilt.style.transform = '';
      portraitTilt.style.transition = 'transform 0.6s cubic-bezier(0.25,0.8,0.25,1)';
    });
  }

  /* ──────────────────────────────────
     7. Project Filter
  ────────────────────────────────── */
  const filterBtns  = document.querySelectorAll('.filter-btn');
  const projCards   = document.querySelectorAll('.pcard[data-cat]');

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;

      projCards.forEach(card => {
        const categories = card.dataset.cat ? card.dataset.cat.split(' ') : [];
        const match = filter === 'all' || categories.includes(filter);
        card.style.transition = 'opacity 0.4s var(--ease), transform 0.4s var(--ease)';
        if (match) {
          card.style.opacity  = '1';
          card.style.transform = '';
          card.style.pointerEvents = '';
          card.style.display = '';
        } else {
          card.style.opacity  = '0.12';
          card.style.transform = 'scale(0.96) translateZ(0)';
          card.style.pointerEvents = 'none';
          setTimeout(() => {
            if(!card.style.pointerEvents) return;
            card.style.display = 'none'; // fully hide to maintain grid flow
          }, 400); // match transition duration
        }
      });
    });
  });

  /* ──────────────────────────────────
     8. Contact Form
  ────────────────────────────────── */
  const form       = document.getElementById('contact-form');
  const submitBtn  = document.getElementById('contact-submit-btn');

  if (form) {
    form.addEventListener('submit', (e) => {
      const name    = form.querySelector('#form-name').value.trim();
      const email   = form.querySelector('#form-email').value.trim();
      const message = form.querySelector('#form-message').value.trim();

      // Simple validation
      if (!name || !email || !message) {
        e.preventDefault();
        showToast('Please fill in all fields.', 'error');
        return;
      }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
        e.preventDefault();
        showToast('Please enter a valid email.', 'error');
        return;
      }

      // Fallback: If previewed locally via file:// protocol, let standard form POST run
      // to prevent CORS block on AJAX request.
      if (window.location.protocol === 'file:') {
        submitBtn.textContent = 'Sending…';
        submitBtn.disabled    = true;
        // Do not prevent default, allow form action to execute
        return;
      }

      e.preventDefault();
      submitBtn.textContent = 'Sending…';
      submitBtn.disabled    = true;

      // Submit to FormSubmit API
      fetch("https://formsubmit.co/ajax/jaysaner2006@gmail.com", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify({
          name: name,
          email: email,
          message: message,
          _subject: "New Message from Portfolio Visitor"
        })
      })
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("FormSubmit submission failed.");
        }
      })
      .then(data => {
        submitBtn.textContent = '✓ Message Sent!';
        showToast('Message sent! Jay will get back to you soon.', 'success');
        form.reset();
        setTimeout(() => {
          submitBtn.textContent = 'Send Message →';
          submitBtn.disabled    = false;
        }, 3000);
      })
      .catch(error => {
        console.error("Error submitting contact form:", error);
        submitBtn.textContent = 'Failed to Send';
        showToast('Could not send message. Please email directly.', 'error');
        setTimeout(() => {
          submitBtn.textContent = 'Send Message →';
          submitBtn.disabled    = false;
        }, 3000);
      });
    });
  }

  /* ──────────────────────────────────
     9. Toast notification
  ────────────────────────────────── */
  function showToast(message, type = 'success') {
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    toast.style.cssText = `
      position: fixed;
      bottom: 2rem; right: 2rem;
      background: ${type === 'success' ? '#6d5df6' : '#ef4444'};
      color: #fff;
      padding: 1rem 1.5rem;
      border-radius: 8px;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 0.9rem;
      font-weight: 500;
      box-shadow: 0 8px 32px rgba(0,0,0,0.4);
      z-index: 9999;
      opacity: 0;
      transform: translateY(12px);
      transition: opacity 0.3s ease, transform 0.3s ease;
    `;
    document.body.appendChild(toast);
    requestAnimationFrame(() => {
      toast.style.opacity   = '1';
      toast.style.transform = 'translateY(0)';
    });
    setTimeout(() => {
      toast.style.opacity   = '0';
      toast.style.transform = 'translateY(12px)';
      setTimeout(() => toast.remove(), 300);
    }, 4000);
  }

  /* ──────────────────────────────────
     10. Back to Top
  ────────────────────────────────── */
  const backBtn = document.getElementById('back-to-top-btn');
  if (backBtn) {
    backBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ──────────────────────────────────
     11. Hero stagger reveal on load
  ────────────────────────────────── */
  const heroText = document.querySelector('.hero-text');
  if (heroText) {
    const children = heroText.children;
    Array.from(children).forEach((el, i) => {
      el.style.opacity    = '0';
      el.style.transform  = 'translateY(24px)';
      el.style.transition = `opacity 0.7s cubic-bezier(0.25,0.8,0.25,1) ${i * 110}ms, transform 0.7s cubic-bezier(0.25,0.8,0.25,1) ${i * 110}ms`;
      setTimeout(() => {
        el.style.opacity   = '1';
        el.style.transform = 'translateY(0)';
      }, 200);
    });
  }

})();
