(function () {
  var STORE = 'yinlab.vault';
  var gate = document.getElementById('lab-gate');
  var form = document.getElementById('lab-form');
  var err = document.getElementById('lab-error');
  var btn = document.getElementById('lab-submit');
  var view = document.getElementById('lab-view');
  var out = document.getElementById('lab-content');
  var lockBtn = document.getElementById('lab-lock');
  var updated = document.getElementById('lab-updated');
  var vault = null;
  try { vault = JSON.parse(document.getElementById('lab-vault').textContent); } catch (e) {}

  if (!vault || !vault.slots) {
    form.hidden = true;
    err.textContent = 'Lab resources have not been published yet.';
    return;
  }
  if (!window.crypto || !window.crypto.subtle) {
    form.hidden = true;
    err.textContent = 'This page needs a current browser and a secure (https) connection.';
    return;
  }
  var subtle = window.crypto.subtle;
  var enc = new TextEncoder();
  function b64d(s) { var b = atob(s), u = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; }
  function b64e(u) { var s = ''; for (var i = 0; i < u.length; i++) s += String.fromCharCode(u[i]); return btoa(s); }
  function hex(buf) { return Array.prototype.map.call(new Uint8Array(buf), function (x) { return ('0' + x.toString(16)).slice(-2); }).join(''); }
  function store(get, val) {
    try {
      if (get) return JSON.parse(localStorage.getItem(STORE) || 'null');
      if (val) localStorage.setItem(STORE, JSON.stringify(val)); else localStorage.removeItem(STORE);
    } catch (e) { return null; }
  }

  async function unwrap(user, pass) {
    var h = await subtle.digest('SHA-256', enc.encode(vault.salt + ':' + user.trim().toLowerCase()));
    var slot = vault.slots[hex(h).slice(0, 24)];
    if (!slot) return null;
    var base = await subtle.importKey('raw', enc.encode(pass), 'PBKDF2', false, ['deriveKey']);
    var kek = await subtle.deriveKey({ name: 'PBKDF2', salt: b64d(slot.s), iterations: vault.iter, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    try { return new Uint8Array(await subtle.decrypt({ name: 'AES-GCM', iv: b64d(slot.iv) }, kek, b64d(slot.wk))); }
    catch (e) { return null; }
  }
  async function open(raw) {
    var key = await subtle.importKey('raw', raw, 'AES-GCM', false, ['decrypt']);
    var pt = await subtle.decrypt({ name: 'AES-GCM', iv: b64d(vault.iv) }, key, b64d(vault.ct));
    out.innerHTML = new TextDecoder().decode(pt);
    if (updated && vault.updated) updated.textContent = 'Updated ' + vault.updated;
    gate.hidden = true;
    view.hidden = false;
  }

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    err.textContent = '';
    btn.disabled = true;
    btn.textContent = 'Unlocking…';
    try {
      var raw = await unwrap(form.username.value, form.passphrase.value);
      if (!raw) {
        err.textContent = "That username and passphrase don't match. Check both, or ask Zhuoli for a new passphrase.";
        return;
      }
      if (form.remember.checked) store(false, { kid: vault.kid, k: b64e(raw) });
      form.passphrase.value = '';
      await open(raw);
    } catch (e2) {
      err.textContent = 'Something went wrong while unlocking. Reload the page and try again.';
    } finally {
      btn.disabled = false;
      btn.textContent = 'Unlock';
    }
  });

  lockBtn.addEventListener('click', function () {
    store(false, null);
    out.innerHTML = '';
    view.hidden = true;
    gate.hidden = false;
  });

  var saved = store(true);
  if (saved && saved.kid === vault.kid) {
    open(b64d(saved.k)).catch(function () { store(false, null); });
  } else if (saved) {
    store(false, null);
  }
})();
