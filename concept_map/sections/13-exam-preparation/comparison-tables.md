# Section 13: Exam Preparation - Comparison Tables

## Question Types Comparison

| Type | Format | Choices | Partial Credit | Strategy |
|------|--------|---------|----------------|----------|
| **Multiple Choice** | 1 correct answer | 4 options | N/A | Eliminate wrong answers |
| **Multiple Response** | 2+ correct answers | 5+ options | NO | Read ALL options carefully |
| **Ordering** | Arrange in correct order | 3-5 steps | NO | Think through workflow |
| **Matching** | Match items to prompts | 3-7 pairs | NO | Match certain ones first |
| **Case Study** | Multiple Qs, same scenario | Varies | Each Q separate | Read scenario once carefully |

---

## Exam Logistics

| Aspect | Detail |
|--------|--------|
| **Exam Code** | MLA-C01 |
| **Duration** | 170 minutes |
| **Questions** | 65 |
| **Passing Score** | 720/1000 |
| **Cost** | $300 USD |
| **Delivery** | Pearson VUE / PSI |
| **Languages** | English, others TBD |

---

## Exam Domain Weights

| Domain | Topic | Weight |
|--------|-------|--------|
| 1 | Data Preparation for ML | 28% |
| 2 | ML Model Development | 26% |
| 3 | Deployment and Orchestration | 22% |
| 4 | Monitoring, Maintenance, Security | 24% |

---

## Preparation Resources Comparison

| Resource | Type | Cost | Best For |
|----------|------|------|----------|
| **Standard Exam Prep Plan** | Video + Quiz | Free | Initial learning |
| **Official Practice Questions** | 20 Questions | Free | Question format familiarity |
| **Enhanced Exam Prep Plan** | Comprehensive | $29/month | Deep preparation |
| **SageMaker Developer Guide** | Documentation | Free | Technical reference |
| **MLA-C01 Exam Guide** | PDF | Free | Exam blueprint |
| **Third-party Practice Exams** | Full exams | Varies | Realistic practice |

---

## AWS Certification Levels

| Level | Experience Required | Examples |
|-------|---------------------|----------|
| **Foundational** | None | Cloud Practitioner, AI Practitioner |
| **Associate** | Prior cloud/IT experience | Solutions Architect, Developer, ML Engineer |
| **Professional** | 2+ years AWS | Solutions Architect Pro, DevOps Engineer Pro |
| **Specialty** | Varies | Security, Machine Learning, Networking |

---

## Certification Paths to ML Engineer

### Path 1: Data-Focused
| Step | Certification | Focus |
|------|---------------|-------|
| 1 | Cloud Practitioner | Cloud basics |
| 2 | Solutions Architect Associate | Architecture |
| 3 | Data Engineer Associate | Data pipelines |
| 4 | **ML Engineer Associate** | **Target** |
| 5 | ML Specialty | Deep expertise |

### Path 2: AI-Focused
| Step | Certification | Focus |
|------|---------------|-------|
| 1 | AI Practitioner | AI/ML basics |
| 2 | Solutions Architect Associate | Architecture |
| 3 | **ML Engineer Associate** | **Target** |
| 4 | ML Specialty | Deep expertise |

### Path 3: DevOps-Focused
| Step | Certification | Focus |
|------|---------------|-------|
| 1 | Developer Associate | Dev skills |
| 2 | SysOps Administrator | Operations |
| 3 | **ML Engineer Associate** | **Target** |
| 4 | DevOps Engineer Pro | MLOps |

---

## Test-Taking Strategies

| Strategy | When to Use | Benefit |
|----------|-------------|---------|
| **Process of Elimination** | Unsure of answer | Increases odds |
| **Flag and Skip** | Taking >3 min | Better time use |
| **Read All Options** | Multiple response | Catch all correct answers |
| **Identify Keywords** | Every question | Focus on requirements |
| **Review Flagged** | End of exam | Fresh perspective |

---

## Key Signals in Questions

| Signal Word | Usually Points To |
|-------------|-------------------|
| "Cost-effective" | Spot Instances, Serverless, right-sizing |
| "Fastest" | Provisioned capacity, parallelization |
| "Scalable" | Managed services, auto-scaling |
| "Secure" | KMS, VPC, IAM, encryption |
| "Real-time" | Kinesis, streaming endpoints |
| "Batch" | Batch Transform, Glue |
| "Minimal operational overhead" | Managed/serverless services |
| "Fault-tolerant" | Multi-AZ, backup strategies |

---

## Formulas to Memorize

