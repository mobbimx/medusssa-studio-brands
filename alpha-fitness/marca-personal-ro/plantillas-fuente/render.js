const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [,, htmlPath, outPath, w, h, transparent] = process.argv;
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({
    viewport: { width: parseInt(w), height: parseInt(h) },
    deviceScaleFactor: 2,
  });
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  await page.waitForTimeout(300);
  await page.screenshot({ path: outPath, omitBackground: transparent === 'true' });
  await browser.close();
  console.log('rendered', outPath);
})();
