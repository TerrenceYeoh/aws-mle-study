# Section 5: SageMaker Built-In Algorithms - Comparison Tables

## Algorithm Selection by Problem Type

| Problem Type | Algorithm | When to Use |
|--------------|-----------|-------------|
| **Linear regression** | Linear Learner | Simple linear relationships |
| **Classification (tabular)** | XGBoost, LightGBM | Structured/tabular data, Kaggle-style problems |
| **Classification (simple)** | Linear Learner, KNN | When interpretability matters |
| **Text classification** | BlazingText | Label sentences/documents |
| **Image classification** | Image Classification | Classify what's in image |
| **Object location** | Object Detection | Find WHERE objects are |
| **Pixel classification** | Semantic Segmentation | Self-driving, medical imaging |
| **Time series forecasting** | DeepAR | Multiple related time series |
| **Anomaly detection (time series)** | Random Cut Forest | Spikes, breaks in patterns |
| **Anomaly detection (IP/security)** | IP Insights | Suspicious login detection |
| **Clustering** | K-Means | Group similar items |
| **Dimensionality reduction** | PCA | Reduce features, visualization |
| **Topic modeling (GPU)** | Neural Topic Model | Document organization |
| **Topic modeling (CPU)** | LDA | Cheaper alternative to NTM |
| **Recommendations (sparse)** | Factorization Machines | User-item interactions |
| **Embeddings (words)** | BlazingText (Word2Vec) | Word vectors |
| **Embeddings (objects)** | Object2Vec | Arbitrary object embeddings |
| **Translation/summarization** | Seq2Seq | Sequence-to-sequence tasks |

---

## Instance Type Comparison

| Algorithm | Training Instance | Inference Instance | Notes |
|-----------|-------------------|-------------------|-------|
| **Linear Learner** | CPU or GPU | CPU or GPU | Multi-GPU doesn't help |
| **XGBoost** | M5 (CPU) or P2/P3 (GPU) | CPU or GPU | Memory-bound; set `tree_method=gpu_hist` |
| **LightGBM** | M5 (CPU only) | CPU | Memory-bound; no GPU support |
| **KNN** | ml.m5.2xlarge or ml.p2.xlarge | CPU (latency) or GPU (throughput) | |
| **K-Means** | CPU recommended | CPU | GPU uses only 1 GPU |
| **PCA** | CPU or GPU | CPU or GPU | Data-dependent |
| **DeepAR** | Start CPU, GPU if batch>512 | CPU only | |
| **Seq2Seq** | GPU only (P3) | GPU | Single machine only |
| **BlazingText** | C5 (<2GB) or GPU (>2GB) | CPU | |
| **NTM** | GPU recommended | CPU OK | |
| **LDA** | CPU only | CPU | Single instance only |
| **Object Detection** | GPU required | CPU or GPU | Multi-GPU OK |
| **Image Classification** | GPU | CPU or GPU | Multi-GPU OK |
| **Semantic Segmentation** | GPU | CPU or GPU | Multi-GPU OK |
| **Random Cut Forest** | CPU only (M4/C4/C5) | ml.c5.xl | No GPU support |
| **IP Insights** | GPU (ml.p3.2xlarge) | CPU or GPU | Multi-GPU OK |
| **Object2Vec** | CPU or GPU | ml.p3.2xlarge | Single machine only |
| **Factorization Machines** | CPU recommended | CPU | GPU only for dense data |

---

## Input Format Comparison

| Algorithm | RecordIO-Protobuf | CSV | Other Formats | Notes |
|-----------|-------------------|-----|---------------|-------|
| **Linear Learner** | Float32 | First col = label | | |
| **XGBoost** | Yes | Yes | libsvm, Parquet | |
| **LightGBM** | No | txt/csv | | |
| **KNN** | Yes | First col = label | | |
| **K-Means** | Yes | Yes | | |
| **PCA** | Yes | Yes | | |
| **DeepAR** | No | No | JSON lines, Gzip, Parquet | |
| **Seq2Seq** | Integers only | No | | Tokens must be integers |
| **BlazingText** | No | `__label__X text` | Augmented manifest | |
| **NTM** | Yes | Yes | | Words tokenized to integers |
| **LDA** | Yes | Yes | | Pipe mode only with RecordIO |
| **Object Detection** | Yes | No | Images + JSON annotations | |
| **Image Classification** | No | No | Images | Default 224x224 |
| **Semantic Segmentation** | No | No | JPG + PNG annotations | |
| **Random Cut Forest** | Yes | Yes | | |
| **IP Insights** | No | CSV only | | Entity, IP format |
| **Object2Vec** | No | No | JSON lines | Tokenized integer pairs |
| **Factorization Machines** | Float32 only | No | | CSV impractical for sparse |

---

## Supervised vs Unsupervised

| Supervised | Unsupervised | Both/Depends |
|------------|--------------|--------------|
| Linear Learner | K-Means | KNN |
| XGBoost | PCA | Object2Vec |
| LightGBM | Random Cut Forest | DeepAR |
| Seq2Seq | Neural Topic Model | |
| BlazingText (classification) | LDA | |
| Object Detection | BlazingText (Word2Vec) | |
| Image Classification | IP Insights | |
| Semantic Segmentation | | |
| Factorization Machines | | |

---

## NLP Algorithm Comparison

| Aspect | BlazingText (Classification) | BlazingText (Word2Vec) | Seq2Seq | NTM | LDA |
|--------|------------------------------|------------------------|---------|-----|-----|
| **Type** | Supervised | Unsupervised | Supervised | Unsupervised | Unsupervised |
| **Purpose** | Label sentences | Word embeddings | Seq-to-seq | Topic modeling | Topic modeling |
| **Output** | Class labels | Word vectors | Token sequence | Topics | Topics |
| **Instance** | C5/GPU | GPU | GPU only | GPU | CPU only |
| **Use Case** | Web search, info retrieval | NLP preprocessing | Translation | Document org | Document org |
| **Deep Learning** | Yes | Yes | Yes | Yes | No |

