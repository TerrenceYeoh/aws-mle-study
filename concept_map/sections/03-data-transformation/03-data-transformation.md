# Section 3: Data Transformation, Integrity, and Feature Engineering

## Overview
This section covers data processing services (EMR, Glue, Athena), feature engineering techniques, and SageMaker tools for data preparation, labeling, and monitoring. Key areas include distributed processing with Spark, handling missing/unbalanced data, and ML model explainability.

---

## Core Concepts

### Feature Engineering

The process of applying domain knowledge to create better features for ML models.

**Key Techniques:**

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **TF-IDF** | Term Frequency-Inverse Document Frequency | Text/search relevance |
| **N-grams** | Contiguous sequences of N words | Text classification, NLP |
| **One-Hot Encoding** | Convert categorical to binary vectors | Non-ordinal categories |
| **Binning** | Convert continuous to discrete categories | Age groups, reduce noise |
| **Scaling** | Normalize feature ranges | Neural networks, distance-based algorithms |
| **Log Transform** | Compress exponential distributions | Skewed data |

**"Applied machine learning is basically feature engineering" - Andrew Ng**

### The Curse of Dimensionality
- Too many features → sparse data → poor performance
- Solutions: Feature selection, PCA, K-Means clustering

---

### Handling Missing Data

| Strategy | Description | Pros | Cons |
|----------|-------------|------|------|
| **Mean/Median/Mode** | Replace with average | Fast, simple | Loses variance |
| **Drop Rows** | Remove incomplete records | Clean data | Loses data |
| **KNN Imputation** | Use similar records | More accurate | Computationally expensive |
| **MICE** | Multiple Imputation by Chained Equations | Handles uncertainty | Complex |
| **Deep Learning** | Neural network predicts values | Learns patterns | Requires training |

**Exam Tip:** Mean replacement is fast but NOT the most accurate approach

---

### Handling Unbalanced Data

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Oversampling** | Duplicate minority samples | Have sufficient minority data |
| **SMOTE** | Create synthetic minority samples | Need more minority data |
| **Undersampling** | Remove majority samples | Have lots of majority data |
| **Class Weights** | Penalize minority misclassification | Built into algorithm |

**SMOTE (Synthetic Minority Oversampling Technique):**
- Creates synthetic samples (not duplicates)
- Interpolates between existing minority samples
- Generally better than simple oversampling

---

### Outlier Detection

**Statistical Methods:**
- Standard deviation: Points > X σ from mean
- Variance: Measures data spread

**AWS Algorithm:** Random Cut Forest (RCF)
- Found in: QuickSight, Kinesis Analytics, SageMaker
- Assigns anomaly score to each data point

**When to Remove:**
- Bot traffic: Yes
- Power users: Maybe
- Billionaires in income data: No (legitimate)
- Sensor malfunction: Yes

---

### Scaling/Normalization

| Method | Formula | Range | Use Case |
|--------|---------|-------|----------|
| **Min-Max** | (x - min)/(max - min) | [0, 1] | Bounded range needed |
| **Standardization** | (x - μ)/σ | ~[-3, 3] | Neural networks |

**Important:** Apply same scaling to training, test, and prediction data

---

## Big Data Processing Services

### Amazon EMR - Elastic MapReduce

**What:** Managed Hadoop framework on EC2

**Cluster Architecture:**

| Node Type | Role | HDFS Data | Spot Instances |
|-----------|------|-----------|----------------|
| **Master** | Manages cluster | No | Not recommended |
| **Core** | Runs tasks + hosts HDFS | Yes | Use cautiously |
| **Task** | Runs tasks only | No | Good fit |

**Usage Patterns:**

| Pattern | Description | Instance Strategy |
|---------|-------------|-------------------|
| **Transient** | Spin up for job, terminate | Spot for task nodes |
| **Long-Running** | Always-on | Reserved instances |

**Storage Options:**
- **HDFS:** Fast, ephemeral
- **EMRFS:** S3 access as HDFS (persistent, durable)
- **EBS:** Persistent HDFS

