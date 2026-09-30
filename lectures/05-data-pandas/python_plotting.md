---
title: "Data Visualization in Python"
subtitle: "A practical guide to matplotlib and seaborn"
format:
  html:
    toc: true
    toc-depth: 3
    code-fold: false
jupyter: python3
---

# Introduction

> **Why do we visualize data?**

Data visualization transforms numbers into insights. A table with 10,000 rows and 8 columns is opaque—you can't see patterns, outliers, or relationships by reading numbers. But plot those same data points, and patterns emerge immediately: trends become visible, clusters appear, outliers stand out, and the shape of distributions reveals itself.

Effective visualization serves three purposes in scientific computing:

1. **Exploration**: During analysis, plots help you understand your data—what's the distribution? Are there outliers? What correlates with what?

2. **Diagnostics**: Plots reveal problems—missing data patterns, heteroscedasticity, non-normality, or computational errors that produce impossible values.

3. **Communication**: Publication-quality figures convey findings to others. A well-designed plot can communicate in seconds what would take paragraphs to explain.

This guide focuses on **matplotlib**, Python's foundational plotting library. Matplotlib is verbose but powerful—you have complete control over every aspect of your figures. We'll emphasize the **object-oriented interface** using `fig, ax = plt.subplots()`, which provides explicit control and scales well to complex multi-panel figures.

We'll also briefly introduce **seaborn**, which builds on matplotlib to provide statistical graphics with sensible defaults and less code. Think of seaborn as matplotlib with good taste.

By the end of this guide, you'll be able to create, customize, and save the core plot types needed for scientific data analysis.

# 1. The Object-Oriented Interface

## 1.1 Two Ways to Plot

Matplotlib has two interfaces:

**State-based (pyplot)**: Quick and convenient but implicit
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('My Plot')
```

**Object-oriented**: Explicit control, scales to complex figures
```python
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
ax.set_title('My Plot')
```

We'll focus on the object-oriented approach because it's clearer which plot you're modifying and works better with subplots.

## 1.2 Anatomy of a Figure

```{python}
import matplotlib.pyplot as plt
import numpy as np

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Plot data
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, linewidth=2)

# Customize
ax.set_xlabel('X axis', fontsize=12)
ax.set_ylabel('Y axis', fontsize=12)
ax.set_title('Anatomy of a Plot', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

Key components:
- **Figure** (`fig`): The whole canvas
- **Axes** (`ax`): The plotting area (confusingly named—these are the actual plots!)
- **Axis**: The x and y axes with ticks and labels

Common pattern:
```python
fig, ax = plt.subplots()  # Create figure and axes
ax.plot(...)              # Plot on axes
ax.set_xlabel(...)        # Configure axes
plt.show()                # Display
```

# 2. Line Plots

Line plots show relationships between continuous variables or trends over time.

## 2.1 Basic Line Plot

```{python}
# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create plot
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y1, label='sin(x)')
ax.plot(x, y2, label='cos(x)')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Trigonometric Functions')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 2.2 Line Styles and Markers

```{python}
fig, ax = plt.subplots(figsize=(10, 5))

# Different line styles
x = np.linspace(0, 10, 50)
ax.plot(x, x, '-', label='solid')
ax.plot(x, x + 1, '--', label='dashed')
ax.plot(x, x + 2, '-.', label='dash-dot')
ax.plot(x, x + 3, ':', label='dotted')

# With markers
ax.plot(x, x + 4, 'o-', label='circles', markevery=5)
ax.plot(x, x + 5, 's--', label='squares', markevery=5)
ax.plot(x, x + 6, '^:', label='triangles', markevery=5)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Line Styles and Markers')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

Common markers: `'o'` (circle), `'s'` (square), `'^'` (triangle up), `'v'` (triangle down), `'*'` (star), `'+'` (plus), `'x'` (x)

## 2.3 Colors and Widths

```{python}
fig, ax = plt.subplots(figsize=(10, 5))

x = np.linspace(0, 10, 100)

# Named colors
ax.plot(x, np.sin(x), color='red', linewidth=2, label='red')
ax.plot(x, np.sin(x) + 0.5, color='blue', linewidth=2, label='blue')

# Hex colors
ax.plot(x, np.sin(x) + 1, color='#FF5733', linewidth=2, label='custom hex')

# RGB tuples (0-1 scale)
ax.plot(x, np.sin(x) + 1.5, color=(0.2, 0.4, 0.6), linewidth=2, label='RGB')

# Varying widths
ax.plot(x, np.sin(x) + 2, linewidth=1, label='thin')
ax.plot(x, np.sin(x) + 2.5, linewidth=4, label='thick')

ax.legend()
ax.set_title('Colors and Line Widths')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

# 3. Scatter Plots

Scatter plots show relationships between two continuous variables.

## 3.1 Basic Scatter

```{python}
# Generate random data
np.random.seed(42)
n = 100
x = np.random.randn(n)
y = 2*x + np.random.randn(n)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(x, y, alpha=0.6)

ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
ax.set_title('Basic Scatter Plot')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 3.2 Colored and Sized by Variables

```{python}
# Data with additional dimensions
x = np.random.randn(100)
y = 2*x + np.random.randn(100)
colors = np.random.rand(100)  # Third variable
sizes = np.random.randint(20, 200, 100)  # Fourth variable

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(x, y, c=colors, s=sizes, alpha=0.5, 
                     cmap='viridis', edgecolors='black', linewidth=0.5)

ax.set_xlabel('X Variable')
ax.set_ylabel('Y Variable')
ax.set_title('Scatter with Color and Size Mapping')

# Add colorbar
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('Color Variable')

ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Parameters:
- `c`: color (single color or array for per-point colors)
- `s`: size (single value or array)
- `alpha`: transparency (0-1)
- `cmap`: colormap for color array
- `edgecolors`: edge color around markers

### Your Turn: Explore Relationships

Create a scatter plot showing the relationship between any two variables from a dataset. Try coloring points by a categorical variable or sizing them by a third continuous variable.

# 4. Bar Charts

Bar charts compare quantities across categories.

## 4.1 Vertical Bars

```{python}
# Data
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 32]

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(categories, values, color='steelblue', edgecolor='black', alpha=0.7)

ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Vertical Bar Chart')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

