# Section 12: ML Best Practices

## Overview

This section covers best practices for designing, building, deploying, and monitoring machine learning systems on AWS. Key themes include **Responsible AI**, the **ML Lifecycle**, **sustainability**, and leveraging AWS services across all phases. The content aligns with the **AWS Well-Architected Machine Learning Lens**.

**Key Takeaways:**
- 8 dimensions of Responsible AI: Fairness, Explainability, Privacy/Security, Safety, Controllability, Veracity/Robustness, Governance, Transparency
- ML Lifecycle: Business Goal → Problem Framing → Data Processing → Model Development → Deployment → Monitoring
- Sustainability is a cross-cutting concern across all phases
- SageMaker provides tools for nearly every best practice

---

## Core Concepts

### Responsible-AI

**8 Core Dimensions:**
| Dimension | Description | AWS Tool |
|-----------|-------------|----------|
| **Fairness** | Equitable treatment across groups | SageMaker Clarify |
| **Explainability** | Understanding model decisions | SageMaker Clarify |
| **Privacy & Security** | Protecting sensitive data | KMS, IAM, Macie |
| **Safety** | Preventing harm | Model Monitor |
| **Controllability** | Human oversight | Amazon A2I |
| **Veracity & Robustness** | Accurate and reliable outputs | Model Monitor |
| **Governance** | Policies and procedures | ML Governance, Model Cards |
| **Transparency** | Clear communication about AI use | Model Cards |