---

### EMR Serverless

- Choose EMR Release and Runtime (Spark, Hive, Presto)
- EMR manages underlying capacity automatically
- Works across multiple AZs

**Key APIs:** CreateApplication, StartApplication, StopApplication, DeleteApplication

---

### EMR on EKS

- Run Spark jobs on Elastic Kubernetes Service
- Share resources between Spark and other K8s apps
- Runs on EC2 or Fargate

---

### Apache Spark

**Components:**

| Component | Purpose |
|-----------|---------|
| **Spark Core** | RDDs, task scheduling |
| **Spark SQL** | SQL on structured data |
| **Spark Streaming** | Real-time processing |
| **MLLib** | Machine learning library |
| **GraphX** | Graph processing |

**Architecture:** Driver Program → Cluster Manager → Executors

**MLLib Algorithms:** Logistic regression, Naive Bayes, K-Means, ALS, LDA, PCA, SVD

---

### AWS Glue

**Purpose:** Serverless ETL and data catalog service

**Key Components:**

| Component | Purpose |
|-----------|---------|
| **Glue Crawler** | Scans data, infers schema |
| **Glue Data Catalog** | Stores table metadata |
| **Glue ETL Jobs** | Transform and move data |
| **Glue Studio** | Visual ETL editor |
| **Glue Data Quality** | Define rules with DQDL |
| **Glue DataBrew** | Visual data preparation |

**Data Quality Definition Language (DQDL) Rules:**
- RowCount, IsComplete, ColumnLength, StandardDeviation, ColumnValues

---

### AWS Glue DataBrew

**Purpose:** Visual data preparation tool

**Features:**
- 250+ ready-made transformations
- Create reusable "recipes"
- Input: S3, Redshift, databases
- Output: S3

**PII Handling Methods:**
- REPLACE_WITH_RANDOM, SHUFFLE_ROWS
- DETERMINISTIC_ENCRYPT, ENCRYPT, DECRYPT
- MASK_CUSTOM, CRYPTOGRAPHIC_HASH, DELETE

---

### Amazon Athena

**Purpose:** Serverless SQL queries on S3 data

**Key Features:**
- Presto under the hood
- Pay-per-query: **$5 per TB scanned**
- No data loading required
- Supports CSV, JSON, Parquet, ORC, Avro

**Cost Optimization:**
- Use columnar formats (Parquet, ORC): Save 30-90%
- Use partitions
- Few large files > many small files

**ACID Transactions:** Powered by Apache Iceberg
- `'table_type' = 'ICEBERG'` in CREATE TABLE
- Supports time travel operations

**CTAS (CREATE TABLE AS SELECT):**
- Convert data formats (CSV → Parquet)
- Create subsets of tables

---

## SageMaker Services

### SageMaker Notebooks
- EC2-based Jupyter notebooks
- Pre-installed: Scikit-learn, TensorFlow, PyTorch, Spark
- Direct S3 access

### SageMaker Processing
- Run data processing workloads
- Input: `/opt/ml/processing/input`
- Output: `/opt/ml/processing/output`

### SageMaker Ground Truth
**Purpose:** Generate labeled training data

**How It Works:**
1. Raw data submitted
2. Model starts auto-labeling
3. Ambiguous data sent to humans
4. Human labels improve model
5. Can reduce labeling costs by **70%**

**Labeler Sources:** Mechanical Turk, Internal team, Professional companies

### SageMaker Ground Truth Plus
- Turnkey managed solution
- AWS experts manage workflow

### SageMaker Data Wrangler
**Purpose:** Visual data preparation in SageMaker Studio

**Features:**
- 300+ built-in transformations
- Custom transforms (Pandas, PySpark)
- "Quick Model" for rapid evaluation
- Balance data, handle missing values, detect outliers

### SageMaker Model Monitor
**Purpose:** Monitor deployed models

**Detects:**
- Data drift
- Anomalies
- Outliers
- Schema changes