## 4.2 Horizontal Bars

```{python}
fig, ax = plt.subplots(figsize=(8, 6))
ax.barh(categories, values, color='coral', edgecolor='black', alpha=0.7)

ax.set_ylabel('Category')
ax.set_xlabel('Value')
ax.set_title('Horizontal Bar Chart')
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()
```

Horizontal bars are better when category names are long.

## 4.3 Grouped Bars

```{python}
# Data for multiple groups
categories = ['A', 'B', 'C', 'D']
values1 = [20, 35, 30, 35]
values2 = [25, 32, 34, 20]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, values1, width, label='Group 1', 
               color='steelblue', edgecolor='black')
bars2 = ax.bar(x + width/2, values2, width, label='Group 2', 
               color='coral', edgecolor='black')

ax.set_xlabel('Category')
ax.set_ylabel('Value')
ax.set_title('Grouped Bar Chart')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

## 4.4 Stacked Bars

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(categories, values1, label='Group 1', color='steelblue', edgecolor='black')
ax.bar(categories, values2, bottom=values1, label='Group 2', 
       color='coral', edgecolor='black')

ax.set_xlabel('Category')
ax.set_ylabel('Total Value')
ax.set_title('Stacked Bar Chart')
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

# 5. Histograms

Histograms show distributions of continuous variables.

## 5.1 Basic Histogram

```{python}
# Generate random data
data = np.random.randn(1000)

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins=30, edgecolor='black', alpha=0.7, color='steelblue')

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Histogram of Normal Distribution')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

## 5.2 Multiple Histograms

```{python}
# Two distributions
data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(data1, bins=30, alpha=0.5, label='Distribution 1', color='blue')
ax.hist(data2, bins=30, alpha=0.5, label='Distribution 2', color='red')

ax.set_xlabel('Value')
ax.set_ylabel('Frequency')
ax.set_title('Overlaid Histograms')
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

## 5.3 Density Histograms

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

# Density histogram (area sums to 1)
ax.hist(data, bins=30, density=True, alpha=0.7, 
        edgecolor='black', color='steelblue', label='Histogram')

# Add theoretical normal curve
x = np.linspace(data.min(), data.max(), 100)
from scipy import stats
ax.plot(x, stats.norm.pdf(x, data.mean(), data.std()), 
        'r-', linewidth=2, label='Normal PDF')

ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_title('Density Histogram with Normal Curve')
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

# 6. Box Plots

Box plots show distribution summaries: median, quartiles, and outliers.

## 6.1 Basic Box Plot

```{python}
# Generate data for multiple groups
data = [np.random.randn(100) + i for i in range(5)]

fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, tick_labels=['A', 'B', 'C', 'D', 'E'], patch_artist=True)

# Color boxes
for patch in bp['boxes']:
    patch.set_facecolor('lightblue')

ax.set_xlabel('Group')
ax.set_ylabel('Value')
ax.set_title('Box Plot Comparison')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

Box plot anatomy:
- **Box**: 25th to 75th percentile (IQR)
- **Line in box**: Median (50th percentile)
- **Whiskers**: Extend to 1.5 × IQR
- **Points beyond whiskers**: Outliers

## 6.2 Horizontal Box Plot

```{python}
fig, ax = plt.subplots(figsize=(10, 6))
bp = ax.boxplot(data, tick_labels=['A', 'B', 'C', 'D', 'E'], 
                patch_artist=True, vert=False)

for patch in bp['boxes']:
    patch.set_facecolor('coral')

ax.set_ylabel('Group')
ax.set_xlabel('Value')
ax.set_title('Horizontal Box Plot')
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.show()
```

# 7. Time Series Plots

Time series show how variables change over time.

## 7.1 Basic Time Series

```{python}
import pandas as pd

# Create time series data
dates = pd.date_range('2024-01-01', periods=365, freq='D')
values = np.cumsum(np.random.randn(365)) + 100

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(dates, values, linewidth=1)

ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Daily Time Series')
ax.grid(True, alpha=0.3)

# Format x-axis dates
import matplotlib.dates as mdates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

## 7.2 Multiple Time Series

```{python}
# Multiple series
values1 = np.cumsum(np.random.randn(365)) + 100
values2 = np.cumsum(np.random.randn(365)) + 95
values3 = np.cumsum(np.random.randn(365)) + 105

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(dates, values1, label='Series A', linewidth=1.5)
ax.plot(dates, values2, label='Series B', linewidth=1.5)
ax.plot(dates, values3, label='Series C', linewidth=1.5)

ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Multiple Time Series')
ax.legend()
ax.grid(True, alpha=0.3)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

## 7.3 Shaded Regions

```{python}
fig, ax = plt.subplots(figsize=(12, 5))

# Plot main series
ax.plot(dates, values1, label='Actual', color='blue', linewidth=2)

# Add confidence interval
lower = values1 - 10
upper = values1 + 10
ax.fill_between(dates, lower, upper, alpha=0.3, color='blue', label='Confidence')

ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.set_title('Time Series with Confidence Interval')
ax.legend()
ax.grid(True, alpha=0.3)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
```

### Your Turn: Visualize Trends

Create a time series plot of temperature, stock prices, or another temporal variable. Add annotations for notable events or shade periods of interest.

# 8. Heatmaps

Heatmaps visualize matrices using color.

## 8.1 Basic Heatmap

```{python}
# Create data matrix
data = np.random.randn(10, 12)

fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(data, cmap='RdBu_r', aspect='auto')

ax.set_xlabel('Column')
ax.set_ylabel('Row')
ax.set_title('Basic Heatmap')

# Add colorbar
plt.colorbar(im, ax=ax, label='Value')

plt.tight_layout()
plt.show()
```

## 8.2 Correlation Matrix

```{python}
# Generate correlated data
from scipy.stats import multivariate_normal

mean = [0, 0, 0, 0]
cov = [[1, 0.8, 0.3, 0.1],
       [0.8, 1, 0.5, 0.2],
       [0.3, 0.5, 1, 0.7],
       [0.1, 0.2, 0.7, 1]]

data = multivariate_normal.rvs(mean=mean, cov=cov, size=1000)
corr_matrix = np.corrcoef(data.T)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1, aspect='auto')

# Add labels
labels = ['Var A', 'Var B', 'Var C', 'Var D']
ax.set_xticks(range(len(labels)))
ax.set_yticks(range(len(labels)))
ax.set_xticklabels(labels)
ax.set_yticklabels(labels)

# Add correlation values
for i in range(len(labels)):
    for j in range(len(labels)):
        text = ax.text(j, i, f'{corr_matrix[i, j]:.2f}',
                      ha="center", va="center", color="black", fontsize=10)

ax.set_title('Correlation Matrix')
plt.colorbar(im, ax=ax, label='Correlation')

plt.tight_layout()
plt.show()
```

