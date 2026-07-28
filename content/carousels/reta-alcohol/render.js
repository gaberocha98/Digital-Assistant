const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const slides = require('./slides');
const { renderSlide } = require('./template');

const OUT = path.join(__dirname, 'out');
fs.mkdirSync(OUT, { recursive: true });

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  for (let i = 0; i < slides.length; i++) {
    const html = renderSlide(slides[i], i);
    await page.setContent(html, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    const file = path.join(OUT, `EON-Reta-${String(i + 1).padStart(2, '0')}.png`);
    await page.screenshot({ path: file, clip: { x: 0, y: 0, width: 1080, height: 1350 } });
    console.log('rendered', file);
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