### SageMaker Clarify
**Purpose:** Bias detection and model explainability

**Pre-Training Bias Metrics:**
- Class Imbalance (CI)
- Difference in Proportions of Labels (DPL)
- KL Divergence, Jensen-Shannon Divergence
- Kolmogorov-Smirnov (KS)

**Explainability:** SHAP values, Partial Dependence Plots

### SageMaker Feature Store
**Purpose:** Centralized feature repository

| Store Type | Latency | Use Case |
|------------|---------|----------|
| **Online Store** | Single-digit ms | Real-time inference |
| **Offline Store** | Higher | Training, batch processing |

### SageMaker Canvas
- No-code ML for business analysts
- Natural language or visual model building

---

## Model Explainability

### SHAP (SHapley Additive exPlanations)
- Based on game theory
- Shows feature contribution to predictions
- Both local (single prediction) and global (overall) explanations

### Partial Dependence Plots (PDPs)
- Show relationship between feature and prediction
- Marginal effect of one feature

---

## Concept Relationships

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Data Sources                                  │
│              (S3, Databases, Streaming)                             │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │   AWS Glue    │ │  Amazon EMR   │ │ Glue DataBrew │
    │ (ETL/Catalog) │ │(Spark/Hadoop) │ │ (Visual Prep) │
    └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
            │                 │                 │
            └────────────────┬┴─────────────────┘
                             ▼
              ┌──────────────────────────────┐
              │     Amazon Athena (Query)     │
              │     (S3 Data Lake)            │
              └──────────────┬───────────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │  SageMaker    │ │ Ground Truth  │ │ Data Wrangler │
    │  Training     │ │  (Labeling)   │ │   (Prep)      │
    └───────┬───────┘ └───────────────┘ └───────────────┘
            │
            ▼
    ┌───────────────────────────────────────────────────┐
    │         SageMaker Model Deployment                 │
    │  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │
    │  │   Monitor   │  │   Clarify   │  │  Feature  │  │
    │  │ (Drift)     │  │  (Bias)     │  │   Store   │  │
    │  └─────────────┘  └─────────────┘  └───────────┘  │
    └───────────────────────────────────────────────────┘
```

---

## Exam Tips

### Service Selection Guide

| Scenario | Service |
|----------|---------|
| "Serverless ETL" | AWS Glue |
| "Visual data preparation" | Glue DataBrew or SageMaker Data Wrangler |
| "Query S3 with SQL" | Amazon Athena |
| "Distributed processing with Spark" | EMR or EMR Serverless |
| "Label training data" | SageMaker Ground Truth |
| "Detect data drift" | SageMaker Model Monitor |
| "Detect bias in data/model" | SageMaker Clarify |
| "Explain model predictions" | SHAP via SageMaker Clarify |
| "No-code ML" | SageMaker Canvas |
| "Feature management" | SageMaker Feature Store |
| "Data quality rules" | AWS Glue Data Quality |

### Key Differentiators

| Question Pattern | Answer |
|------------------|--------|
| "Anomaly detection algorithm" | Random Cut Forest |
| "Convert CSV to Parquet in Athena" | CTAS (CREATE TABLE AS SELECT) |
| "Reduce Athena costs" | Use columnar formats, partitions |
| "Synthetic oversampling" | SMOTE |
| "Managed labeling service" | Ground Truth Plus |
| "300+ transformations visual" | SageMaker Data Wrangler |
| "250+ transformations visual" | Glue DataBrew |
| "ACID transactions on S3" | Athena with Apache Iceberg |

---

## Related Sections
- [[02-data-ingestion/02-data-ingestion]] - S3, Kinesis, streaming data
- [[04-managed-ai-services/04-managed-ai-services]] - Rekognition, Comprehend
- [[05-sagemaker-algorithms/05-sagemaker-algorithms]] - Built-in algorithms
- [[06-model-training/06-model-training]] - Training techniques
- [[09-mlops/09-mlops]] - Pipelines and automation
