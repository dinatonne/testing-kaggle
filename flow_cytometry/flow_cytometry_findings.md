# Flow Cytometry Data Analysis — Findings Overview
**Dataset:** Rituximab Flow Cytometry Data  
**Tools:** JupyterLab (exploration & visualisation) + VS Code (structured scripts)

---

## Part 1: JupyterLab Analysis

### 1. Data Loading & Preview
- Loaded the dataset and previewed the first and last rows (`df.head()`, `df.tail()`)
- **1,545 cells** measured across **9 parameters:** FSC.H, SSC.H, FL1.H, FL2.H, FL3.H, FL1.A, FL1.W, Time, Gate

### 2. Data Quality Check
- All columns are numeric (`int64`) — no text data
- **No missing values** across any column — the dataset is complete and clean
- Summary statistics show FSC.H and SSC.H range from ~11 to 1023 (arbitrary units)

### 3. Cell Population Breakdown (Gating)

| Gate | Cell Count | Percentage |
|---|---|---|
| Gate 1 | 1,080 | 69.9% |
| Gate 2 | 294 | 19.0% |
| Gate -1 | 171 | 11.1% |

Gate 1 is the dominant population, making up ~70% of all measured cells.

### 4. Average Fluorescence per Gate

| Gate | FL1.H | FL2.H | FL3.H |
|---|---|---|---|
| Gate -1 | 519.0 | 203.8 | 464.2 |
| Gate 1 | 228.6 | 101.4 | 192.1 |
| Gate 2 | 693.1 | 173.3 | 382.0 |

Gate 2 shows the highest FL1 fluorescence (693.1), suggesting the strongest marker expression. Gate -1 shows high fluorescence despite being the negative gate.

### 5. Visualisations Produced in Jupyter

**FSC vs SSC scatter plot**
- Classic flow cytometry plot showing cell size vs granularity
- Cells cluster in distinct regions reflecting different populations

**FSC vs SSC coloured by gate**
- Gate -1 cells are larger and more granular (higher FSC and SSC)
- Gate 1 cells cluster tightly at lower FSC/SSC values
- Gate 2 cells show intermediate scatter properties

**Fluorescence distributions (FL1, FL2, FL3)**
- All three channels show right-skewed distributions
- Most cells have low-to-mid fluorescence with a tail of highly expressing cells

**Channel correlations**

| | FSC.H | SSC.H | FL1.H | FL2.H | FL3.H |
|---|---|---|---|---|---|
| FSC.H | 1.00 | 0.67 | 0.61 | 0.60 | 0.83 |
| SSC.H | 0.67 | 1.00 | 0.28 | 0.62 | 0.48 |
| FL1.H | 0.61 | 0.28 | 1.00 | 0.55 | 0.69 |
| FL2.H | 0.60 | 0.62 | 0.55 | 1.00 | 0.49 |
| FL3.H | 0.83 | 0.48 | 0.69 | 0.49 | 1.00 |

FSC.H and FL3.H have the strongest correlation (0.83) — larger cells tend to have higher FL3 expression.

**FL1 vs FL2 scatter plot (coloured by gate)**
- Clear separation between gates visible in fluorescence space

**Cell size distribution by gate**
- Gate -1 cells are significantly larger than Gate 1 cells
- Gate 1 shows a tight, narrow size distribution

**Box plots & violin plots (FL1, FL2, FL3 by gate)**
- Gate 2 shows the widest spread of FL1 values — highest variability in expression
- Gate 1 has the most consistent fluorescence levels

**Time series — cell size and granularity over time**
- FSC.H and SSC.H remain relatively stable throughout the run
- No major instrument issues or flow rate changes detected

**Live vs dead cell classification**

| Population | Cell Count |
|---|---|
| Live cells (FSC > 200) | 1,031 |
| Dead cells (FSC ≤ 200) | 514 |

33% of cells are classified as dead/debris based on low forward scatter.

**Coefficient of Variation (CV)**

| Channel | CV (%) |
|---|---|
| FSC.H | 62.07 |
| SSC.H | 74.12 |
| FL1.H | 67.12 |
| FL2.H | 71.87 |
| FL3.H | 74.42 |

High CV values reflect natural biological variability across mixed cell populations — expected in this type of sample.

**Correlation heatmap**
- Visual confirmation of the correlation table above
- FSC.H–FL3.H and FSC.H–SSC.H are the strongest relationships

---

## Part 2: VS Code Analysis (ritu_analysis.py)

### 1. Basic Data Quality Check
- Confirmed dataset shape (1,545 rows × 9 columns) and zero missing values
- Descriptive statistics consistent with Jupyter findings

### 2. Cell Population Breakdown
- Same gate distribution as above: Gate 1 (69.9%), Gate 2 (19.0%), Gate -1 (11.1%)

### 3. Outlier Detection

| Metric | Value |
|---|---|
| Total cells | 1,545 |
| Outlier cells (±3 SD from mean FSC) | 46 |
| Outlier percentage | 2.98% |

46 cells fall outside 3 standard deviations from the mean FSC — these could be doublets or debris and would typically be excluded from a real analysis pipeline.

### 4. Gate Population Comparison

| Gate | Mean FSC | Mean SSC | Mean FL1 |
|---|---|---|---|
| Gate -1 | 512.1 | 513.3 | 519.0 |
| Gate 1 | 237.8 | 217.1 | 228.6 |
| Gate 2 | 337.4 | 227.3 | 693.1 |

Gate -1 cells are the largest and most granular. Gate 2 has the highest FL1 fluorescence despite moderate size — suggesting high marker expression independent of cell size.

### 5. Coefficient of Variation
- Results consistent with Jupyter: all channels show CV between 62–74%
- Confirms high but expected biological variability across the mixed population

---

## Key Takeaways

1. The dataset is complete with no missing values
2. Three distinct cell populations identified by gating — Gate 1 is dominant at 70%
3. Gate 2 shows the highest FL1 fluorescence, suggesting strongest marker expression
4. ~3% of cells are outliers by FSC — likely debris or doublets
5. ~33% of cells fall below the live/dead threshold (FSC ≤ 200)
6. FSC and FL3.H are most strongly correlated (0.83)
7. CV values are high but expected for a mixed biological sample
8. Time series shows a stable run with no instrument issues
