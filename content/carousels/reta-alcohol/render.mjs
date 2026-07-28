import { chromium } from 'playwright';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const html = 'file://' + path.join(__dirname, 'slides.html');
const outDir = path.join(__dirname, 'slides');

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 2 });
await page.goto(html, { waitUntil: 'networkidle' });

for (let i = 1; i <= 8; i++) {
  const el = await page.$(`#s${i}`);
  const file = path.join(outDir, `slide-${String(i).padStart(2, '0')}.png`);
  await el.screenshot({ path: file });
  console.log('wrote', file);
}
await browser.close();
