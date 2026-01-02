# Section 3: Data Transformation - Comparison Tables

## Big Data Processing Service Comparisons

### EMR vs Glue vs Athena

| Criteria | Amazon EMR | AWS Glue | Amazon Athena |
|----------|------------|----------|---------------|
| **Purpose** | Full Hadoop/Spark cluster | Serverless ETL | Serverless SQL queries |
| **Processing** | Batch/streaming | Batch ETL | Interactive queries |
| **Infrastructure** | EC2 clusters (managed) | Fully serverless | Fully serverless |
| **Pricing** | Per-hour + EC2 | Per DPU-hour | Per TB scanned |
| **Best For** | Complex Spark jobs, HPC | ETL pipelines, catalog | Ad-hoc S3 queries |
| **Languages** | Spark, Hive, Presto, etc. | Python, Scala | SQL (Presto) |

**Decision Guide:**
- Need full Spark control? → **EMR**
- Simple ETL to/from S3? → **Glue**
- Query S3 with SQL? → **Athena**

---

### EMR Variants Comparison

| Variant | Cluster Management | Use Case |
|---------|-------------------|----------|
| **EMR on EC2** | You manage instances | Full control, custom config |
| **EMR Serverless** | AWS manages capacity | Variable workloads, no ops |
| **EMR on EKS** | Run on Kubernetes | Share K8s resources |

---

### EMR Node Types

| Node Type | Runs Tasks | Hosts HDFS | Spot Instances | Failure Impact |
|-----------|-----------|------------|----------------|----------------|
| **Master** | Coordinates | No | Not recommended | Cluster fails |
| **Core** | Yes | Yes | Use cautiously | Data loss risk |
| **Task** | Yes | No | Good fit | No data loss |

---

## Data Preparation Tool Comparisons

### Glue DataBrew vs SageMaker Data Wrangler

| Criteria | AWS Glue DataBrew | SageMaker Data Wrangler |
|----------|-------------------|------------------------|
| **Purpose** | General data preparation | ML-focused data prep |
| **Transformations** | 250+ | 300+ |
| **Interface** | Standalone service | SageMaker Studio |
| **Output** | S3 | Processing jobs, Pipelines, Feature Store |
| **Target Users** | Data engineers | Data scientists |
| **ML Integration** | Limited | Deep SageMaker integration |
| **Quick Model** | No | Yes (rapid evaluation) |
| **PII Handling** | Yes (extensive) | Yes |

**Decision Guide:**
- General ETL/data prep? → **Glue DataBrew**
- ML pipeline integration? → **Data Wrangler**

---

### Ground Truth vs Ground Truth Plus

| Criteria | Ground Truth | Ground Truth Plus |
|----------|--------------|-------------------|
| **Setup** | Self-managed workflow | AWS-managed workflow |
| **Labelers** | You choose (Turk, internal, vendors) | AWS expert workforce |
| **Configuration** | Manual | Intake form |
| **Monitoring** | You manage | Project Portal |
| **Cost** | Pay per task | Managed service pricing |

**Decision Guide:**
- Have labeling expertise? → **Ground Truth**
- Want turnkey solution? → **Ground Truth Plus**

---

## Feature Engineering Technique Comparisons

### Missing Data Strategies

| Strategy | Speed | Accuracy | Data Preserved | Use When |
|----------|-------|----------|----------------|----------|
| **Mean/Median** | Fast | Low | Yes | Quick baseline |
| **Drop Rows** | Fast | N/A | No | Few missing values |
| **Drop Columns** | Fast | N/A | No | Feature mostly missing |
| **KNN Imputation** | Slow | High | Yes | Similar records exist |
| **MICE** | Slow | High | Yes | Complex missing patterns |
| **Deep Learning** | Slow | High | Yes | Large datasets, complex patterns |

---

### Unbalanced Data Techniques

| Technique | Creates New Data | Risk | Best For |
|-----------|------------------|------|----------|
| **Oversampling** | No (duplicates) | Overfitting | Small minority class |
| **SMOTE** | Yes (synthetic) | Some overfitting | Moderate minority class |
| **Undersampling** | No | Info loss | Large majority class |
| **Class Weights** | No | None | Any imbalance |

**SMOTE is generally preferred over simple oversampling**

---

### Encoding Methods

| Method | Output | Ordinal Relationship | Use Case |
|--------|--------|---------------------|----------|
| **One-Hot** | Binary vectors | No | Categories with no order |
| **Label Encoding** | Integer | Yes (implied) | Ordinal categories |
| **Target Encoding** | Continuous | N/A | High cardinality |

---

### Scaling Methods

