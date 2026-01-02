# AWS MLE Exam - Quick Reference Card

> Last-minute review guide for AWS Certified Machine Learning Engineer - Associate (MLA-C01)

---

## Exam Facts
- **65 questions** | **170 minutes** | **$300** | Pass: **720/1000**
- Question types: Multiple choice, Multiple response, **Ordering**, **Matching**, **Case Study**
- **No partial credit** for ordering/matching questions

---

## Domain Weights

| Domain | Weight | Focus Areas |
|--------|--------|-------------|
| **1. Data Preparation** | 28% | Ingestion, storage, transformation, Feature Store |
| **2. Model Development** | 26% | Algorithms, training, tuning, evaluation |
| **3. Deployment** | 22% | Endpoints, inference, scaling, edge |
| **4. Monitoring & Security** | 24% | Model Monitor, Clarify, IAM, KMS |

---

## Must-Know Formulas

```
Precision = TP / (TP + FP)     → "Of predicted +, how many correct?"
Recall    = TP / (TP + FN)     → "Of actual +, how many found?"
F1 Score  = 2(P×R) / (P+R)     → Harmonic mean

Confusion Matrix:
              Predicted
            Pos    Neg
Actual Pos  TP     FN
       Neg  FP     TN
```

**When to Prioritize:**
- **Precision** → False positives costly (spam, fraud alerts)
- **Recall** → False negatives costly (disease, security threats)

---

## Key AWS Services Cheat Sheet

### Data Ingestion
| Service | Use When |
|---------|----------|
| **Kinesis Streams** | Real-time streaming, multiple consumers |
| **Kinesis Firehose** | Load to S3/Redshift/OpenSearch |
| **SQS** | Decoupling, exactly-once processing |
| **SNS** | Fan-out notifications |

### Data Processing
| Service | Use When |
|---------|----------|
| **Glue** | Serverless ETL, data catalog |
| **EMR** | Big data, Spark/Hadoop |
| **Data Wrangler** | Visual data prep in SageMaker |
| **Athena** | Query S3 with SQL |

### Storage
| Service | Use When |
|---------|----------|
| **S3** | Training data, model artifacts |
| **Feature Store** | Feature consistency train/inference |
| **FSx Lustre** | High-performance training |
| **EFS** | Shared notebook storage |

### Managed AI
| Service | Use When |
|---------|----------|
| **Rekognition** | Images/video analysis |
| **Textract** | Document/form extraction |
| **Comprehend** | NLP, sentiment, PII detection |
| **Transcribe** | Speech-to-text |
| **Polly** | Text-to-speech |
| **Forecast** | Time series (managed) |
| **Personalize** | Recommendations |

### SageMaker Algorithms
| Algorithm | Use When |
|-----------|----------|
| **XGBoost** | Tabular data (default choice) |
| **Linear Learner** | Simple linear problems |
| **BlazingText** | Text classification, Word2Vec |
| **Image Classification** | Classify images |
| **Object Detection** | Bounding boxes |
| **DeepAR** | Time series forecasting |
| **K-Means** | Clustering |
| **Random Cut Forest** | Anomaly detection |
| **PCA** | Dimensionality reduction |

### Deployment
| Type | Use When |
|------|----------|
| **Real-time Endpoint** | Low latency, production |
| **Serverless Inference** | Variable/unpredictable traffic |
| **Async Inference** | Long-running predictions |
| **Batch Transform** | Large datasets, offline |
| **Multi-Model Endpoint** | Many similar models |
| **Neo + Greengrass** | Edge deployment |

### Generative AI
| Service | Use When |
|---------|----------|
| **Bedrock** | Foundation models as API |
| **JumpStart** | Deploy FMs to endpoint |
| **Knowledge Bases** | RAG applications |
| **Agents** | Task execution with tools |

### MLOps
| Service | Use When |
|---------|----------|
| **Pipelines** | ML workflow orchestration |
| **Model Registry** | Version and approve models |
| **Experiments** | Track training runs |
| **Step Functions** | Complex workflow branching |

### Security
| Service | Use When |
|---------|----------|
| **IAM** | Access control |
| **KMS** | Encryption keys |
| **Secrets Manager** | Store credentials |
| **VPC** | Network isolation |
| **PrivateLink** | Private AWS connectivity |

### Monitoring
| Service | Use When |
|---------|----------|
| **Model Monitor** | Data drift, model quality |
| **Clarify** | Bias, explainability |
| **CloudWatch** | Metrics, logs, alarms |
| **CloudTrail** | API auditing |
| **Config** | Configuration compliance |

---

## SageMaker Instance Types

| Prefix | Chip | Use Case |
|--------|------|----------|
| **ml.m5** | CPU | General ML |
| **ml.c5** | CPU | Compute-intensive |
| **ml.p3/p4d** | NVIDIA GPU | DL training |
| **ml.g4dn** | NVIDIA GPU | GPU inference |
| **ml.trn1** | Trainium | Cost-effective training |
| **ml.inf1/inf2** | Inferentia | Cost-effective inference |

---

## Training Optimization

