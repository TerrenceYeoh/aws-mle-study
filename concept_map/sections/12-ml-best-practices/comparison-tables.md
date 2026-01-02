# Section 12: ML Best Practices - Comparison Tables

## Responsible AI Tools

| Tool | Purpose | Key Feature |
|------|---------|-------------|
| **SageMaker Clarify** | Bias detection & explainability | Pre/post-training bias metrics, SHAP values |
| **SageMaker Model Monitor** | Production model monitoring | Drift detection, quality metrics |
| **Amazon Augmented AI (A2I)** | Human-in-the-loop | Review low-confidence predictions |
| **SageMaker Model Cards** | Model documentation | Governance & transparency |
| **Bedrock Model Evaluation** | Foundation model evaluation | Compare model performance |

---

## ML Lifecycle Phase Tools

### Data Processing

| Tool | Primary Use |
|------|-------------|
| **Ground Truth** | Data labeling |
| **Data Wrangler** | Interactive data preparation |
| **AWS Glue** | Data catalog & ETL |
| **Feature Store** | Feature storage & reuse |
| **Athena** | Query data, remove PII |
| **Macie** | Sensitive data discovery |
| **Comprehend** | PII detection in text |

### Model Development

| Tool | Primary Use |
|------|-------------|
| **SageMaker Experiments** | Track experiments |
| **SageMaker Debugger** | Debug training issues |
| **Training Compiler** | Optimize training code |
| **Automatic Model Tuning** | Hyperparameter optimization |
| **Autopilot** | AutoML |
| **Distributed Training Libraries** | Scale across instances |

### Deployment

| Tool | Primary Use |
|------|-------------|
| **SageMaker Endpoints** | Real-time inference |
| **Serverless Inference** | Variable traffic |
| **Batch Transform** | Large-scale batch |
| **Inference Recommender** | Right-size endpoints |
| **SageMaker Neo** | Model optimization |
| **IoT Greengrass** | Edge deployment |

### Monitoring

| Tool | Primary Use |
|------|-------------|
| **Model Monitor** | Data/model quality, bias |
| **CloudWatch** | Metrics & logs |
| **SageMaker Pipelines** | Automated retraining |
| **QuickSight** | ROI dashboards |

---

## HPO Methods Comparison

| Method | Efficiency | When to Use | AWS Support |
|--------|------------|-------------|-------------|
| **Bayesian** | High | Default choice | SageMaker Auto Tuning |
| **Hyperband** | High | Early stopping beneficial | SageMaker Auto Tuning |
| **Random Search** | Low | Simple problems only | SageMaker Auto Tuning |
| **Grid Search** | Very Low | Avoid - exhaustive | Manual only |

**Best Practice:** Always prefer **Bayesian** or **Hyperband** over random/grid search.

---

## Deployment Strategies

| Strategy | Traffic Shift | Rollback | Best For |
|----------|---------------|----------|----------|
| **Blue/Green** | Instant 100% | Instant | Quick full cutover |
| **Canary** | Small % first | Fast | Risk mitigation |
| **Linear** | Gradual % | Moderate | Controlled rollout |
| **A/B Testing** | Split traffic | N/A | Compare model versions |

---

## Inference Deployment Options

| Option | Latency | Cost Model | Best For |
|--------|---------|------------|----------|
| **Real-time** | Low (ms) | Always-on | Production APIs |
| **Serverless** | Variable | Pay per request | Variable traffic |
| **Asynchronous** | Minutes | Queue-based | Long-running inference |
| **Batch Transform** | Hours | Per job | Large datasets |

---

## Hardware for ML Workloads

### Training Hardware

| Instance Type | Chip | Best For |
|---------------|------|----------|
| **p4d/p5** | NVIDIA GPU | Large-scale DL training |
| **trn1** | Trainium | Cost-effective DL training |
| **g5** | NVIDIA GPU | General GPU training |
| **CPU instances** | Intel/AMD/Graviton | Traditional ML |

### Inference Hardware

| Instance Type | Chip | Best For |
|---------------|------|----------|
| **inf1/inf2** | Inferentia | Deep learning inference |
| **g4dn** | NVIDIA GPU | GPU inference |
| **Graviton3** | ARM | CPU inference (cost-effective) |
| **Elastic Inference** | Add-on GPU | Flexible GPU acceleration |

**Key Insight:** AWS custom chips (Trainium, Inferentia) offer better price-performance for specific workloads.

---

## Cost Optimization Strategies

| Phase | Strategy | AWS Tool |
|-------|----------|----------|
| **Training** | Spot Instances | Managed Spot Training |
| **Training** | Stop resources when idle | Lifecycle Configuration |
| **Training** | Warm-start HPO | Auto Model Tuning |
| **Inference** | Right-size fleet | Inference Recommender |
| **Inference** | Auto-scaling | SageMaker AutoScaling |
| **Inference** | Serverless for variable traffic | Serverless Inference |
| **All** | Resource tagging | AWS Budgets, Cost Explorer |

---

## Model Optimization Tools

| Tool | Optimization Type | Use Case |
|------|-------------------|----------|
| **SageMaker Neo** | Compilation | Edge & cloud deployment |
| **Training Compiler** | Graph optimization | Faster training |
| **Treelite** | Tree model compilation | Decision tree inference |
| **Hugging Face Infinity** | Transformer optimization | NLP model inference |

