document.addEventListener('DOMContentLoaded', () => {
  const sidebar = document.getElementById('sidebar');
  const searchInput = document.getElementById('sidebar-search');
  const mobileToggle = document.getElementById('mobile-menu-toggle');
  const backdrop = document.getElementById('sidebar-backdrop');
  const categoryHeaders = document.querySelectorAll('.nav-category-header');

  const STORAGE_KEY_PREFIX = 'util_category_expanded_';

  categoryHeaders.forEach((header) => {
    const categoryEl = header.closest('.nav-category');
    const categoryName = categoryEl.getAttribute('data-category');
    const toggleBtn = header.querySelector('.category-toggle-btn');

    if (categoryName) {
      const savedState = localStorage.getItem(STORAGE_KEY_PREFIX + categoryName);
      if (savedState !== null) {
        if (savedState === 'true') {
          categoryEl.classList.add('expanded');
        }
        else {
          if (!categoryEl.classList.contains('active-category')) {
            categoryEl.classList.remove('expanded');
          }
        }
      }
    }

    if (toggleBtn) {
      toggleBtn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        categoryEl.classList.toggle('expanded');
        if (categoryName) {
          localStorage.setItem(
            STORAGE_KEY_PREFIX + categoryName,
            categoryEl.classList.contains('expanded').toString()
          );
        }
      });
    }
  });

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = (e.target.value || '').trim().toLowerCase();
      const categories = document.querySelectorAll('.nav-category');

      if (query.length === 0) {
        categories.forEach((cat) => {
          cat.style.display = '';
          const categoryName = cat.getAttribute('data-category');
          const savedState = localStorage.getItem(STORAGE_KEY_PREFIX + categoryName);
          if (savedState === 'false' && !cat.classList.contains('active-category')) {
            cat.classList.remove('expanded');
          }
          else {
            cat.classList.add('expanded');
          }
          const items = cat.querySelectorAll('.nav-item');
          items.forEach((item) => {
            item.style.display = '';
          });
        });
        return;
      }

      categories.forEach((cat) => {
        const catTitle = (cat.getAttribute('data-category') || '').toLowerCase();
        const items = cat.querySelectorAll('.nav-item');
        let hasMatch = false;

        if (catTitle.includes(query)) {
          hasMatch = true;
          items.forEach((item) => {
            item.style.display = '';
          });
        }
        else {
          items.forEach((item) => {
            const text = (item.textContent || '').trim().toLowerCase();
            if (text.includes(query)) {
              item.style.display = '';
              hasMatch = true;
            }
            else {
              item.style.display = 'none';
            }
          });
        }

        if (hasMatch) {
          cat.style.display = '';
          cat.classList.add('expanded');
        }
        else {
          cat.style.display = 'none';
        }
      });
    });
  }

  function openMobileMenu() {
    if (sidebar) {
      sidebar.classList.add('open');
    }
    if (backdrop) {
      backdrop.classList.add('active');
    }
  }

  function closeMobileMenu() {
    if (sidebar) {
      sidebar.classList.remove('open');
    }
    if (backdrop) {
      backdrop.classList.remove('active');
    }
  }

  if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
      if (sidebar && sidebar.classList.contains('open')) {
        closeMobileMenu();
      }
      else {
        openMobileMenu();
      }
    });
  }

  if (backdrop) {
    backdrop.addEventListener('click', () => {
      closeMobileMenu();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeMobileMenu();
      if (searchInput && document.activeElement === searchInput) {
        searchInput.value = '';
        searchInput.dispatchEvent(new Event('input'));
        searchInput.blur();
      }
    }

    if (e.key === '/' && document.activeElement !== searchInput && searchInput) {
      const tagName = (document.activeElement && document.activeElement.tagName) || '';
      if (tagName !== 'INPUT' && tagName !== 'TEXTAREA') {
        e.preventDefault();
        searchInput.focus();
        searchInput.select();
      }
    }
  });

  const preBlocks = document.querySelectorAll('.content pre');
  preBlocks.forEach((pre) => {
    const wrapper = document.createElement('div');
    wrapper.className = 'code-block-wrapper';
    pre.parentNode.insertBefore(wrapper, pre);
    wrapper.appendChild(pre);

    const copyBtn = document.createElement('button');
    copyBtn.className = 'copy-code-btn';
    copyBtn.type = 'button';
    copyBtn.innerText = 'Copy';
    wrapper.appendChild(copyBtn);

    copyBtn.addEventListener('click', async () => {
      const codeText = pre.querySelector('code')
        ? pre.querySelector('code').innerText
        : pre.innerText;

      try {
        await navigator.clipboard.writeText(codeText);
        copyBtn.innerText = 'Copied!';
        setTimeout(() => {
          copyBtn.innerText = 'Copy';
        }, 2000);
      }
      catch (err) {
        copyBtn.innerText = 'Failed';
        setTimeout(() => {
          copyBtn.innerText = 'Copy';
        }, 2000);
      }
    });
  });
});
