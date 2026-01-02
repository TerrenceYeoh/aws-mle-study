# Section 5: SageMaker Built-In Algorithms

## Overview

SageMaker provides a comprehensive suite of built-in ML algorithms optimized for AWS infrastructure. These algorithms handle the entire ML workflow: data preparation, training, and deployment.

**Key Takeaways:**
- Choose algorithms based on problem type (supervised/unsupervised) and data characteristics
- Input formats matter: RecordIO-protobuf is often fastest, CSV is most flexible
- Instance type selection (CPU vs GPU) varies significantly by algorithm
- Many algorithms support distributed training across multiple instances

---

## SageMaker Architecture

```
S3 Training Data → Model Training ← Training Code Image (ECR)
                        ↓
                S3 Model Artifacts
                        ↓
            Model Deployment/Hosting ← Inference Code Image (ECR)
                        ↓
                    Endpoint
                        ↓
                   Client App
```

### Input Modes

| Mode | Description | Best For |
|------|-------------|----------|
| **S3 File Mode** | Default; copies data locally | General use |
| **S3 Fast File Mode** | Streams data, starts immediately | Large datasets |
| **Pipe Mode** | Legacy streaming | Replaced by Fast File |
| **FSx for Lustre** | 100s GB/s, millions IOPS | High performance (requires VPC) |
| **Amazon EFS** | Shared file system | Data already in EFS |

---

## Algorithm Quick Reference

### Regression/Classification Algorithms

#### Linear Learner
- **Type:** Supervised
- **Use Cases:** Linear regression, binary/multi-class classification
- **Input:** RecordIO-protobuf (Float32) or CSV
- **Key Features:**
  - Automatic normalization
  - Multiple models trained in parallel
  - L1/L2 regularization