---

## Monitoring Types in Model Monitor

| Monitor Type | What It Detects | Baseline |
|--------------|-----------------|----------|
| **Data Quality** | Schema changes, missing values, outliers | Training data statistics |
| **Model Quality** | Accuracy degradation | Ground truth labels |
| **Bias Drift** | Fairness metric changes | Pre-training bias analysis |
| **Feature Attribution** | Feature importance drift | SHAP values |

---

## Version Control & Lineage

| Component | Tool |
|-----------|------|
| Code | Git, CodeCommit |
| Notebooks | Git, SageMaker Studio |
| Data | S3 versioning, Feature Store |
| Features | Feature Store |
| Models | Model Registry |
| Experiments | SageMaker Experiments |
| Pipelines | SageMaker Pipelines |
| Full Lineage | ML Lineage Tracking |

---

## Security Best Practices

| Practice | AWS Tools |
|----------|-----------|
| Least privilege access | IAM |
| Data encryption at rest | KMS |
| Data encryption in transit | TLS, inter-node encryption |
| Network isolation | VPC, PrivateLink |
| Secret management | Secrets Manager |
| Sensitive data protection | Macie |
| Secure inter-node communication | SageMaker inter-node encryption |

---

## Quick Decision Tables

### Which SageMaker Tool for This Task?

| Task | Tool |
|------|------|
| Detect bias in data/model | **Clarify** |
| Monitor production model | **Model Monitor** |
| Track experiments | **Experiments** |
| Debug training | **Debugger** |
| Store/share features | **Feature Store** |
| Orchestrate ML workflow | **Pipelines** |
| Version models | **Model Registry** |
| Right-size endpoints | **Inference Recommender** |
| Optimize for edge | **Neo** |
| AutoML | **Autopilot** |

### Which Instance for This Workload?

| Workload | Instance |
|----------|----------|
| DL training (cost-effective) | **trn1** (Trainium) |
| DL training (high-performance) | **p4d/p5** (NVIDIA) |
| DL inference (cost-effective) | **inf1/inf2** (Inferentia) |
| CPU inference (cost-effective) | **Graviton3** |
| GPU inference | **g4dn** |
| Traditional ML | CPU instances |

### Which Deployment Option?

| Need | Option |
|------|--------|
| Low latency (<100ms) | **Real-time** |
| Variable/unpredictable traffic | **Serverless** |
| Long-running predictions | **Asynchronous** |
| Large batch of data | **Batch Transform** |
| Multiple models, one endpoint | **Multi-Model Endpoint** |
| Edge devices | **Neo + Greengrass** |

### Which Deployment Strategy?

| Need | Strategy |
|------|----------|
| Quick full cutover | **Blue/Green** |
| Risk mitigation | **Canary** |
| Gradual rollout | **Linear** |
| Compare model versions | **A/B Testing** |

### Which Monitoring Tool?

| Need | Tool |
|------|------|
| Data quality issues | **Model Monitor** |
| Model accuracy degradation | **Model Monitor** |
| Bias drift | **Model Monitor + Clarify** |
| Infrastructure metrics | **CloudWatch** |
| Human review | **Amazon A2I** |
| Cost tracking | **AWS Budgets** |

---

## Trade-off Analysis

### Common ML Trade-offs

| Trade-off | Consideration |
|-----------|---------------|
| **Accuracy vs. Complexity** | Simpler models are easier to explain/maintain |
| **Bias vs. Fairness** | May need to sacrifice some accuracy for fairness |
| **Bias vs. Variance** | Balance underfitting vs. overfitting |
| **Precision vs. Recall** | Depends on business cost of false positives/negatives |
| **Latency vs. Cost** | Real-time is expensive; batch is cheaper |
| **Custom vs. Pre-trained** | Training from scratch is resource-intensive |

**Tools for Trade-off Analysis:** SageMaker Experiments, Clarify

---

## Sustainability Practices by Phase

| Phase | Practice | Benefit |
|-------|----------|---------|
| **Problem Framing** | Use pre-trained models | Avoid expensive training |
| **Problem Framing** | Select sustainable regions | Greener energy |
| **Data Processing** | Minimize idle resources | Reduce waste |
| **Training** | Early stopping | Don't over-train |
| **Training** | Bayesian HPO | Fewer training runs |
| **Training** | Limit concurrent jobs | Resource efficiency |
| **Deployment** | Serverless for variable traffic | No idle resources |
| **Deployment** | Efficient silicon (Graviton, Inferentia) | Better performance/watt |
| **Monitoring** | Retrain only when necessary | Reduce training frequency |

---

## MLOps Workload Orchestrator Pipelines

| Pipeline | Purpose |
|----------|---------|
| Training + HPO | Train model with hyperparameter tuning |
| Training + Autopilot | Train with AutoML |
| BYOM Real-time | Deploy your own model for real-time |
| BYOM Batch | Deploy your own model for batch |
| Custom Algorithm | Use your own Docker/ECR images |
| Data Quality Monitor | Monitor inference data quality |
| Model Quality Monitor | Monitor model accuracy |
| Bias Monitor | Monitor for bias drift |
| Explainability Monitor | Monitor feature attribution |
