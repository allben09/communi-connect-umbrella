// Communi-Connect Umbrella – Animations

document.addEventListener('DOMContentLoaded', () => {
  // Scroll Reveal
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.1 });
  reveals.forEach(el => observer.observe(el));

  // Animated Counters
  const counters = document.querySelectorAll('.stat-number');
  counters.forEach(counter => {
    const target = +counter.dataset.target;
    if (!target) return;
    const duration = 1800;
    const step = target / (duration / 16);
    let current = 0;
    const update = () => {
      current += step;
      if (current < target) {
        counter.textContent = Math.ceil(current);
        requestAnimationFrame(update);
      } else {
        counter.textContent = target;
      }
    };
    const countObserver = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        update();
        countObserver.disconnect();
      }
    });
    countObserver.observe(counter);
  });
});
