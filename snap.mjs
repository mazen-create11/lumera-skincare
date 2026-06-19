import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 1080 });
  await page.goto('http://localhost:8848/product-mask.html', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'screenshot_desktop.png', fullPage: true });
  await page.setViewport({ width: 375, height: 812 });
  await page.goto('http://localhost:8848/product-mask.html', { waitUntil: 'networkidle0' });
  await page.screenshot({ path: 'screenshot_mobile.png', fullPage: true });
  await browser.close();
})();
