#!/usr/bin/env node
// Lab resources vault: encrypts _private/lab-resources.html so only listed lab members can read /lab/.
//
//   node scripts/lab-vault.mjs                 re-encrypt after editing the resources page
//   node scripts/lab-vault.mjs add <username> ["Full Name"]   add a member, prints their passphrase
//   node scripts/lab-vault.mjs reset <username>               issue a new passphrase
//   node scripts/lab-vault.mjs remove <username>              revoke access (re-encrypts with a new key)
//   node scripts/lab-vault.mjs list                           show members
//
// Every run re-encrypts with a fresh content key, so removed members and old
// "remember this device" sessions stop working once you commit and push.
// _private/ is git-ignored: the readable page and passphrases never leave this computer.

import { webcrypto as crypto } from 'node:crypto';
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SRC = join(ROOT, '_private', 'lab-resources.html');
const MEMBERS = join(ROOT, '_private', 'lab-members.json');
const OUT = join(ROOT, '_data', 'lab_vault.json');
const ITER = 600000;
const subtle = crypto.subtle;
const enc = new TextEncoder();

const b64 = (u8) => Buffer.from(u8).toString('base64');
const rand = (n) => crypto.getRandomValues(new Uint8Array(n));
const hex = (buf) => Buffer.from(buf).toString('hex');
const norm = (u) => String(u || '').trim().toLowerCase();

function newPassphrase() {
  const alphabet = 'abcdefghjkmnpqrstuvwxyz23456789'; // no look-alikes
  const bytes = rand(16);
  let s = '';
  for (let i = 0; i < 16; i++) s += alphabet[bytes[i] % alphabet.length] + ((i % 4 === 3 && i < 15) ? '-' : '');
  return s;
}

function loadMembers() {
  if (!existsSync(MEMBERS)) return { members: [] };
  return JSON.parse(readFileSync(MEMBERS, 'utf8'));
}
function saveMembers(db) {
  mkdirSync(dirname(MEMBERS), { recursive: true });
  writeFileSync(MEMBERS, JSON.stringify(db, null, 2) + '\n');
}

async function slotId(salt, username) {
  const h = await subtle.digest('SHA-256', enc.encode(salt + ':' + norm(username)));
  return hex(h).slice(0, 24);
}

async function build(db) {
  if (!existsSync(SRC)) { console.error('Missing ' + SRC); process.exit(1); }
  if (!db.members.length) { console.error('No members yet. Add one with: node scripts/lab-vault.mjs add <username>'); process.exit(1); }
  const html = readFileSync(SRC, 'utf8');
  const rawKey = rand(32);
  const key = await subtle.importKey('raw', rawKey, 'AES-GCM', false, ['encrypt']);
  const iv = rand(12);
  const ct = new Uint8Array(await subtle.encrypt({ name: 'AES-GCM', iv }, key, enc.encode(html)));
  const salt = b64(rand(16));
  const slots = {};
  for (const m of db.members) {
    const s = rand(16), wiv = rand(12);
    const base = await subtle.importKey('raw', enc.encode(m.passphrase), 'PBKDF2', false, ['deriveKey']);
    const kek = await subtle.deriveKey({ name: 'PBKDF2', salt: s, iterations: ITER, hash: 'SHA-256' }, base, { name: 'AES-GCM', length: 256 }, false, ['encrypt']);
    const wk = new Uint8Array(await subtle.encrypt({ name: 'AES-GCM', iv: wiv }, kek, rawKey));
    slots[await slotId(salt, m.username)] = { s: b64(s), iv: b64(wiv), wk: b64(wk) };
  }
  const vault = { v: 1, kid: hex(rand(8)), salt, iter: ITER, iv: b64(iv), ct: b64(ct), updated: new Date().toISOString().slice(0, 10), slots };
  writeFileSync(OUT, JSON.stringify(vault) + '\n');
  console.log(`Encrypted for ${db.members.length} member(s) -> _data/lab_vault.json. Commit and push to publish.`);
}

const [cmd, arg, ...rest] = process.argv.slice(2);
const db = loadMembers();
const find = (u) => db.members.find((m) => m.username === norm(u));

if (!cmd || cmd === 'build') {
  await build(db);
} else if (cmd === 'list') {
  if (!db.members.length) console.log('No members.');
  for (const m of db.members) console.log(`${m.username.padEnd(16)} ${m.name || ''}  (added ${m.added})`);
} else if (cmd === 'add' || cmd === 'reset') {
  if (!arg) { console.error(`Usage: node scripts/lab-vault.mjs ${cmd} <username>`); process.exit(1); }
  let m = find(arg);
  if (cmd === 'add' && m) { console.error(`${m.username} already exists. Use "reset" for a new passphrase.`); process.exit(1); }
  if (cmd === 'reset' && !m) { console.error(`No member named ${norm(arg)}.`); process.exit(1); }
  if (!m) { m = { username: norm(arg), name: rest.join(' '), added: new Date().toISOString().slice(0, 10) }; db.members.push(m); }
  m.passphrase = newPassphrase();
  saveMembers(db);
  await build(db);
  console.log(`\nSend this to ${m.name || m.username} privately:\n  Username:   ${m.username}\n  Passphrase: ${m.passphrase}\n`);
} else if (cmd === 'remove') {
  const before = db.members.length;
  db.members = db.members.filter((m) => m.username !== norm(arg));
  if (db.members.length === before) { console.error(`No member named ${norm(arg)}.`); process.exit(1); }
  saveMembers(db);
  await build(db);
  console.log(`Removed ${norm(arg)}.`);
} else {
  console.error('Commands: build | add <username> ["Full Name"] | reset <username> | remove <username> | list');
  process.exit(1);
}