| Method | Formula | Output Range | Use Case |
|--------|---------|--------------|----------|
| **Min-Max** | (x-min)/(max-min) | [0, 1] | Bounded algorithms |
| **Standardization** | (x-μ)/σ | ~[-3, 3] | Neural networks |
| **Robust Scaling** | Uses median/IQR | Variable | Data with outliers |

---

## SageMaker Service Comparisons

### Model Monitoring Tools

| Tool | Purpose | Detects |
|------|---------|---------|
| **Model Monitor** | Production quality | Data drift, anomalies, schema changes |
| **Clarify** | Bias & explainability | Pre/post-training bias, feature importance |

---

### Feature Store Types

| Store Type | Latency | Storage | Use Case |
|------------|---------|---------|----------|
| **Online Store** | Single-digit ms | Low-latency DB | Real-time inference |
| **Offline Store** | Minutes | S3 (Parquet) | Training, batch scoring |

---

### SageMaker Clarify Bias Metrics

| Metric | Abbreviation | Measures |
|--------|--------------|----------|
| Class Imbalance | CI | Unequal training samples |
| Difference in Proportions | DPL | Outcome rate differences |
| KL Divergence | KL | Distribution divergence |
| Jensen-Shannon | JS | Symmetric divergence |
| Kolmogorov-Smirnov | KS | Max distribution difference |

---

## Athena Comparisons

### Athena Data Formats

| Format | Type | Splittable | Query Performance | Cost Efficiency |
|--------|------|------------|-------------------|-----------------|
| **CSV** | Row | No | Slow | Low |
| **JSON** | Row | No | Slow | Low |
| **Parquet** | Columnar | Yes | Fast | High (30-90% savings) |
| **ORC** | Columnar | Yes | Fast | High |
| **Avro** | Row | Yes | Medium | Medium |

**Best Practice:** Convert to Parquet/ORC for cost savings

---

### Athena Encryption Options

| Type | Key Management | Use Case |
|------|----------------|----------|
| **SSE-S3** | AWS managed | Simple, default |
| **SSE-KMS** | Customer via KMS | Audit trail needed |
| **CSE-KMS** | Client-side with KMS | Encrypt before storing |

---

## Quick Reference Decision Trees

### Data Processing Decision

```
Need to transform data?
├── Simple ETL to S3 → AWS Glue
├── Visual preparation → Glue DataBrew or Data Wrangler
├── Complex Spark jobs → EMR
└── Just query S3 → Athena
```

### Data Labeling Decision

```
Need labeled training data?
├── Self-managed workflow → Ground Truth
├── Turnkey solution → Ground Truth Plus
├── Auto-label images → Rekognition
└── Auto-label text → Comprehend
```

### Model Quality Decision

```
Monitor deployed model?
├── Data drift detection → Model Monitor
├── Bias detection → Clarify
├── Explain predictions → Clarify (SHAP)
└── Feature management → Feature Store
```

### Missing Data Decision

```
Handle missing values?
├── Quick baseline → Mean/Median imputation
├── Few missing → Drop rows
├── Accurate needed → KNN or MICE
└── Complex patterns → Deep Learning
```

### Unbalanced Data Decision

```
Handle class imbalance?
├── Small minority → Oversampling
├── Need synthetic data → SMOTE
├── Large majority → Undersampling
└── Algorithm supports → Class weights
```

---

## Exam Pattern Quick Answers

| Question Pattern | Answer |
|------------------|--------|
| "Serverless ETL service" | AWS Glue |
| "Visual data prep with recipes" | Glue DataBrew |
| "Visual data prep for ML" | SageMaker Data Wrangler |
| "Query S3 without loading" | Amazon Athena |
| "Reduce Athena query costs" | Use Parquet/ORC, partitions |
| "Convert CSV to Parquet in Athena" | CTAS |
| "ACID transactions on S3 data lake" | Athena + Apache Iceberg |
| "Label training data with humans" | Ground Truth |
| "Managed labeling service" | Ground Truth Plus |
| "Detect drift in production model" | Model Monitor |
| "Detect bias in training data" | Clarify (pre-training) |
| "Explain model predictions" | Clarify (SHAP) |
| "Anomaly detection algorithm" | Random Cut Forest |
| "Synthetic minority oversampling" | SMOTE |
| "Real-time feature serving" | Feature Store (Online) |
| "No-code ML tool" | SageMaker Canvas |
| "Data quality rules in Glue" | Glue Data Quality (DQDL) |
| "Handle PII in data" | Glue DataBrew transformations |
| "Spark on Kubernetes" | EMR on EKS |
| "Auto-scaling Spark" | EMR Serverless |
