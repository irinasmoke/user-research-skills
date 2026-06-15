# Excel Charts Skill

## Overview

Create professional Excel charts (.xlsx) with proper formatting. Use this skill when creating bar charts, comparison charts, or any data visualization in Excel.

## Critical Rules

### ALWAYS use xlsxwriter, NEVER openpyxl for charts

openpyxl has broken/unreliable chart support:
- `numFmt` on `DataLabelList` silently fails — data labels never show "%"
- `y_axis.scaling.orientation = "maxMin"` reverses the value axis too (bars go right-to-left)
- Category axis labels appear on the wrong side
- `tickLblPos` settings don't persist through save
- Chart XML post-processing often corrupts the file ("We found a problem with some content")

**xlsxwriter** handles all of this correctly out of the box.

### Installation

```bash
pip3 install xlsxwriter --break-system-packages --quiet
```

### Standard Chart Pattern

```python
import xlsxwriter

wb = xlsxwriter.Workbook('output.xlsx')

# Write data sheet (smallest first so largest appears at TOP in bar chart)
ws = wb.add_worksheet('Data')
ws.write(0, 0, 'Category')
ws.write(0, 1, 'Series 1 (%)')
ws.write(0, 2, 'Series 2 (%)')

categories_reversed = list(reversed(categories_sorted_desc))
for i, cat in enumerate(categories_reversed):
    ws.write(i + 1, 0, cat)
    ws.write(i + 1, 1, series1_data.get(cat, 0))
    ws.write(i + 1, 2, series2_data.get(cat, 0))

n = len(categories_reversed)

chart = wb.add_chart({'type': 'bar'})

chart.add_series({
    'name': 'Series 1',
    'categories': ['Data', 1, 0, n, 0],
    'values': ['Data', 1, 1, n, 1],
    'fill': {'color': '#0078D4'},       # Azure blue
    'border': {'color': '#0078D4'},
    'data_labels': {'value': True, 'num_format': '0.0"%"', 'font': {'size': 9}},
})

chart.add_series({
    'name': 'Series 2',
    'categories': ['Data', 1, 0, n, 0],
    'values': ['Data', 1, 2, n, 2],
    'fill': {'color': '#C8C8C8'},       # Neutral gray
    'border': {'color': '#C8C8C8'},
    'data_labels': {'value': True, 'num_format': '0.0"%"', 'font': {'size': 9}},
})

chart.set_title({'name': 'Chart Title'})
chart.set_x_axis({
    'name': 'Percentage of Respondents (%)',
    'num_format': '0"%"',
})
chart.set_y_axis({'reverse': False})
chart.set_legend({'position': 'bottom'})
chart.set_size({'width': 800, 'height': 500})

ws_charts = wb.add_worksheet('Charts')
ws_charts.insert_chart('A1', chart)
wb.close()
```

## Key Patterns

### Largest category at top of horizontal bar chart
- Sort your data **descending** by value
- Then **reverse** it when writing to the sheet
- xlsxwriter renders bottom-row-first for bar charts, so reversed = largest at top
- Do NOT use `set_y_axis({'reverse': True})` — that flips labels but not intuition

### Data labels with percentage
- Use `'num_format': '0.0"%"'` in the `data_labels` dict per series
- This reliably shows "14.8%" instead of "14.8"

### Category labels on the left
- This is the default for horizontal bar charts in xlsxwriter — no special config needed
- Do NOT set axis orientation or tickLblPos manually

### Axis title on the bottom (x-axis)
- Use `chart.set_x_axis({'name': 'Your Label'})` 
- For bar charts, x_axis = the value/horizontal axis at the bottom

### Colors
- Foundry/Azure: `#0078D4`
- Neutral/comparison: `#C8C8C8` (light gray)
- Set both `fill` and `border` to the same color for clean bars

### Chart sizing
- Width 800 is good for most charts
- Height: 350 for 5-7 categories, 500 for 10-15, 600+ for 15+

## Common Mistakes to Avoid

1. **Don't use openpyxl for charts** — it works for data/sheets but charts are broken
2. **Don't include multi-label categories** — filter out entries with semicolons (e.g., "Cat1; Cat2") 
3. **Don't set orientation "maxMin"** — it breaks the value axis direction
4. **Don't do XML post-processing on chart XML** — it usually corrupts the file
5. **Don't forget to close Excel before writing** — `osascript -e 'tell application "Microsoft Excel" to close every workbook saving no'`
6. **openpyxl and xlsxwriter cannot coexist in one file** — pick one library per file creation

## Dependencies

- `xlsxwriter` (pip install)
- Python 3 standard library