| Technique | Benefit |
|-----------|---------|
| **Spot Instances** | Up to 90% savings |
| **Checkpointing** | Resume interrupted training |
| **Bayesian HPO** | Efficient hyperparameter search |
| **Early Stopping** | Avoid overtraining |
| **Distributed Training** | Scale to large models/data |
| **Training Compiler** | Faster training |

---

## Regularization Techniques

| Technique | Effect |
|-----------|--------|
| **L1 (Lasso)** | Feature selection (sparse) |
| **L2 (Ridge)** | Weight shrinkage |
| **Dropout** | Random neuron deactivation |
| **Early Stopping** | Stop at optimal point |
| **Data Augmentation** | More training examples |

---

## Deployment Strategies

| Strategy | Use When |
|----------|----------|
| **Blue/Green** | Quick full cutover |
| **Canary** | Risk mitigation (test small %) |
| **Linear** | Gradual controlled rollout |
| **A/B Testing** | Compare model versions |

---

## Model Monitor Types

| Type | Detects |
|------|---------|
| **Data Quality** | Schema changes, missing values |
| **Model Quality** | Accuracy degradation |
| **Bias Drift** | Fairness metric changes |
| **Feature Attribution** | Feature importance drift |

---

## Responsible AI (8 Dimensions)

1. **Fairness** → Clarify
2. **Explainability** → Clarify (SHAP)
3. **Privacy & Security** → KMS, IAM, Macie
4. **Safety** → Model Monitor
5. **Controllability** → A2I (human-in-the-loop)
6. **Veracity & Robustness** → Model Monitor
7. **Governance** → Model Cards, Model Registry
8. **Transparency** → Model Cards

---

## ML Lifecycle

```
Business Goal → Problem Framing → Data Processing →
Model Development → Deployment → Monitoring
         ↑___________________________________|
                    Feedback Loop
```

---

## Common Exam Signals

| Keyword | Think... |
|---------|----------|
| "Cost-effective" | Spot, Serverless, right-sizing |
| "Fastest" | Provisioned, parallelization |
| "Scalable" | Managed services, auto-scaling |
| "Secure" | KMS, VPC, IAM, encryption |
| "Real-time" | Kinesis, real-time endpoints |
| "Batch" | Batch Transform, Glue |
| "Minimal ops" | Managed/serverless |
| "Variable traffic" | Serverless Inference |
| "Edge" | Neo + Greengrass |

---

## Anti-Patterns (Wrong Answers)

| If You See... | It's Probably Wrong Because... |
|---------------|--------------------------------|
| EC2 for ML training | Use SageMaker (managed) |
| S3 for real-time lookups | Use Feature Store Online |
| Grid search | Use Bayesian/Hyperband |
| Real-time endpoint for batch | Use Batch Transform |
| Single AZ production | Need Multi-AZ |
| Public endpoints for ML | Use VPC + PrivateLink |

---

## Quick S3 Storage Class Guide

| Need | Class |
|------|-------|
| Frequent access | **Standard** |
| Unknown pattern | **Intelligent-Tiering** |
| Infrequent, fast retrieval | **Standard-IA** |
| Archive, instant access | **Glacier Instant** |
| Archive, hours OK | **Glacier Flexible** |
| Long-term archive | **Glacier Deep Archive** |

---

## Kinesis Shards Math

- **Write**: 1 MB/sec or 1000 records/sec per shard
- **Read**: 2 MB/sec per shard
- More throughput → More shards

---

## Feature Store Key Points

- **Online**: Low-latency inference (<10ms)
- **Offline**: Batch training (S3-based)
- **Feature Groups**: Organize features
- **Point-in-time**: Prevent data leakage
- **Consistency**: Same features train/inference

---

## Encryption Quick Reference

| Type | Service | Key Management |
|------|---------|----------------|
| **SSE-S3** | S3 | AWS managed |
| **SSE-KMS** | S3 | Customer KMS |
| **SSE-C** | S3 | Customer provided |
| **Inter-container** | SageMaker | Distributed training |
| **In-transit** | All | TLS |

---

## CloudWatch vs CloudTrail vs Config

| Question | Answer |
|----------|--------|
| "How is it performing?" | **CloudWatch** |
| "Who did what?" | **CloudTrail** |
| "Is it configured right?" | **Config** |

---

## Last-Minute Reminders

1. **XGBoost** is usually right for tabular data
2. **Bayesian HPO** > Random/Grid search
3. **Spot + Checkpointing** for cost-effective training
4. **Feature Store** ensures train/inference consistency
5. **Model Monitor** catches drift in production
6. **Clarify** for bias and explainability
7. **Serverless Inference** for variable traffic
8. **VPC + PrivateLink** for security
9. **KMS** for encryption key management
10. **SageMaker Pipelines** for ML workflow orchestration

---

## Test Strategy

1. **Read carefully** - especially for ordering/matching
2. **Pace**: 2-2.5 min/question
3. **Flag and move on** if stuck >3 min
4. **Process of elimination** - often 2 answers are clearly wrong
5. **Review flagged** questions at end
6. **Don't change** answers without good reason
7. **You don't need 100%** - stay calm!

---

**Good luck!**
