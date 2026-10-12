# zhuoliyin.github.io

Personal academic homepage of Zhuoli Yin, served by GitHub Pages (Jekyll).

## Where to edit

| What | File |
| --- | --- |
| News | `_data/news.yml` (newest first; Markdown allowed) |
| Publications | `_data/publications.yml` (`selected: true` shows it on the homepage) |
| Homepage bio, awards, service | `_pages/home.html` |
| Research / Teaching | `_pages/Research.md`, `_pages/Teaching.md` |
| Join the lab | `_pages/prospective-students.html` |
| Life page | `_data/life.yml` (photos go in `images/life/`) |
| Navigation | `_data/navigation.yml` |
| Styles | `assets/css/site.css` (plain CSS) |

## Lab resources (members only)

`/lab/` is encrypted in the browser (AES-256-GCM, a per-member PBKDF2 key). The readable source
and the member list live in `_private/`, which is git-ignored and never pushed.

```bash
node scripts/lab-vault.mjs add <username> "Full Name"   # prints a passphrase to send privately
node scripts/lab-vault.mjs remove <username>            # revoke
node scripts/lab-vault.mjs reset <username>             # new passphrase
node scripts/lab-vault.mjs                              # re-encrypt after editing _private/lab-resources.html
node scripts/lab-vault.mjs list
```

Commit `_data/lab_vault.json` and push after each change. Requires Node.js 18+.