Common colormaps:
- **Sequential**: `viridis`, `plasma`, `Blues`, `Reds` (for continuous data)
- **Diverging**: `RdBu`, `coolwarm`, `seismic` (for data with meaningful center)
- **Qualitative**: `Set1`, `Set2`, `tab10` (for categories)

# 9. Pie Charts

Pie charts show proportions (use sparingly—bar charts are often clearer).

## 9.1 Basic Pie Chart

```{python}
# Data
categories = ['Category A', 'Category B', 'Category C', 'Category D']
sizes = [30, 25, 20, 25]
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(sizes, labels=categories, colors=colors,
                                   autopct='%1.1f%%', startangle=90)

# Improve text readability
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontweight('bold')

ax.set_title('Distribution by Category')
plt.tight_layout()
plt.show()
```

## 9.2 Exploded Pie Chart

```{python}
fig, ax = plt.subplots(figsize=(8, 6))

# Explode second slice
explode = (0, 0.1, 0, 0)

ax.pie(sizes, labels=categories, colors=colors, autopct='%1.1f%%',
       startangle=90, explode=explode, shadow=True)

ax.set_title('Exploded Pie Chart')
plt.tight_layout()
plt.show()
```

**When to use pie charts**: Only for showing parts of a whole with few categories (≤5). Often, a bar chart is clearer.

# 10. Subplots and Layouts

## 10.1 Grid of Subplots

```{python}
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top left: Line plot
x = np.linspace(0, 10, 100)
axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title('Line Plot')
axes[0, 0].grid(True, alpha=0.3)

# Top right: Scatter
axes[0, 1].scatter(np.random.randn(50), np.random.randn(50), alpha=0.6)
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].grid(True, alpha=0.3)

# Bottom left: Histogram
axes[1, 0].hist(np.random.randn(1000), bins=30, edgecolor='black', alpha=0.7)
axes[1, 0].set_title('Histogram')
axes[1, 0].grid(axis='y', alpha=0.3)

# Bottom right: Bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 32]
axes[1, 1].bar(categories, values, color='steelblue', edgecolor='black')
axes[1, 1].set_title('Bar Chart')
axes[1, 1].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()
```

Access subplots:
- `axes[row, col]` for 2D array
- `axes[i]` for 1D array (single row or column)
- `ax` for single subplot

## 10.2 Shared Axes

```{python}
fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

x = np.linspace(0, 10, 100)

axes[0].plot(x, np.sin(x))
axes[0].set_ylabel('sin(x)')
axes[0].grid(True, alpha=0.3)

axes[1].plot(x, np.cos(x), color='orange')
axes[1].set_ylabel('cos(x)')
axes[1].grid(True, alpha=0.3)

axes[2].plot(x, np.sin(x) * np.cos(x), color='green')
axes[2].set_ylabel('sin(x) × cos(x)')
axes[2].set_xlabel('x')
axes[2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

Parameters:
- `sharex=True`: Share x-axis (common scale)
- `sharey=True`: Share y-axis
- `sharex='col'`: Share within columns
- `sharey='row'`: Share within rows

# 11. Customization

## 11.1 Labels and Titles

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x))

# Labels with formatting
ax.set_xlabel('Time (seconds)', fontsize=14, fontweight='bold')
ax.set_ylabel('Amplitude (volts)', fontsize=14, fontweight='bold')
ax.set_title('Oscillating Signal', fontsize=16, fontweight='bold', pad=20)

# Subtitle (using text)
ax.text(0.5, 1.05, 'Measured at room temperature', 
        transform=ax.transAxes, ha='center', fontsize=10, style='italic')

ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## 11.2 Legends

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2)
ax.plot(x, np.sin(x) * np.cos(x), label='sin(x) × cos(x)', linewidth=2)

# Customize legend
ax.legend(loc='upper right',         # Location
          frameon=True,               # Show frame
          framealpha=0.9,            # Frame transparency
          fontsize=11,               # Font size
          title='Functions',         # Title
          title_fontsize=12)         # Title size

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

Legend locations: `'upper left'`, `'upper right'`, `'lower left'`, `'lower right'`, `'center'`, `'best'` (auto)

## 11.3 Annotations

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
ax.plot(x, y, linewidth=2)

# Annotate maximum
max_idx = np.argmax(y)
ax.annotate('Maximum', 
            xy=(x[max_idx], y[max_idx]),           # Point to annotate
            xytext=(x[max_idx] + 0.5, y[max_idx] + 0.3),  # Text location
            fontsize=12,
            arrowprops=dict(arrowstyle='->', color='red', lw=2))

# Annotate minimum
min_idx = np.argmin(y)
ax.annotate('Minimum',
            xy=(x[min_idx], y[min_idx]),
            xytext=(x[min_idx] + 0.5, y[min_idx] - 0.3),
            fontsize=12,
            arrowprops=dict(arrowstyle='->', color='blue', lw=2))

ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Annotated Plot')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 11.4 Grid, Spines, and Ticks

```{python}
fig, ax = plt.subplots(figsize=(10, 6))

