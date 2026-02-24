## **Your Daily Workflow & Commit Practices**

### **Start of Day:**
```bash
# Activate env
source .env/bin/activate

# Get latest code & data
git pull
dvc pull
```

### **During Work:**
```bash
# 1. Create/update notebooks in notebooks/
# 2. Write modular code in src/
# 3. Generate outputs to reports/figures/
# 4. Save processed data to data/processed/ when ready
```

### **Commit Strategy by Type:**

#### **Code Changes (Git):**
```bash
# After adding a feature
git add src/feature_engineering.py
git commit -m "feat: add age binning transformation"
git push

# After fixing a bug
git add src/preprocessing.py
git commit -m "fix: handle missing values in balance column"
git push
```

#### **Notebook Changes (Git):**
```bash
# Clear outputs first! (smaller diffs)
git add notebooks/03_feature_analysis.ipynb
git commit -m "feat: add correlation analysis notebook"
git push
```

#### **Data Changes (DVC + Git):**
```bash
# After creating processed dataset
dvc add data/processed/
git add data/processed.dvc
git commit -m "data: add clean features for modeling"
dvc push        # Backs up to local remote
git push        # Pushes code + pointer
```

#### **Documentation (Git):**
```bash
git add README.md references/
git commit -m "docs: update project setup instructions"
git push
```

#### **Experiment Results (Git):**
```bash
git add reports/figures/confusion_matrix.png
git add reports/metrics.csv
git commit -m "experiment: initial random forest results"
git push
```

### **End of Day:**
```bash
# Ensure everything is committed
git status        # Should be clean
dvc status        # Should be clean

# Push everything
git push
dvc push
```

## **Golden Rules:**
- **Small, focused commits** (one logical change per commit)
- **Clear messages** using conventional commits
- **Never commit data to Git** (only DVC pointers)
- **Push daily** (code to GitHub, data to local remote)

This signals professionalism and reproducibility to any reviewer.