---

## Computer Vision Algorithm Comparison

| Aspect | Image Classification | Object Detection | Semantic Segmentation |
|--------|---------------------|------------------|----------------------|
| **Question Answered** | WHAT is in image? | WHAT and WHERE? | What is EACH PIXEL? |
| **Output** | Class labels | Bounding boxes + labels | Segmentation mask |
| **Use Case** | Photo tagging | Autonomous vehicles | Medical imaging |
| **Architecture** | CNN | CNN + SSD | FCN/PSP/DeepLabV3 |
| **Backbones** | MobileNet, ResNet, EfficientNet | VGG-16, ResNet-50 | ResNet50, ResNet101 |
| **Instance** | GPU | GPU | GPU |

---

## Anomaly Detection Comparison

| Aspect | Random Cut Forest | IP Insights |
|--------|-------------------|-------------|
| **Data Type** | Time series | Entity-IP pairs |
| **Learning** | Unsupervised | Unsupervised |
| **Output** | Anomaly score | Suspicious behavior flag |
| **Use Case** | Spikes, pattern breaks | Login anomalies, fraud |
| **Integration** | Kinesis Analytics | Security applications |
| **Instance** | CPU only | GPU recommended |
| **Input** | RecordIO/CSV | CSV only |

---

## Topic Modeling Comparison

| Aspect | Neural Topic Model (NTM) | LDA |
|--------|--------------------------|-----|
| **Approach** | Deep learning (neural variational inference) | Statistical (not deep learning) |
| **Instance** | GPU recommended | CPU only (single instance) |
| **Cost** | Higher (GPU) | Lower (CPU) |
| **Use Case** | Large-scale topic modeling | Budget-conscious, simpler needs |
| **Output** | Topic distributions | Topic distributions |
| **Metric** | Validation loss | Per-word log likelihood |

---

## Gradient Boosting Comparison

| Aspect | XGBoost | LightGBM |
|--------|---------|----------|
| **Type** | Boosted decision trees | Gradient boosting (GOSS, EFB) |
| **GPU Support** | Yes | No |
| **Instance Recommendation** | M5 (CPU) or P2/P3 (GPU) | M5 only |
| **Distributed Training** | Yes (GPU with XGBoost 1.5+) | Yes (CPU only) |
| **Memory** | Memory-bound | Memory-bound |
| **Input Formats** | CSV, libsvm, RecordIO, Parquet | txt/csv |
| **Serialization** | Pickle | - |

---

## Embeddings Algorithm Comparison

| Aspect | BlazingText (Word2Vec) | Object2Vec | Factorization Machines |
|--------|------------------------|------------|----------------------|
| **Scope** | Words only | Any objects | Pair-wise (user-item) |
| **Learning** | Unsupervised | Supervised | Supervised |
| **Data Type** | Text | Token pairs | Sparse matrices |
| **Use Case** | NLP preprocessing | Recommendations, similarity | Click prediction, recommendations |
| **Modes** | cbow, skipgram, batch_skipgram | - | - |
| **Instance** | GPU | Single machine | CPU recommended |

---

## Key Hyperparameters by Algorithm

### Overfitting Prevention

| Algorithm | Hyperparameters |
|-----------|----------------|
| XGBoost | `max_depth`, `subsample`, `eta`, `gamma`, `alpha`, `lambda` |
| Linear Learner | `L1`, `wd` (weight decay) |
| Neural networks | `dropout`, `early_stopping` |
| IP Insights | `vector_dim` (too large = overfit) |

### Class Imbalance

| Algorithm | Solution |
|-----------|----------|
| XGBoost | `scale_pos_weight` = sum(negative)/sum(positive) |
| Linear Learner | `balance_multiclass_weights` |

### Choosing K/Clusters

| Algorithm | Approach |
|-----------|----------|
| K-Means | Elbow method (plot within-cluster sum of squares) |
| KNN | Experiment with different K values |

---

## Exam-Ready Quick Reference

### "Which algorithm?" Decision Tree

```
Is it supervised?
├── Yes
│   ├── Tabular data?
│   │   ├── Yes → XGBoost, LightGBM, Linear Learner
│   │   └── No → Continue
│   ├── Images?
│   │   ├── Classification → Image Classification
│   │   ├── Location → Object Detection
│   │   └── Pixel-level → Semantic Segmentation
│   ├── Text?
│   │   ├── Classification → BlazingText
│   │   └── Sequence → Seq2Seq
│   ├── Time series? → DeepAR
│   └── Recommendations (sparse)? → Factorization Machines
│
└── No (Unsupervised)
    ├── Clustering? → K-Means
    ├── Dimensionality reduction? → PCA
    ├── Topic modeling?
    │   ├── GPU available → Neural Topic Model
    │   └── CPU only → LDA
    ├── Anomaly detection?
    │   ├── Time series → Random Cut Forest
    │   └── IP addresses → IP Insights
    └── Word embeddings? → BlazingText (Word2Vec)
```

### Instance Type Rules

| Rule | Algorithms |
|------|------------|
| **GPU required for training** | Seq2Seq, Object Detection |
| **CPU only** | LDA, Random Cut Forest |
| **Multi-GPU doesn't help** | Linear Learner |
| **Memory-bound (use M5)** | XGBoost, LightGBM |
| **GPU for large data** | BlazingText (>2GB) |