x = np.linspace(-5, 5, 100)
y = x**2
ax.plot(x, y, linewidth=2)

# Customize grid
ax.grid(True, which='major', linestyle='-', linewidth=0.5, alpha=0.7)
ax.grid(True, which='minor', linestyle=':', linewidth=0.5, alpha=0.4)
ax.minorticks_on()

# Customize spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=12, length=6, width=2)
ax.tick_params(axis='both', which='minor', length=4, width=1)

ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y = x²', fontsize=14)
ax.set_title('Customized Grid and Spines', fontsize=16)

plt.tight_layout()
plt.show()
```

### Your Turn: Customize a Figure

Take one of your earlier plots and customize it with:
1. Meaningful axis labels with units
2. A descriptive title
3. A legend if multiple series
4. Annotations for key features
5. A clean grid

# 12. Saving Figures

## 12.1 File Formats

```python
# Save as PNG (web, presentations)
fig.savefig('figure.png', dpi=300, bbox_inches='tight')

# Save as PDF (publications, vector graphics)
fig.savefig('figure.pdf', bbox_inches='tight')

# Save as SVG (editable vector graphics)
fig.savefig('figure.svg', bbox_inches='tight')

# Save as JPG (compressed, smaller files)
fig.savefig('figure.jpg', dpi=300, quality=95, bbox_inches='tight')
```

Key parameters:
- `dpi`: Dots per inch (300 for publication, 150 for web)
- `bbox_inches='tight'`: Removes extra whitespace
- `transparent=True`: Transparent background (PNG, PDF)
- `facecolor='white'`: Background color

## 12.2 Complete Example with Save

```{python}
#| eval: false

# Create publication-quality figure
fig, ax = plt.subplots(figsize=(8, 6))

x = np.linspace(0, 10, 100)
y = np.exp(-x/5) * np.sin(x)

ax.plot(x, y, linewidth=2, color='darkblue')
ax.fill_between(x, 0, y, alpha=0.3, color='lightblue')

ax.set_xlabel('Time (s)', fontsize=14)
ax.set_ylabel('Amplitude', fontsize=14)
ax.set_title('Damped Oscillation', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)

# Save in multiple formats
plt.tight_layout()
fig.savefig('damped_oscillation.png', dpi=300, bbox_inches='tight')
fig.savefig('damped_oscillation.pdf', bbox_inches='tight')

print("Figures saved successfully")
plt.close(fig)  # Close to free memory
```

# 13. Choosing the Right Plot Type

| **Data Type** | **Purpose** | **Plot Type** |
|---------------|-------------|---------------|
| One continuous variable | Show distribution | Histogram, box plot |
| Two continuous variables | Show relationship | Scatter plot, line plot |
| Continuous over time | Show trend | Time series (line plot) |
| Continuous by category | Compare groups | Box plot, violin plot, bar chart |
| Counts by category | Compare frequencies | Bar chart |
| Parts of whole | Show proportions | Stacked bar, (pie chart) |
| Matrix/grid data | Show patterns | Heatmap |
| Multiple related series | Compare trends | Multiple line plots |

**General guidelines**:
- **Bar charts** > Pie charts (easier to compare)
- **Scatter plots** for raw data, **line plots** for aggregated/sequential data
- **Box plots** for distribution summaries, **histograms** for distribution shapes
- **Heatmaps** for large correlation matrices or grid patterns
- Use **subplots** to show multiple related views

# 14. Introduction to Seaborn

Seaborn builds on matplotlib with better defaults and statistical graphics.

## 14.1 Why Seaborn?

```{python}
import seaborn as sns

