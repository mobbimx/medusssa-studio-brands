// Render index.html -> deck.pdf (12 páginas, horizontal, una slide por página).
// Requiere Node + Playwright (chromium). Uso:  node scripts/render.mjs
import { createRequire } from 'node:module';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const require = createRequire(import.meta.url);
// Resuelve Playwright esté donde esté instalado (local o global).
function loadChromium() {
  const candidates = ['playwright', 'playwright-core', '/opt/node22/lib/node_modules/playwright'];
  for (const c of candidates) {
    try { return require(c).chromium; } catch {}
  }
  throw new Error('No se encontró Playwright. Instala con: npm i -D playwright');
}

const here = path.dirname(fileURLToPath(import.meta.url));
const dir = path.resolve(here, '..');
const htmlPath = path.join(dir, 'index.html');
const out = path.join(dir, 'deck.pdf');

const chromium = loadChromium();
const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
try { await page.evaluate(() => document.fonts && document.fonts.ready); } catch {}
await page.waitForTimeout(600);
await page.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log('PDF ->', out);