- **Instance:** CPU or GPU (multi-GPU doesn't help)
- **Key Hyperparameters:** `learning_rate`, `mini_batch_size`, `L1`, `wd`, `target_precision`, `target_recall`

#### XGBoost
- **Type:** Supervised (boosted decision trees)
- **Use Cases:** Classification, regression
- **Input:** CSV, libsvm, RecordIO-protobuf, Parquet
- **Key Features:**
  - Very popular (Kaggle competitions)
  - Gradient descent to minimize loss
  - Memory-bound (not compute-bound)
- **Instance:** M5 for CPU, P2/P3/G4dn/G5 for GPU
- **Key Hyperparameters:** `max_depth`, `eta`, `subsample`, `gamma`, `alpha`, `lambda`, `scale_pos_weight`
- **GPU Setup:** Set `tree_method=gpu_hist`

#### LightGBM
- **Type:** Supervised (gradient boosting)
- **Use Cases:** Classification, regression, ranking
- **Input:** txt/csv
- **Key Features:**
  - Uses GOSS and EFB techniques
  - Similar to CatBoost
  - Memory-bound
- **Instance:** CPU only (M5 recommended, not C5)
- **Key Hyperparameters:** `learning_rate`, `num_leaves`, `feature_fraction`, `max_depth`

#### KNN (K-Nearest-Neighbors)
- **Type:** Supervised/Unsupervised
- **Use Cases:** Simple classification or regression
- **Input:** RecordIO-protobuf or CSV (first column = label)
- **Key Features:**
  - Built-in dimensionality reduction ("sign" or "fjlt" methods)
  - Addresses "curse of dimensionality"
- **Instance:** CPU or GPU
- **Inference:** CPU for latency, GPU for throughput
- **Key Hyperparameters:** `k`, `sample_size`

---

### Clustering Algorithms

#### K-Means
- **Type:** Unsupervised
- **Use Cases:** Divide data into K groups by similarity
- **Input:** RecordIO-protobuf or CSV
- **Key Features:**
  - Uses k-means++ for initialization
  - Extra cluster centers for accuracy
  - Measured by Euclidean distance
- **Instance:** CPU recommended (GPU uses only 1 GPU)
- **Key Hyperparameters:** `k` (use elbow method), `mini_batch_size`, `init_method`

---

### Dimensionality Reduction

#### PCA (Principal Component Analysis)
- **Type:** Unsupervised
- **Use Cases:** Reduce features while preserving variance
- **Input:** RecordIO-protobuf or CSV
- **Key Features:**
  - SVD-based
  - **Regular mode:** sparse data, moderate size
  - **Randomized mode:** large datasets
- **Instance:** CPU or GPU (data-dependent)
- **Key Hyperparameters:** `algorithm_mode`, `subtract_mean`

---

### Time Series

#### DeepAR
- **Type:** Supervised (RNN-based)
- **Use Cases:** Forecasting 1D time series
- **Input:** JSON lines (Gzip/Parquet)
- **Key Features:**
  - Train on multiple related time series
  - Finds frequencies and seasonality
  - Fields: `start`, `target`, optional `dynamic_feat`, `cat`
- **Instance:** Start CPU, move to GPU if mini_batch_size > 512
- **Inference:** CPU only
- **Key Hyperparameters:** `context_length`, `epochs`, `num_cells`
- **Best Practice:** `prediction_length` ≤ 400

---

### NLP Algorithms

#### Seq2Seq (Sequence to Sequence)
- **Type:** Supervised (RNN/CNN with attention)
- **Use Cases:** Translation, summarization, speech-to-text
- **Input:** RecordIO-protobuf (**integers**, not floats)
- **Key Features:**
  - Training can take days
  - Pre-trained models available
- **Instance:** GPU only, single machine
- **Metrics:** Accuracy, BLEU score, Perplexity
- **Key Hyperparameters:** `batch_size`, `optimizer_type`, `num_layers_encoder/decoder`

#### BlazingText
- **Type:** Supervised (text classification) or Unsupervised (Word2Vec)
- **Use Cases:**
  - Text classification (predict labels)
  - Word embeddings (semantic similarity)
- **Input:**
  - Classification: `__label__X text...` format
  - Word2Vec: one sentence per line
- **Instance:**
  - Word2Vec: ml.p3.2xlarge
  - Classification <2GB: C5
  - Classification >2GB: GPU
- **Word2Vec Modes:** cbow, skipgram, batch_skipgram
- **Key Hyperparameters:** `mode`, `learning_rate`, `vector_dim`, `word_ngrams`

#### Neural Topic Model (NTM)
- **Type:** Unsupervised (neural variational inference)
- **Use Cases:** Organize documents into topics
- **Input:** RecordIO-protobuf or CSV (words tokenized to integers)
- **Instance:** GPU recommended for training, CPU for inference
- **Key Hyperparameters:** `num_topics`, `mini_batch_size`, `learning_rate`

#### LDA (Latent Dirichlet Allocation)
- **Type:** Unsupervised (NOT deep learning)
- **Use Cases:** Topic modeling (similar to NTM)
- **Input:** RecordIO-protobuf or CSV
- **Instance:** Single-instance CPU only
- **Key Hyperparameters:** `num_topics`, `alpha0`
- **Difference from NTM:** CPU-based, potentially cheaper

---

### Computer Vision

#### Object Detection
- **Type:** Supervised (CNN + SSD)
- **Use Cases:** Identify objects with bounding boxes
- **Input:** RecordIO or images with JSON annotations
- **Variants:**
  - MXNet: VGG-16, ResNet-50
  - TensorFlow: ResNet, EfficientNet, MobileNet
- **Instance:** GPU required (multi-GPU/multi-machine OK)
- **Key Hyperparameters:** `mini_batch_size`, `learning_rate`, `optimizer`

#### Image Classification
- **Type:** Supervised
- **Use Cases:** Assign labels to images (NOT location)
- **Input:** Images (default 224x224)
- **Key Features:**
  - Transfer learning from ImageNet
  - MXNet or TensorFlow variants
- **Instance:** GPU (multi-GPU/multi-machine OK)
- **Key Hyperparameters:** `batch_size`, `learning_rate`, `optimizer`

#### Semantic Segmentation
- **Type:** Supervised
- **Use Cases:** Pixel-level classification
- **Input:** JPG images + PNG annotations
- **Algorithms:** FCN, PSP, DeepLabV3
- **Backbones:** ResNet50, ResNet101
- **Instance:** GPU (multi-GPU/multi-machine OK)
- **Key Hyperparameters:** `algorithm`, `backbone`, `epochs`

---

### Anomaly Detection

#### Random Cut Forest (RCF)
- **Type:** Unsupervised (Amazon-developed)
- **Use Cases:** Anomaly detection in time series
- **Input:** RecordIO-protobuf or CSV
- **Key Features:**
  - Assigns anomaly score to each point
  - Available in Kinesis Analytics
- **Instance:** CPU only (M4, C4, C5)
- **Key Hyperparameters:** `num_trees`, `num_samples_per_tree`

#### IP Insights
- **Type:** Unsupervised
- **Use Cases:** Detect suspicious IP behavior
- **Input:** CSV only (Entity, IP)
- **Key Features:**
  - Neural network learns latent vectors
  - Auto-generates negative samples
- **Instance:** GPU recommended (ml.p3.2xlarge)
- **Key Hyperparameters:** `num_entity_vectors` (2x unique entities), `vector_dim`

---

### Embeddings & Recommendations

#### Object2Vec
- **Type:** Supervised
- **Use Cases:** Create embeddings of arbitrary objects
- **Input:** JSON lines (tokenized integer pairs)
- **Key Features:**
  - Generalized Word2Vec
  - Encoder options: pooled embeddings, CNN, BiLSTM
- **Instance:** Single machine only (CPU or GPU)
- **Key Hyperparameters:** `enc1_network`, `enc2_network`, `dropout`

#### Factorization Machines
- **Type:** Supervised
- **Use Cases:** Recommendations with sparse data
- **Input:** RecordIO-protobuf (Float32 only)
- **Key Features:**
  - Pair-wise interactions (user→item)
  - Click prediction, item recommendations
- **Instance:** CPU recommended (GPU only for dense data)
- **Key Hyperparameters:** Initialization methods (uniform, normal, constant)

---

## Concept Relationships

```
┌─────────────────────────────────────────────────────────────────────┐
│                     SAGEMAKER BUILT-IN ALGORITHMS                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  SUPERVISED                    UNSUPERVISED                         │
│  ──────────                    ────────────                         │
│  ┌──────────────┐              ┌──────────────┐                     │
│  │ Regression/  │              │ Clustering   │                     │
│  │ Classification│             │ • K-Means    │                     │
│  │ • Linear     │              └──────────────┘                     │
│  │   Learner    │                                                   │
│  │ • XGBoost    │              ┌──────────────┐                     │
│  │ • LightGBM   │              │ Dim Reduction│                     │
│  │ • KNN        │              │ • PCA        │                     │
│  └──────────────┘              └──────────────┘                     │
│                                                                     │
│  ┌──────────────┐              ┌──────────────┐                     │
│  │ NLP          │              │ Topic Model  │                     │
│  │ • Seq2Seq    │              │ • NTM        │                     │
│  │ • BlazingText│◄────────────►│ • LDA        │                     │
│  └──────────────┘              └──────────────┘                     │
│                                                                     │
│  ┌──────────────┐              ┌──────────────┐                     │
│  │ Vision       │              │ Anomaly      │                     │
│  │ • Object Det │              │ • RCF        │                     │
│  │ • Image Class│              │ • IP Insights│                     │
│  │ • Semantic   │              └──────────────┘                     │
│  │   Segment    │                                                   │
│  └──────────────┘                                                   │
│                                                                     │
│  ┌──────────────┐              ┌──────────────┐                     │
│  │ Time Series  │              │ Embeddings   │                     │
│  │ • DeepAR     │              │ • Object2Vec │                     │
│  └──────────────┘              │ • Factor Mach│                     │
│                                └──────────────┘                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Exam Tips

### Algorithm Selection
- **Sparse data + recommendations** → Factorization Machines
- **Time series forecasting** → DeepAR
- **Anomaly detection in time series** → Random Cut Forest
- **Anomaly detection with IPs** → IP Insights
- **Topic modeling (GPU)** → Neural Topic Model
- **Topic modeling (CPU, cheaper)** → LDA
- **Word embeddings** → BlazingText (Word2Vec mode)
- **Text classification** → BlazingText (supervised mode)
- **Pixel-level image classification** → Semantic Segmentation
- **Object location in images** → Object Detection
- **Simple classification/regression** → Linear Learner or XGBoost

### Instance Type Patterns
- **GPU Required:** Seq2Seq, Object Detection (training)
- **CPU Only:** LDA, Random Cut Forest
- **GPU Recommended:** IP Insights, Neural Topic Model (training)
- **Memory-bound (use M5):** XGBoost, LightGBM
- **Multi-GPU doesn't help:** Linear Learner

### Input Format Patterns
- **RecordIO-protobuf preferred:** Most algorithms (faster)
- **CSV only:** IP Insights
- **Integers required:** Seq2Seq (tokens must be integers)
- **RecordIO only (no CSV):** Factorization Machines (sparse data)
- **JSON lines:** DeepAR, Object2Vec

### Key Hyperparameter Patterns
- **Overfitting prevention:** `max_depth`, `subsample`, `alpha`, `lambda` (XGBoost)
- **Unbalanced classes:** `scale_pos_weight` (XGBoost), `balance_multiclass_weights` (Linear Learner)
- **Choose K:** Use "elbow method" for K-Means

---

## Related Sections
- [[02-data-ingestion/02-data-ingestion]] - S3, data storage
- [[03-data-transformation/03-data-transformation]] - Feature engineering, data prep
- [[06-model-training/06-model-training]] - Training infrastructure, hyperparameter tuning
- [[09-mlops/09-mlops]] - Model deployment, endpoints
