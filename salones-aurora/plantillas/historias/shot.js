// Renderiza las plantillas HTML a PNG 1080x1350.
// Uso:  NODE_PATH=/opt/node22/lib/node_modules node shot.js
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const dir = __dirname;
  const names = fs.readFileSync(path.join(dir,'html','_manifest.txt'),'utf8').trim().split('\n');
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args:['--no-sandbox'] });
  const page = await browser.newPage({ viewport:{ width:1080, height:1920 }, deviceScaleFactor:1 });
  for (const n of names) {
    await page.goto('file://' + path.join(dir,'html', n + '.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(dir, n + '.png') });
    console.log('✓', n + '.png');
  }
  await browser.close();
})();