### Classification Metrics

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Precision** | TP / (TP + FP) | Of predicted positive, % correct |
| **Recall** | TP / (TP + FN) | Of actual positive, % found |
| **F1 Score** | 2 × (P × R) / (P + R) | Harmonic mean of P and R |
| **Accuracy** | (TP + TN) / Total | Overall correctness |
| **Specificity** | TN / (TN + FP) | True negative rate |

### When to Prioritize

| Prioritize | When |
|------------|------|
| **Precision** | False positives are costly (spam, fraud alerts) |
| **Recall** | False negatives are costly (disease detection, security) |
| **F1 Score** | Need balance between precision and recall |

---

## Regularization Techniques

| Technique | Type | Effect | Use When |
|-----------|------|--------|----------|
| **L1 (Lasso)** | Weight penalty | Sparse weights, feature selection | Too many features |
| **L2 (Ridge)** | Weight penalty | Smaller weights | Overfitting, keep all features |
| **Elastic Net** | L1 + L2 | Combined benefits | Best of both worlds |
| **Dropout** | Neural network | Random neuron deactivation | Deep learning overfitting |
| **Early Stopping** | Training control | Stop at optimal point | Validation loss increasing |
| **Data Augmentation** | Data enhancement | More training examples | Limited training data |

---

## Common Service Confusions

### Storage for ML

| Need | Service | NOT |
|------|---------|-----|
| Training data storage | **S3** | EBS (instance-attached) |
| Feature storage | **Feature Store** | DynamoDB (wrong use case) |
| Model artifacts | **S3** | EFS (usually) |
| Low-latency feature lookup | **Feature Store Online** | S3 (too slow) |

### Training Options

| Need | Service | NOT |
|------|---------|-----|
| Built-in algorithm | **SageMaker Training** | EC2 (manual setup) |
| Custom container | **SageMaker + ECR** | Lambda (size limits) |
| Distributed training | **SageMaker Distributed** | Multiple EC2s (manual) |
| HPO | **SageMaker Auto Tuning** | Manual tuning |

### Deployment Options

| Need | Service | NOT |
|------|---------|-----|
| Real-time inference | **SageMaker Endpoint** | Batch Transform |
| Variable traffic | **Serverless Inference** | Always-on endpoint |
| Large batch | **Batch Transform** | Real-time endpoint |
| Edge deployment | **SageMaker Neo + Greengrass** | Cloud endpoint |

### Monitoring

| Need | Service | NOT |
|------|---------|-----|
| Data drift | **Model Monitor** | CloudWatch (metrics only) |
| Bias detection | **Clarify** | Model Monitor alone |
| Infrastructure metrics | **CloudWatch** | Model Monitor |
| API auditing | **CloudTrail** | CloudWatch Logs |

---

## Quick Decision Tables

### Which Exam Prep Resource?

| Need | Resource |
|------|----------|
| Learn exam format | Official Practice Questions (free) |
| Comprehensive prep | Standard Exam Prep Plan (free) |
| Hands-on practice | Enhanced Plan (paid) |
| Technical deep-dive | SageMaker Developer Guide |
| Exam blueprint | MLA-C01 Exam Guide |

### Which Certification Next?

| If You Have | Consider Next |
|-------------|---------------|
| No certifications | AI Practitioner or Cloud Practitioner |
| Cloud Practitioner | AI Practitioner or Solutions Architect |
| AI Practitioner | ML Engineer Associate |
| ML Engineer Associate | Data Engineer or ML Specialty |
| ML Specialty | You're done with ML path! |

### Time Allocation Strategy

| Phase | Time | Focus |
|-------|------|-------|
| First pass | 120 min | Answer all, flag uncertain |
| Review flagged | 30 min | Reconsider difficult ones |
| Final check | 20 min | Review all answers |

---

## Day-of Checklist

| Category | Item |
|----------|------|
| **Documents** | Valid government ID |
| **Logistics** | Test center location confirmed |
| **Physical** | Good night's sleep |
| **Physical** | Light meal (not right before) |
| **Physical** | Bathroom break before |
| **Mental** | Review key formulas |
| **Mental** | Confidence in preparation |

---

## Common Mistakes to Avoid

| Mistake | Better Approach |
|---------|-----------------|
| Rushing through questions | Take full 2-2.5 min per question |
| Not reading all options | Read every choice before selecting |
| Changing answers without reason | Trust first instinct unless certain |
| Spending too long on one question | Flag and move on after 3 min |
| Not using scratch paper | Write out complex scenarios |
| Ignoring "NOT" or "EXCEPT" | Highlight negative keywords |
| Assuming simpler is wrong | AWS often prefers simpler solutions |
