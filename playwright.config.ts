import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './playwright_tests',
  use: {
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  reporter: [
  ['list'],
  ['json', { outputFile: './qa-dashboard/public/results.json' }],
  ['html', { outputFolder: 'playwright-report', open: 'never' }]
],
});
