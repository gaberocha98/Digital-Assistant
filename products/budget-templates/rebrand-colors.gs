/**
 * Digital Assistant — Budget Tracker Color Rebrand Script
 *
 * HOW TO USE:
 * 1. Open your copy of the spreadsheet
 * 2. Go to Extensions > Apps Script
 * 3. Paste this entire script
 * 4. Click Run > rebrandAll
 * 5. Authorize when prompted
 * 6. Wait ~30 seconds for all sheets to update
 */

// Brand colors
const BRAND = {
  PRIMARY:       '#0D9488', // Teal
  PRIMARY_DARK:  '#115E59', // Deep Teal
  PRIMARY_LIGHT: '#CCFBF1', // Mint
  ACCENT:        '#F59E0B', // Amber Gold
  ACCENT_LIGHT:  '#FEF3C7', // Soft Gold
  DARK:          '#1E293B', // Charcoal
  MEDIUM:        '#64748B', // Slate
  LIGHT:         '#F1F5F9', // Cloud
  WHITE:         '#FFFFFF',
  INCOME:        '#10B981', // Green
  EXPENSE:       '#F43F5E', // Coral
  SAVINGS:       '#3B82F6', // Blue
  DEBT:          '#F97316', // Orange
  BILLS:         '#8B5CF6', // Purple
};

// Original pink colors to replace
const PINK_COLORS = [
  '#e4a5c0', '#e8b4cb', '#f2d5e3', '#f7e7ef', '#d4849f',
  '#e091b0', '#f5c6d8', '#fce4ee', '#ffb6c1', '#ff69b4',
  '#e75480', '#c71585', '#db7093', '#ff1493', '#d63384',
  '#e685b5', '#ffe4ec', '#f8d7e5', '#f0a8c8', '#e78bb8',
];

// Original blue colors to replace
const BLUE_COLORS = [
  '#a4c2f4', '#6d9eeb', '#4a86e8', '#3d78d8', '#1155cc',
  '#1c4587', '#b4d7ff', '#9fc5e8', '#6fa8dc', '#3c78d8',
  '#4285f4', '#2962ff', '#1a73e8', '#5b9bd5', '#4472c4',
  '#d6e4f0', '#dae8fc', '#c6dafc', '#a8c6f0', '#cfe2f3',
];

function rebrandAll() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheets = ss.getSheets();

  sheets.forEach(sheet => {
    const name = sheet.getName().toLowerCase();
    Logger.log('Processing sheet: ' + sheet.getName());

    if (name.includes('pink') || name.includes('rosa')) {
      rebrandSheet(sheet, PINK_COLORS, 'warm');
    } else if (name.includes('blue') || name.includes('blå')) {
      rebrandSheet(sheet, BLUE_COLORS, 'cool');
    } else if (name.includes('example') || name.includes('budget')) {
      rebrandSheet(sheet, PINK_COLORS.concat(BLUE_COLORS), 'warm');
    } else if (name.includes('instruction')) {
      rebrandInstructions(sheet);
    }
  });

  SpreadsheetApp.flush();
  Logger.log('Rebrand complete!');
}

function rebrandSheet(sheet, oldColors, tone) {
  const range = sheet.getDataRange();
  const backgrounds = range.getBackgrounds();
  const fontColors = range.getFontColors();
  const newBackgrounds = backgrounds.map(row => row.map(color => mapColor(color, oldColors, tone)));
  const newFontColors = fontColors.map(row => row.map(color => mapFontColor(color)));

  range.setBackgrounds(newBackgrounds);
  range.setFontColors(newFontColors);

  rebrandConditionalFormatting(sheet);
}

function mapColor(color, oldColors, tone) {
  if (!color) return color;
  const c = color.toLowerCase();

  // Dark header backgrounds (deep/saturated colors)
  if (isColorClose(c, oldColors.slice(0, 5)) || isSaturatedDark(c)) {
    return BRAND.PRIMARY_DARK;
  }

  // Medium accent backgrounds
  if (isColorClose(c, oldColors.slice(5, 10)) || isSaturatedMedium(c)) {
    return BRAND.PRIMARY;
  }

  // Light tinted backgrounds
  if (isColorClose(c, oldColors.slice(10, 15)) || isLightTint(c)) {
    return BRAND.PRIMARY_LIGHT;
  }

  // Very light tinted backgrounds
  if (isColorClose(c, oldColors.slice(15, 20)) || isVeryLightTint(c)) {
    return BRAND.LIGHT;
  }

  // Gray backgrounds stay as neutral
  if (isGray(c)) {
    return BRAND.LIGHT;
  }

  return color;
}