**Related:** [[12-ml-best-practices#SageMaker-Clarify]], [[12-ml-best-practices#Amazon-Augmented-AI]], [[12-ml-best-practices#SageMaker-Model-Monitor]]

---

### ML-Lifecycle

**AWS-Defined ML Lifecycle:**
```
┌─────────────┐    ┌──────────────┐    ┌─────────────────┐
│  Business   │ →  │  ML Problem  │ →  │     Data        │
│    Goal     │    │   Framing    │    │   Processing    │
└─────────────┘    └──────────────┘    └────────┬────────┘
                                                │
┌─────────────┐    ┌──────────────┐    ┌────────▼────────┐
│  Monitoring │ ←  │  Deployment  │ ←  │     Model       │
│             │    │              │    │   Development   │
└──────┬──────┘    └──────────────┘    └─────────────────┘
       │
       └──────────────── Feedback Loop ────────────────────→
```

**Detailed Steps:**
1. **Identify Business Goal** - KPIs, ROI, explainability requirements
2. **Frame ML Problem** - Roles, lineage tracking, feedback loops
3. **Collect Data** - Label, ingest, aggregate
4. **Pre-Process Data** - Clean, partition, scale, unbias, augment
5. **Engineer Features** - Selection, transformation, creation, extraction
6. **Train, Tune, & Evaluate** - Algorithm selection, HPO, validation
7. **Deploy** - Endpoint strategies, cloud vs edge
8. **Monitor** - Drift detection, retraining triggers, human-in-the-loop

---

### ML-Design-Principles

| Principle | Description | AWS Tools |
|-----------|-------------|-----------|
| Assign ownership | Clear accountability | SageMaker Role Manager |
| Provide protection | Security controls | IAM, KMS, VPC |
| Enable resiliency | Fault tolerance | Multi-AZ, backups |
| Enable reusability | Share components | Feature Store, Model Registry |
| Enable reproducibility | Version control | Git, SageMaker Experiments |
| Optimize resources | Reduce cost | Spot Instances, right-sizing |
| Enable automation | CI/CD/CT | SageMaker Pipelines |
| Continuous improvement | Monitoring & analysis | Model Monitor, CloudWatch |
| Minimize environmental impact | Sustainability | Managed services, efficient silicon |

---

## AWS Services for ML Best Practices

### SageMaker-Clarify
**Purpose:** Bias detection, model evaluation, explainability

**Use Cases:**
- Detect bias in training data
- Explain model predictions (feature importance)
- Review fairness metrics
- Test trade-offs (bias vs. fairness)

**Related:** [[12-ml-best-practices#SageMaker-Model-Monitor]], [[12-ml-best-practices#SageMaker-Experiments]]

---

### SageMaker-Model-Monitor
**Purpose:** Monitor deployed models for quality degradation

**Monitors:**
- Data quality
- Model quality
- Bias drift
- Feature attribution drift

**Related:** [[12-ml-best-practices#SageMaker-Clarify]], [[11-management-governance#CloudWatch]]

---

### SageMaker-Feature-Store
**Purpose:** Centralized feature repository for consistency

**Key Benefit:** Ensures feature consistency between training and inference

**Components:**
- Online Feature Store (low-latency)
- Offline Feature Store (batch)

**Related:** [[09-mlops#SageMaker-Pipelines]], [[12-ml-best-practices#SageMaker-Experiments]]

---

### SageMaker-Pipelines
**Purpose:** ML workflow orchestration and CI/CD/CT

**Use Cases:**
- Automate data processing
- Automate training and evaluation
- Automate deployment
- Automated retraining framework

**Related:** [[09-mlops/09-mlops#Model-Registry]], [[09-mlops#CloudFormation]]

---

### SageMaker-Experiments
**Purpose:** Track and compare model experiments

**Use Cases:**
- Hyperparameter tracking
- Model improvement strategies
- Performance comparison
- Organize training artifacts

**Related:** [[06-model-training/06-model-training#SageMaker-Debugger]], [[09-mlops#SageMaker-Pipelines]]

---

### Amazon-Augmented-AI
**Purpose:** Human-in-the-loop for AI/ML workflows

**Use Cases:**
- Review low-confidence predictions
- Correct model outputs
- Quality assurance
- Compliance verification

**Related:** [[12-ml-best-practices#SageMaker-Model-Monitor]], [[03-data-transformation#Ground-Truth]]

---

### SageMaker-Inference-Recommender
**Purpose:** Right-size inference endpoints

**Provides:**
- Instance type recommendations
- Cost optimization
- Performance benchmarks

**Related:** SageMaker-AutoScaling, [[11-management-governance#CloudWatch]]

---

## Phase-Specific Best Practices

### Business Goal Identification

| Practice | AWS Tools |
|----------|-----------|
| Define KPIs | - |
| Agree on explainability | SageMaker Clarify |
| Plan drift monitoring | Model Monitor |
| Validate data permissions | IAM, Lake Formation |
| Define ROI/TCO | Cost Explorer, Budgets |
| Environmental impact | Sustainable regions |

---

### ML Problem Framing

| Practice | AWS Tools |
|----------|-----------|
| Establish roles | SageMaker Role Manager |
| Model improvement strategy | Experiments, HPO, AutoML |
| Lineage tracking | Lineage Tracking, Pipelines, Feature Store |
| Feedback loops | Model Monitor, CloudWatch, A2I |
| Data encryption | Glue DataBrew, KMS |
| API abstraction | SageMaker + API Gateway |
| Pre-trained vs custom | JumpStart, Marketplace |

---

### Data Processing

| Practice | AWS Tools |
|----------|-----------|
| Profile data quality | Data Wrangler, Glue, Athena |
| Version control | Model Registry, Git, Experiments |
| Least privilege | IAM |
| Protect sensitive data | Macie |
| Enforce lineage | ML Lineage Tracker |
| Remove PII | Comprehend, Transcribe, Athena |
| Data catalog | AWS Glue |
| Data pipeline | SageMaker Pipelines |
| Data labeling | Ground Truth |
| Feature reusability | Feature Store |

---

### Model Development

| Practice | AWS Tools |
|----------|-----------|
| CI/CD automation | CloudFormation, CDK, Pipelines |
| Reliable packaging | ECR, CodeArtifact |
| Inter-node encryption | SageMaker, EMR encryption |
| Feature consistency | Feature Store |
| Bias detection | Clarify |
| Managed training | SageMaker, Training Compiler, Spot |
| Distributed training | Distributed Training Libraries |
| HPO | Automatic Model Tuning |
| Debugging | SageMaker Debugger, CloudWatch |

**Efficient HPO Methods:**
- Prefer: **Bayesian**, **Hyperband**
- Avoid: Random search, Grid search

---

### Deployment

| Practice | AWS Tools |
|----------|-----------|
| Deployment strategies | Blue/Green, A/B, Linear, Canary |
| Cloud vs edge | SageMaker Endpoints vs Neo + Greengrass |
| Cost-effective hardware | Elastic Inference, Inf1/Inf2, Neo |
| Right-sizing | Inference Recommender, AutoScaling |
| Multiple models | Multi-Model Endpoints, Inference Pipelines |

**Efficient Silicon:**
| Chip | Use Case |
|------|----------|
| Graviton3 | CPU inference |
| Inferentia (inf2) | Deep learning inference |
| Trainium (trn1) | Training |

---

### Monitoring

| Practice | AWS Tools |
|----------|-----------|
| Model observability | Model Monitor, CloudWatch, Clarify |
| Data drift detection | Model Monitor |
| Auto-scaling | SageMaker AutoScaling |
| Automated retraining | Pipelines, Jenkins |
| Human-in-the-loop | Amazon A2I |
| Cost monitoring | Tagging, Budgets |
| ROI tracking | QuickSight |

---

## Sustainability Best Practices

### Across All Phases

| Phase | Sustainability Practice |
|-------|------------------------|
| **Problem Framing** | Use pre-trained models, select sustainable regions |
| **Data Processing** | Minimize idle resources, lifecycle policies |
| **Training** | Early stopping, efficient HPO (Bayesian), limit concurrent jobs |
| **Deployment** | Efficient silicon (Graviton, Inferentia), serverless for variable traffic |
| **Monitoring** | Retrain only when necessary, right-size instances |

---

## Tools & Solutions

### AWS Well-Architected ML Lens

**Purpose:** Assess ML workloads against best practices

**Features:**
- Custom lens for Well-Architected Tool
- Interview-style assessment
- Recommendations for improvement

---

### MLOps Workload Orchestrator

**Purpose:** Pre-built MLOps solution from AWS Solutions Library

**Features:**
- CloudFormation template
- 12 pre-built pipelines
- Training, inference, monitoring

**Pipeline Types:**
- Training with HPO or Autopilot
- BYOM real-time/batch inference
- Custom algorithm (Docker/ECR)
- Model Monitor (data quality, model quality, bias, explainability)

---

## Concept Relationships

```
                        ┌───────────────────────────┐
                        │    Responsible AI         │
                        │  (8 Core Dimensions)      │
                        └────────────┬──────────────┘
                                     │
        ┌────────────────────────────┼────────────────────────────┐
        ▼                            ▼                            ▼
┌───────────────┐          ┌─────────────────┐          ┌─────────────────┐
│   SageMaker   │          │   SageMaker     │          │    Amazon       │
│   Clarify     │          │  Model Monitor  │          │      A2I        │
│ (Bias/Explain)│          │ (Drift/Quality) │          │  (Human Loop)   │
└───────────────┘          └─────────────────┘          └─────────────────┘

                        ┌───────────────────────────┐
                        │     ML Lifecycle          │
                        └────────────┬──────────────┘
                                     │
    ┌─────────┬─────────┬─────────┬──┴──┬─────────┬─────────┐
    ▼         ▼         ▼         ▼     ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Business│ │Problem│ │ Data  │ │Model │ │Deploy │ │Monitor│
│ Goal  │ │Framing│ │Process│ │ Dev  │ │       │ │       │
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘

                        ┌───────────────────────────┐
                        │    SageMaker Ecosystem    │
                        └────────────┬──────────────┘
                                     │
    ┌─────────┬─────────┬─────────┬──┴──┬─────────┬─────────┐
    ▼         ▼         ▼         ▼     ▼         ▼         ▼
┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐
│Feature│ │Experi-│ │Pipe-  │ │Model │ │Clarify│ │Model  │
│ Store │ │ments  │ │lines  │ │Registry│       │ │Monitor│
└───────┘ └───────┘ └───────┘ └───────┘ └───────┘ └───────┘
```

---

## Exam Tips

### Responsible AI
- **8 dimensions** - memorize: Fairness, Explainability, Privacy/Security, Safety, Controllability, Veracity/Robustness, Governance, Transparency
- **SageMaker Clarify** = bias detection + explainability
- **Amazon A2I** = human-in-the-loop

### ML Lifecycle
- Know the **6 phases**: Business Goal → Problem Framing → Data Processing → Model Development → Deployment → Monitoring
- **Feedback loops** critical for continuous improvement

### Efficiency & Cost
- **Bayesian/Hyperband** for HPO (NOT random/grid search)
- **Spot Instances** for training cost savings
- **Inference Recommender** for right-sizing endpoints
- **Feature Store** ensures train/inference consistency

### Deployment
- Know deployment strategies: **Blue/Green**, **A/B**, **Linear**, **Canary**
- **Neo** for model optimization (edge + cloud)
- **Inferentia (inf2)** for DL inference
- **Trainium (trn1)** for training
- **Graviton3** for CPU inference

### Monitoring
- **Model Monitor** detects: data drift, model quality, bias, feature attribution
- **Retrain only when necessary** - define acceptable accuracy threshold

### Sustainability
- Cross-cutting concern across all phases
- Early stopping, efficient HPO, right-sizing, efficient silicon
- Consider pre-trained models vs training from scratch

### Well-Architected ML Lens
- Part of AWS Well-Architected Tool
- Interview-style assessment for ML workloads