# Set seaborn style globally
sns.set_theme(style='whitegrid', palette='muted')

# Generate data
np.random.seed(42)
data = {
    'Group': ['A']*50 + ['B']*50 + ['C']*50,
    'Value': np.concatenate([
        np.random.randn(50) + 0,
        np.random.randn(50) + 2,
        np.random.randn(50) + 1
    ])
}
import pandas as pd
df = pd.DataFrame(data)

# Seaborn makes this easy
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Matplotlib version (verbose)
for i, group in enumerate(['A', 'B', 'C']):
    group_data = df[df['Group'] == group]['Value']
    axes[0].hist(group_data, alpha=0.5, label=group)
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Matplotlib')
axes[0].legend()

# Seaborn version (concise)
sns.histplot(data=df, x='Value', hue='Group', ax=axes[1], alpha=0.5)
axes[1].set_title('Seaborn')

plt.tight_layout()
plt.show()
```

## 14.2 Statistical Plots

```{python}
# Generate more complex data
np.random.seed(42)
data = pd.DataFrame({
    'x': np.random.randn(200),
    'y': np.random.randn(200),
    'category': np.random.choice(['A', 'B', 'C'], 200)
})
data['y'] = data['y'] + data['x'] * 0.5  # Create correlation

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Scatter with regression line
sns.regplot(data=data, x='x', y='y', ax=axes[0, 0])
axes[0, 0].set_title('Regression Plot')

# Scatter colored by category
sns.scatterplot(data=data, x='x', y='y', hue='category', ax=axes[0, 1])
axes[0, 1].set_title('Colored Scatter')

# Box plot by category
sns.boxplot(data=data, x='category', y='y', ax=axes[1, 0])
axes[1, 0].set_title('Box Plot by Category')

# Violin plot (like box plot but shows distribution)
sns.violinplot(data=data, x='category', y='y', ax=axes[1, 1])
axes[1, 1].set_title('Violin Plot')

plt.tight_layout()
plt.show()
```

## 14.3 Pair Plot

```{python}
# Generate multivariate data
data = pd.DataFrame(
    np.random.randn(200, 4),
    columns=['Var1', 'Var2', 'Var3', 'Var4']
)
data['Category'] = np.random.choice(['A', 'B'], 200)

# Pair plot shows all pairwise relationships
pair_grid = sns.pairplot(data, hue='Category', diag_kind='hist', height=2)
pair_grid.fig.suptitle('Pair Plot of Multiple Variables', y=1.02)
plt.tight_layout()
plt.show()
```

## 14.4 Heatmaps in Seaborn

```{python}
# Correlation matrix with seaborn
numeric_data = data[['Var1', 'Var2', 'Var3', 'Var4']]
corr = numeric_data.corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', 
            vmin=-1, vmax=1, center=0, square=True, ax=ax)
ax.set_title('Correlation Heatmap (Seaborn)')
plt.tight_layout()
plt.show()
```

Seaborn advantages:
- Better default aesthetics
- Automatic legends and colors
- Built-in statistical summaries
- Easy integration with pandas DataFrames
- Less code for common plots

When to use:
- **Seaborn**: Quick exploratory analysis, statistical graphics
- **Matplotlib**: Fine control, custom layouts, animations

# 15. Complete Example: Hurricane Analysis

Let's create a comprehensive figure analyzing hurricane data:

```{python}
# Generate synthetic hurricane data
np.random.seed(42)
years = np.arange(1980, 2024)
n_years = len(years)

hurricane_data = pd.DataFrame({
    'year': np.repeat(years, 20),
    'wind_speed': np.concatenate([np.random.gamma(2, 20, 20) + 50 + i*0.2 
                                  for i in range(n_years)]),
    'category': np.random.choice([1, 2, 3, 4, 5], n_years * 20, 
                                 p=[0.4, 0.3, 0.15, 0.1, 0.05])
})

# Create comprehensive figure
fig = plt.figure(figsize=(16, 10))
gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)

# 1. Time series of hurricane counts
ax1 = fig.add_subplot(gs[0, :])
yearly_counts = hurricane_data.groupby('year').size()
ax1.plot(yearly_counts.index, yearly_counts.values, linewidth=2, marker='o', markersize=4)
ax1.fill_between(yearly_counts.index, yearly_counts.values, alpha=0.3)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Hurricanes', fontsize=12)
ax1.set_title('Annual Hurricane Frequency (1980-2023)', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)