function mapFontColor(color) {
  if (!color) return color;
  const c = color.toLowerCase();

  // Dark font colors stay dark
  if (c === '#000000' || c === '#333333' || c === '#434343') {
    return BRAND.DARK;
  }

  // White font stays white
  if (c === '#ffffff' || c === '#fff') {
    return BRAND.WHITE;
  }

  // Colored fonts become brand primary
  if (isSaturated(c)) {
    return BRAND.PRIMARY;
  }

  return color;
}

function rebrandConditionalFormatting(sheet) {
  const rules = sheet.getConditionalFormatRules();
  // Clear and rebuild if needed
  // Conditional formatting colors will need manual update
}

function rebrandInstructions(sheet) {
  const range = sheet.getDataRange();
  const backgrounds = range.getBackgrounds();
  const allOldColors = PINK_COLORS.concat(BLUE_COLORS);
  const newBackgrounds = backgrounds.map(row => row.map(color => {
    const c = (color || '').toLowerCase();
    if (isColorClose(c, allOldColors) || isSaturated(c)) {
      if (isSaturatedDark(c)) return BRAND.PRIMARY_DARK;
      if (isSaturatedMedium(c)) return BRAND.PRIMARY;
      return BRAND.PRIMARY_LIGHT;
    }
    return color;
  }));
  range.setBackgrounds(newBackgrounds);
}

// Color utility functions
function hexToRgb(hex) {
  hex = hex.replace('#', '');
  if (hex.length === 3) hex = hex[0]+hex[0]+hex[1]+hex[1]+hex[2]+hex[2];
  return {
    r: parseInt(hex.substring(0, 2), 16),
    g: parseInt(hex.substring(2, 4), 16),
    b: parseInt(hex.substring(4, 6), 16)
  };
}

function isColorClose(color, targets) {
  try {
    const rgb = hexToRgb(color);
    return targets.some(t => {
      const target = hexToRgb(t);
      const dist = Math.sqrt(
        Math.pow(rgb.r - target.r, 2) +
        Math.pow(rgb.g - target.g, 2) +
        Math.pow(rgb.b - target.b, 2)
      );
      return dist < 60;
    });
  } catch(e) { return false; }
}

function isSaturated(color) {
  try {
    const rgb = hexToRgb(color);
    const max = Math.max(rgb.r, rgb.g, rgb.b);
    const min = Math.min(rgb.r, rgb.g, rgb.b);
    if (max === 0) return false;
    return (max - min) / max > 0.3;
  } catch(e) { return false; }
}

function isSaturatedDark(color) {
  try {
    const rgb = hexToRgb(color);
    const lum = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114);
    return isSaturated(color) && lum < 120;
  } catch(e) { return false; }
}

function isSaturatedMedium(color) {
  try {
    const rgb = hexToRgb(color);
    const lum = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114);
    return isSaturated(color) && lum >= 120 && lum < 180;
  } catch(e) { return false; }
}

function isLightTint(color) {
  try {
    const rgb = hexToRgb(color);
    const lum = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114);
    return isSaturated(color) && lum >= 180 && lum < 230;
  } catch(e) { return false; }
}

function isVeryLightTint(color) {
  try {
    const rgb = hexToRgb(color);
    const lum = (rgb.r * 0.299 + rgb.g * 0.587 + rgb.b * 0.114);
    return isSaturated(color) && lum >= 230;
  } catch(e) { return false; }
}

function isGray(color) {
  try {
    const rgb = hexToRgb(color);
    const max = Math.max(rgb.r, rgb.g, rgb.b);
    const min = Math.min(rgb.r, rgb.g, rgb.b);
    return (max - min) < 20 && max > 30 && max < 240;
  } catch(e) { return false; }
}
