# AWS MLE Exam - All Service Comparisons

> Consolidated comparison tables from all 13 sections for quick exam review.

---

## Table of Contents
1. [Storage Services](#storage-services)
2. [Data Ingestion & Streaming](#data-ingestion--streaming)
3. [Data Processing & ETL](#data-processing--etl)
4. [Feature Engineering](#feature-engineering)
5. [Managed AI Services](#managed-ai-services)
6. [SageMaker Training](#sagemaker-training)
7. [SageMaker Algorithms](#sagemaker-algorithms)
8. [Model Deployment](#model-deployment)
9. [Generative AI & Bedrock](#generative-ai--bedrock)
10. [MLOps & Pipelines](#mlops--pipelines)
11. [Security Services](#security-services)
12. [Monitoring & Governance](#monitoring--governance)
13. [Cost Optimization](#cost-optimization)

---

## Storage Services

### S3 Storage Classes

| Class | Access Pattern | Retrieval | Min Duration | Use Case |
|-------|---------------|-----------|--------------|----------|
| **Standard** | Frequent | Instant | None | Active ML data |
| **Intelligent-Tiering** | Unknown | Instant | None | Variable access patterns |
| **Standard-IA** | Infrequent | Instant | 30 days | Backups, older models |
| **One Zone-IA** | Infrequent | Instant | 30 days | Reproducible data |
| **Glacier Instant** | Rare | Milliseconds | 90 days | Archive with instant access |
| **Glacier Flexible** | Rare | Minutes-hours | 90 days | Compliance archives |
| **Glacier Deep Archive** | Rare | 12-48 hours | 180 days | Long-term archive |

### Storage for ML Workloads

| Need | Service | Why |
|------|---------|-----|
| Training data | **S3** | Scalable, integrates with SageMaker |
| Feature store | **SageMaker Feature Store** | Online + offline, consistency |
| Model artifacts | **S3** | Versioning, lifecycle policies |
| Notebook files | **EFS** | Shared across instances |
| High-performance training | **FSx for Lustre** | High throughput, S3 integration |
| HDFS workloads | **FSx for HDFS** | Hadoop compatible |

### EBS vs EFS vs FSx

| Aspect | EBS | EFS | FSx for Lustre |
|--------|-----|-----|----------------|
| **Type** | Block | File (NFS) | File (Lustre) |
| **Attachment** | Single EC2 | Multiple EC2 | Multiple EC2 |
| **Performance** | Very high | Scalable | Highest |
| **Use Case** | Boot volumes | Shared notebooks | HPC, training |
| **S3 Integration** | Manual | No | Native |

---

## Data Ingestion & Streaming

### Kinesis Family

| Service | Purpose | Latency | Use Case |
|---------|---------|---------|----------|
| **Data Streams** | Real-time streaming | ~200ms | Custom processing |
| **Data Firehose** | Managed delivery | 60s buffer | S3/Redshift loading |
| **Data Analytics** | SQL on streams | Seconds | Real-time analytics |
| **Video Streams** | Video ingestion | Real-time | Video ML |

### Kinesis vs SQS vs SNS

| Aspect | Kinesis Streams | SQS | SNS |
|--------|-----------------|-----|-----|
| **Pattern** | Streaming | Queue | Pub/Sub |
| **Ordering** | Per shard | FIFO only | No |
| **Retention** | 1-365 days | 14 days max | None |
| **Consumers** | Multiple | Single (per message) | Multiple |
| **Replay** | Yes | No | No |
| **Use Case** | Real-time ML | Decoupling | Fan-out |

### Batch vs Real-Time Ingestion

| Aspect | Batch | Real-Time |
|--------|-------|-----------|
| **Services** | S3, Glue, EMR | Kinesis, MSK |
| **Latency** | Minutes-hours | Milliseconds-seconds |
| **Volume** | High | Variable |
| **Processing** | Scheduled | Continuous |
| **Cost** | Lower | Higher |

---

## Data Processing & ETL

### ETL Service Selection

| Need | Service | Why |
|------|---------|-----|
| Serverless ETL | **AWS Glue** | No infrastructure |
| Big data processing | **EMR** | Hadoop/Spark ecosystem |
| Interactive prep | **Data Wrangler** | Visual, SageMaker integrated |
| SQL transforms | **Athena** | Query S3 directly |
| Streaming ETL | **Kinesis + Lambda** | Real-time |
| Simple transforms | **Lambda** | Event-driven, serverless |

### Glue vs EMR

| Aspect | Glue | EMR |
|--------|------|-----|
| **Management** | Serverless | Managed clusters |
| **Scaling** | Automatic | Manual/Auto |
| **Cost** | Pay per DPU-hour | Pay per instance-hour |
| **Flexibility** | Limited | Full Spark/Hadoop |
| **Best For** | ETL jobs | Complex processing |

### Data Wrangler vs Glue DataBrew

| Aspect | Data Wrangler | Glue DataBrew |
|--------|---------------|---------------|
| **Integration** | SageMaker Studio | Standalone |
| **Target User** | Data scientists | Data engineers |
| **Output** | Feature Store, S3 | S3, Glue catalog |
| **ML Focus** | High | Lower |

---

## Feature Engineering

### Feature Store Components

| Component | Purpose | Latency | Use Case |
|-----------|---------|---------|----------|
| **Online Store** | Real-time lookup | <10ms | Inference |
| **Offline Store** | Batch access | Minutes | Training |

### Encoding Methods

| Method | Input Type | Output | Use Case |
|--------|------------|--------|----------|
| **One-Hot** | Categorical | Binary vectors | Few categories |
| **Label Encoding** | Categorical | Integers | Ordinal data |
| **Target Encoding** | Categorical | Target mean | High cardinality |
| **Hashing** | Categorical | Fixed bins | Very high cardinality |

### Scaling Methods

| Method | Formula | Range | Use Case |
|--------|---------|-------|----------|
| **Normalization** | (x-min)/(max-min) | [0,1] | Neural networks |
| **Standardization** | (x-μ)/σ | ~[-3,3] | Linear models, SVM |
| **Robust Scaling** | (x-median)/IQR | Varies | Outlier-heavy data |

---

## Managed AI Services

### Vision Services

| Service | Purpose | Input |
|---------|---------|-------|
| **Rekognition** | Image/video analysis | Images, video |
| **Textract** | Document extraction | Documents, forms |
| **Lookout for Vision** | Anomaly detection | Industrial images |

### Language Services

| Service | Purpose | Input |
|---------|---------|-------|
| **Comprehend** | NLP analysis | Text |
| **Translate** | Translation | Text |
| **Transcribe** | Speech-to-text | Audio |
| **Polly** | Text-to-speech | Text |
| **Lex** | Chatbots | Text/voice |
| **Kendra** | Enterprise search | Documents |

### Forecasting & Recommendations

| Service | Purpose | Data Type |
|---------|---------|-----------|
| **Forecast** | Time series prediction | Time series |
| **Personalize** | Recommendations | User interactions |
| **Fraud Detector** | Fraud detection | Transactions |

### When to Use Managed vs Custom

| Scenario | Choice |
|----------|--------|
| Standard use case (sentiment, OCR) | **Managed AI Service** |
| Custom domain/labels | **Custom model** |
| Quick prototype | **Managed AI Service** |
| Full control needed | **SageMaker** |
| Edge deployment | **Custom + Neo** |

---

## SageMaker Training

### Training Instance Selection

| Workload | Instance Family | Examples |
|----------|-----------------|----------|
| Traditional ML | CPU | ml.m5, ml.c5 |
| Deep Learning | GPU | ml.p3, ml.p4d, ml.g4dn |
| Cost-effective DL | AWS Silicon | ml.trn1 (Trainium) |
| Memory-intensive | High memory | ml.r5 |

### Distributed Training Strategies

| Strategy | Data | Model | Use Case |
|----------|------|-------|----------|
| **Data Parallel** | Split | Replicated | Large datasets |
| **Model Parallel** | Replicated | Split | Large models |
| **Hybrid** | Split | Split | Very large models |

### Managed Spot Training

| Aspect | Detail |
|--------|--------|
| **Savings** | Up to 90% |
| **Risk** | Interruption |
| **Mitigation** | Checkpointing |
| **Best For** | Fault-tolerant, flexible |

### HPO Strategies

| Strategy | Efficiency | Best For |
|----------|------------|----------|
| **Bayesian** | High | Default choice |
| **Hyperband** | High | Early stopping beneficial |
| **Random** | Low | Simple problems |
| **Grid** | Very Low | Avoid |

---

## SageMaker Algorithms

### Supervised Learning - Regression

| Algorithm | Type | Use Case | Mode |
|-----------|------|----------|------|
| **Linear Learner** | Linear | Simple regression | Built-in |
| **XGBoost** | Tree ensemble | Tabular data | Built-in |
| **KNN** | Instance-based | Small datasets | Built-in |

### Supervised Learning - Classification

| Algorithm | Type | Use Case | Mode |
|-----------|------|----------|------|
| **Linear Learner** | Linear | Binary/multi-class | Built-in |
| **XGBoost** | Tree ensemble | Tabular data | Built-in |
| **Image Classification** | CNN | Image labels | Built-in |
| **Object Detection** | CNN | Bounding boxes | Built-in |

### Unsupervised Learning

| Algorithm | Purpose | Output |
|-----------|---------|--------|
| **K-Means** | Clustering | Cluster assignments |
| **PCA** | Dimensionality reduction | Principal components |
| **Random Cut Forest** | Anomaly detection | Anomaly scores |
| **IP Insights** | IP anomaly detection | Risk scores |

### NLP Algorithms

| Algorithm | Purpose | Output |
|-----------|---------|--------|
| **BlazingText** | Text classification, Word2Vec | Classes, embeddings |
| **Sequence-to-Sequence** | Translation, summarization | Text |
| **Object2Vec** | Embeddings for pairs | Similarity scores |
| **LDA** | Topic modeling | Topic distributions |
| **NTM** | Topic modeling | Topic distributions |

### Time Series

| Algorithm | Purpose | Use Case |
|-----------|---------|----------|
| **DeepAR** | Forecasting | Multiple related series |

### Algorithm Selection Quick Guide

| Data Type | Problem | Algorithm |
|-----------|---------|-----------|
| Tabular | Classification/Regression | **XGBoost** |
| Tabular | Simple linear | **Linear Learner** |
| Images | Classification | **Image Classification** |
| Images | Detection | **Object Detection** |
| Text | Classification | **BlazingText** |
| Text | Translation | **Seq2Seq** |
| Time series | Forecasting | **DeepAR** |
| Any | Clustering | **K-Means** |
| Any | Anomaly | **Random Cut Forest** |
| Any | Dim reduction | **PCA** |

---

## Model Deployment

### Endpoint Types

| Type | Latency | Cost | Best For |
|------|---------|------|----------|
| **Real-time** | Low (ms) | Always-on | Production APIs |
| **Serverless** | Variable | Pay per request | Variable traffic |
| **Asynchronous** | Minutes | Queue-based | Long inference |
| **Batch Transform** | Hours | Per job | Large datasets |

### Multi-Model vs Multi-Container

| Aspect | Multi-Model Endpoint | Multi-Container |
|--------|---------------------|-----------------|
| **Models** | Many (same framework) | Few (different frameworks) |
| **Loading** | Dynamic | All loaded |
| **Memory** | Shared | Dedicated per container |
| **Use Case** | Many similar models | Different model types |

### Deployment Strategies

| Strategy | Traffic Shift | Rollback | Best For |
|----------|---------------|----------|----------|
| **Blue/Green** | Instant 100% | Instant | Quick cutover |
| **Canary** | Small % first | Fast | Risk mitigation |
| **Linear** | Gradual % | Moderate | Controlled rollout |
| **A/B Testing** | Split | N/A | Model comparison |

### Inference Hardware

| Instance | Chip | Best For |
|----------|------|----------|
| **inf1/inf2** | Inferentia | DL inference (cost-effective) |
| **g4dn** | NVIDIA GPU | GPU inference |
| **Graviton3** | ARM | CPU inference (cost-effective) |
| **ml.c5** | Intel | CPU inference |

---

## Generative AI & Bedrock

### Foundation Model Providers in Bedrock

| Provider | Models | Specialty |
|----------|--------|-----------|
| **Anthropic** | Claude | Reasoning, safety |
| **Amazon** | Titan | General purpose, embeddings |
| **AI21 Labs** | Jurassic | Text generation |
| **Cohere** | Command | Enterprise text |
| **Meta** | Llama | Open weights |
| **Stability AI** | Stable Diffusion | Image generation |

### Bedrock vs SageMaker JumpStart

| Aspect | Bedrock | JumpStart |
|--------|---------|-----------|
| **Type** | Managed API | Deploy to endpoint |
| **Customization** | Fine-tuning, RAG | Full control |
| **Infrastructure** | None | Managed by you |
| **Cost** | Per token | Per instance |
| **Best For** | Quick integration | Custom deployment |

### RAG vs Fine-Tuning

| Aspect | RAG | Fine-Tuning |
|--------|-----|-------------|
| **Data Updates** | Real-time | Requires retraining |
| **Cost** | Lower | Higher |
| **Customization** | Limited | Deep |
| **Use Case** | Current data, Q&A | Style, domain expertise |

### Knowledge Bases vs Agents

| Feature | Knowledge Bases | Agents |
|---------|-----------------|--------|
| **Purpose** | RAG/retrieval | Task execution |
| **Data Source** | Vector DB | APIs, tools |
| **Output** | Answers | Actions |

---

## MLOps & Pipelines

### CI/CD Tools for ML

| Tool | Purpose | Scope |
|------|---------|-------|
| **SageMaker Pipelines** | ML workflow orchestration | Training to deployment |
| **CodePipeline** | General CI/CD | Code to deployment |
| **CodeBuild** | Build/test | Compilation, testing |
| **CodeCommit** | Source control | Git repository |
| **Step Functions** | Workflow orchestration | Any AWS service |

### Model Registry Features

| Feature | Purpose |
|---------|---------|
| **Model Groups** | Organize model versions |
| **Approval Status** | Gate deployments |
| **Lineage** | Track data/code origins |
| **Metadata** | Store model info |

### Pipeline Orchestration Comparison

| Service | Best For | Integration |
|---------|----------|-------------|
| **SageMaker Pipelines** | ML-specific workflows | Native SageMaker |
| **Step Functions** | Complex branching | All AWS services |
| **MWAA (Airflow)** | Existing Airflow users | Open source |
| **EventBridge** | Event-driven triggers | All AWS services |

---

## Security Services

### The Big Three: IAM vs KMS vs Secrets Manager

| Service | Purpose | Protects |
|---------|---------|----------|
| **IAM** | Access control | Who can do what |
| **KMS** | Encryption keys | Data at rest/transit |
| **Secrets Manager** | Secret storage | Credentials, API keys |

### Encryption Options

| Aspect | SSE-S3 | SSE-KMS | SSE-C |
|--------|--------|---------|-------|
| **Key Management** | AWS | AWS KMS | Customer |
| **Audit Trail** | No | CloudTrail | No |
| **Rotation** | Auto | Configurable | Manual |
| **Use Case** | Default | Compliance | Full control |

### Network Security

| Service | Purpose | Use Case |
|---------|---------|----------|
| **VPC** | Network isolation | Private resources |
| **Security Groups** | Instance firewall | Allow rules |
| **NACLs** | Subnet firewall | Allow/Deny rules |
| **PrivateLink** | Private connectivity | No internet exposure |
| **VPC Endpoints** | Private AWS access | Keep traffic in VPC |

### SageMaker Security Features

| Feature | Purpose |
|---------|---------|
| **Network Isolation** | No internet access |
| **Inter-container Encryption** | Protect distributed training |
| **VPC Config** | Private deployment |
| **IAM Roles** | Execution permissions |

---

## Monitoring & Governance

### CloudWatch vs CloudTrail vs Config

| Aspect | CloudWatch | CloudTrail | Config |
|--------|------------|------------|--------|
| **Purpose** | Performance | Audit | Compliance |
| **Answers** | "How is it performing?" | "Who did what?" | "Is it configured right?" |
| **Data** | Metrics, logs | API calls | Configurations |

### SageMaker Monitoring Tools

| Tool | Monitors | Use Case |
|------|----------|----------|
| **Model Monitor** | Data quality, drift, bias | Production models |
| **Clarify** | Bias, explainability | Pre/post training |
| **Debugger** | Training issues | During training |
| **Profiler** | Resource utilization | Training optimization |

### Model Monitor Types

| Type | Detects | Baseline |
|------|---------|----------|
| **Data Quality** | Schema, missing values | Training data |
| **Model Quality** | Accuracy degradation | Ground truth |
| **Bias Drift** | Fairness changes | Pre-training analysis |
| **Feature Attribution** | Feature importance changes | SHAP values |

### Responsible AI Tools

| Tool | Purpose |
|------|---------|
| **Clarify** | Bias detection, explainability |
| **Model Monitor** | Drift detection |
| **A2I** | Human-in-the-loop review |
| **Model Cards** | Model documentation |

---

## Cost Optimization

### Training Cost Optimization

| Strategy | Savings | Risk |
|----------|---------|------|
| **Spot Instances** | Up to 90% | Interruption |
| **Warm-start HPO** | Variable | None |
| **Right-sizing** | Variable | None |
| **Early stopping** | Variable | None |

### Inference Cost Optimization

| Strategy | Best For | Tool |
|----------|----------|------|
| **Serverless** | Variable traffic | Serverless Inference |
| **Auto-scaling** | Predictable patterns | SageMaker AutoScaling |
| **Right-sizing** | All | Inference Recommender |
| **Spot (batch)** | Fault-tolerant batch | Batch Transform |

### Instance Cost Comparison (Relative)

| Type | Cost | Performance | Use Case |
|------|------|-------------|----------|
| **On-Demand** | $$$ | Guaranteed | Production |
| **Spot** | $ | Interruptible | Training |
| **Reserved** | $$ | Guaranteed | Steady workloads |
| **Savings Plans** | $$ | Flexible | Variable workloads |

---

## Quick Decision Tables

### "Which Service?" - Common Exam Patterns

| Need | Answer |
|------|--------|
| Store training data | **S3** |
| Stream real-time data | **Kinesis Data Streams** |
| Serverless ETL | **AWS Glue** |
| Interactive data prep | **Data Wrangler** |
| Detect faces in images | **Rekognition** |
| Extract text from documents | **Textract** |
| Sentiment analysis | **Comprehend** |
| Time series forecasting | **Forecast** or **DeepAR** |
| Recommendations | **Personalize** |
| Tabular classification | **XGBoost** |
| Image classification | **Image Classification** algo |
| Text classification | **BlazingText** |
| Anomaly detection | **Random Cut Forest** |
| Real-time inference | **SageMaker Endpoint** |
| Batch inference | **Batch Transform** |
| Variable traffic inference | **Serverless Inference** |
| Foundation models | **Bedrock** |
| ML workflow orchestration | **SageMaker Pipelines** |
| Model versioning | **Model Registry** |
| Bias detection | **Clarify** |
| Production monitoring | **Model Monitor** |
| Encryption keys | **KMS** |
| Store credentials | **Secrets Manager** |
| API auditing | **CloudTrail** |
| Performance metrics | **CloudWatch** |
| Configuration compliance | **AWS Config** |

### Instance Type Selection

| Workload | Instance |
|----------|----------|
| Traditional ML training | **ml.m5** (CPU) |
| Deep learning training | **ml.p4d** (NVIDIA GPU) |
| Cost-effective DL training | **ml.trn1** (Trainium) |
| Deep learning inference | **ml.inf2** (Inferentia) |
| CPU inference | **ml.c5** or Graviton |
| High memory | **ml.r5** |

---

## Anti-Patterns to Avoid

| Wrong Choice | Right Choice | Why |
|--------------|--------------|-----|
| EC2 for ML training | SageMaker | Managed, scalable |
| S3 for real-time features | Feature Store Online | Latency |
| Real-time endpoint for batch | Batch Transform | Cost |
| Grid search for HPO | Bayesian/Hyperband | Efficiency |
| Training without checkpoints on Spot | Enable checkpointing | Data loss risk |
| Public endpoints for sensitive data | VPC + PrivateLink | Security |
| Manual scaling | Auto-scaling | Efficiency |
| Single AZ for production | Multi-AZ | Availability |