# 2. Distribution of wind speeds
ax2 = fig.add_subplot(gs[1, 0])
ax2.hist(hurricane_data['wind_speed'], bins=30, edgecolor='black', alpha=0.7, color='steelblue')
ax2.set_xlabel('Wind Speed (mph)', fontsize=11)
ax2.set_ylabel('Frequency', fontsize=11)
ax2.set_title('Wind Speed Distribution', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3)

# 3. Box plot by category
ax3 = fig.add_subplot(gs[1, 1])
categories = [hurricane_data[hurricane_data['category'] == i]['wind_speed'].values 
              for i in [1, 2, 3, 4, 5]]
bp = ax3.boxplot(categories, labels=['1', '2', '3', '4', '5'], patch_artist=True)
for patch in bp['boxes']:
    patch.set_facecolor('coral')
ax3.set_xlabel('Category', fontsize=11)
ax3.set_ylabel('Wind Speed (mph)', fontsize=11)
ax3.set_title('Wind Speed by Category', fontsize=12, fontweight='bold')
ax3.grid(axis='y', alpha=0.3)

# 4. Category distribution
ax4 = fig.add_subplot(gs[1, 2])
category_counts = hurricane_data['category'].value_counts().sort_index()
ax4.bar(category_counts.index, category_counts.values, 
        color=['#ffffcc', '#ffeda0', '#fed976', '#fc4e2a', '#bd0026'],
        edgecolor='black', alpha=0.8)
ax4.set_xlabel('Category', fontsize=11)
ax4.set_ylabel('Count', fontsize=11)
ax4.set_title('Hurricanes by Category', fontsize=12, fontweight='bold')
ax4.grid(axis='y', alpha=0.3)

# 5. Scatter: wind speed over time
ax5 = fig.add_subplot(gs[2, :2])
scatter = ax5.scatter(hurricane_data['year'], hurricane_data['wind_speed'],
                     c=hurricane_data['category'], cmap='YlOrRd', 
                     alpha=0.6, s=20, edgecolors='black', linewidth=0.3)
ax5.set_xlabel('Year', fontsize=12)
ax5.set_ylabel('Wind Speed (mph)', fontsize=12)
ax5.set_title('Hurricane Intensity Over Time', fontsize=12, fontweight='bold')
cbar = plt.colorbar(scatter, ax=ax5)
cbar.set_label('Category', fontsize=10)
ax5.grid(True, alpha=0.3)

# 6. Average intensity by decade
ax6 = fig.add_subplot(gs[2, 2])
hurricane_data['decade'] = (hurricane_data['year'] // 10) * 10
decade_avg = hurricane_data.groupby('decade')['wind_speed'].mean()
ax6.bar(decade_avg.index, decade_avg.values, width=8, 
        color='darkred', edgecolor='black', alpha=0.7)
ax6.set_xlabel('Decade', fontsize=11)
ax6.set_ylabel('Avg Wind Speed (mph)', fontsize=11)
ax6.set_title('Average Intensity by Decade', fontsize=12, fontweight='bold')
ax6.grid(axis='y', alpha=0.3)

# Overall title
fig.suptitle('Atlantic Hurricane Analysis (1980-2023)', 
             fontsize=18, fontweight='bold', y=0.995)

plt.show()
```

# Summary

You now have the tools to create effective data visualizations in Python:

**Core Skills**:
- Object-oriented matplotlib interface (`fig, ax = plt.subplots()`)
- Essential plot types (line, scatter, bar, histogram, box, time series, heatmap)
- Customization (labels, legends, colors, annotations)
- Subplots and layouts
- Saving figures in multiple formats

**Best Practices**:
- Choose appropriate plot types for your data
- Label axes clearly with units
- Add informative titles
- Use color meaningfully
- Make figures self-contained
- Save at appropriate resolution

**Next Steps**:
- Explore seaborn for statistical graphics
- Learn `plotly` for interactive visualizations
- Study data visualization principles (Tufte, Cleveland)
- Practice making figures that communicate clearly

Visualization is both art and science. Technical skill with matplotlib is necessary, but thoughtful design—choosing the right plot type, using color effectively, removing clutter—is what makes figures truly communicate. Practice with real data, seek feedback, and study well-designed figures to develop your judgment.

Now go visualize your data!