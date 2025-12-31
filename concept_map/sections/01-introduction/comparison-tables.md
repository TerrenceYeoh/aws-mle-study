# Section 1: Introduction - Comparison Tables

## Exam Comparison: MLA-C01 vs Related Certifications

| Aspect | ML Engineer Associate (MLA-C01) | ML Specialty | Data Engineer Associate | AI Practitioner |
|--------|--------------------------------|--------------|------------------------|-----------------|
| Level | Associate | Specialty | Associate | Foundational |
| Focus | Implementation | Design & Architecture | Data pipelines | AI/ML concepts |
| Depth | Operational | Deep technical | Data-focused | Broad overview |
| SageMaker | Heavy focus | Heavy focus | Light | Light |
| GenAI/Bedrock | Yes | Limited | No | Yes |

---

## Service Category Comparisons

### Storage Services: When to Use What?

| Service | Type | Use Case | Latency | Cost |
|---------|------|----------|---------|------|
| [[S3]] | Object | Data lakes, model artifacts, any file | High | Low |
| [[EBS]] | Block | EC2 instance storage, databases | Low | Medium |
| [[EFS]] | File (NFS) | Shared storage across instances | Medium | Medium |
| [[FSx]] | File (various) | High-performance workloads (Lustre, Windows) | Very Low | High |

**Decision Flow**:
```
Need shared access across instances?
├── Yes → Need extreme performance? → Yes → FSx Lustre
│                                   → No  → EFS
└── No  → Need block storage for EC2? → Yes → EBS
                                      → No  → S3
```

---

### Data Processing: EMR vs Glue vs SageMaker Processing

| Criteria | [[EMR]] | [[Glue]] | [[SageMaker]] Processing |
|----------|---------|----------|-------------------------|
| Management | Self-managed clusters | Serverless | Serverless |
| Best For | Complex big data, Spark/Hadoop | ETL jobs, data catalog | ML-specific preprocessing |
| Scaling | Manual/Auto | Automatic | Automatic |
| Cost Model | Per instance-hour | Per DPU-hour | Per instance-hour |
| Integration | Standalone | Data Catalog, S3 | SageMaker ecosystem |

**When to Use**:
- **EMR**: Custom Spark/Hadoop jobs, need full cluster control
- **Glue**: Simple ETL, need data catalog, serverless preferred
- **SageMaker Processing**: ML preprocessing, part of SageMaker pipeline

---

### ML Platform: SageMaker vs Bedrock

| Criteria | [[SageMaker]] | [[Bedrock]] |
|----------|---------------|-------------|
| Purpose | Full ML platform | Foundation model access |
| Model Type | Train custom models | Use pre-trained FMs |
| Customization | Full control | Fine-tuning, RAG |
| Complexity | Higher | Lower |
| Use Case | Custom ML solutions | GenAI applications |

**Decision Flow**:
```
Need to train custom models?
├── Yes → SageMaker
└── No  → Want to use foundation models (LLMs)?
          ├── Yes → Bedrock
          └── No  → Consider Managed AI Services
```

---

### Managed AI Services by Use Case

| Use Case | Service | Input | Output |
|----------|---------|-------|--------|
| Text analysis | [[Comprehend]] | Text | Sentiment, entities, topics |
| Document extraction | [[Textract]] | Images/PDFs | Structured data |
| Translation | [[Translate]] | Text | Translated text |
| Speech-to-text | [[Transcribe]] | Audio | Text |
| Text-to-speech | [[Polly]] | Text | Audio |
| Chatbots | [[Lex]] | Text/Voice | Responses |
| Image/Video analysis | [[Rekognition]] | Images/Video | Labels, faces, objects |
| Recommendations | [[Personalize]] | User behavior | Recommendations |
| Time series forecast | [[Forecast]] | Historical data | Predictions |
| Enterprise search | [[Kendra]] | Documents | Search results |
| Fraud detection | [[Fraud-Detector]] | Transaction data | Risk scores |
| Equipment anomaly | [[Lookout-for-Equipment]] | Sensor data | Anomalies |

---

### MLOps: CI/CD Service Comparison

| Service | Purpose | Stage |
|---------|---------|-------|
| [[CodeBuild]] | Build/compile code, run tests | Build |
| [[CodeDeploy]] | Deploy to EC2, Lambda, ECS | Deploy |
| [[CodePipeline]] | Orchestrate full CI/CD workflow | Orchestration |

**Pipeline Flow**:
```
Source (CodeCommit/GitHub) → CodeBuild → CodeDeploy
                              ↓
                        CodePipeline (orchestrates all)
```

---

### Infrastructure as Code: CloudFormation vs CDK

| Criteria | [[CloudFormation]] | [[CDK]] |
|----------|-------------------|---------|
| Language | YAML/JSON | Python, TypeScript, Java, etc. |
| Abstraction | Low-level | High-level constructs |
| Learning Curve | Template syntax | Programming language |
| Reusability | Copy/paste templates | OOP patterns, inheritance |
| Output | Direct deployment | Generates CloudFormation |

**When to Use**:
- **CloudFormation**: Simple stacks, prefer declarative YAML
- **CDK**: Complex infrastructure, prefer programming languages

---

### Orchestration: EventBridge vs MWAA (Airflow)

| Criteria | [[EventBridge]] | [[MWAA]] |
|----------|-----------------|----------|
| Type | Event-driven | Workflow orchestration |
| Trigger | Events (real-time) | Scheduled/dependency-based |
| Complexity | Simple rules | Complex DAGs |
| Use Case | React to AWS events | Batch workflows, ML pipelines |
| Management | Serverless | Managed Airflow |

---

### Security Services Overview

| Service | Purpose | Protects |
|---------|---------|----------|
| [[IAM]] | Access management | Who can do what |
| [[KMS]] | Encryption key management | Data at rest |
| [[Secrets-Manager]] | Store secrets | Credentials, API keys |
| [[VPC]] | Network isolation | Network traffic |
| [[PrivateLink]] | Private connectivity | Service endpoints |
| [[WAF]] | Web application firewall | Web apps from attacks |
| [[Shield]] | DDoS protection | Infrastructure |
| [[Macie]] | Data discovery | Sensitive data in S3 |

---

### Monitoring & Governance Services

| Service | Purpose | Data Type |
|---------|---------|-----------|
| [[CloudWatch]] | Metrics, logs, alarms | Operational data |
| [[CloudTrail]] | API call auditing | Who did what |
| [[Config]] | Resource compliance | Configuration state |
| [[X-Ray]] | Distributed tracing | Request flow |
| [[Trusted-Advisor]] | Best practice checks | Recommendations |
| [[Budgets]] | Cost alerts | Spending thresholds |
| [[Cost-Explorer]] | Cost analysis | Historical costs |

---

## ML Lifecycle Phase Mapping

| Phase | Activities | Key Services |
|-------|------------|--------------|
| **Process Data** | Collect, store, catalog | [[S3]], [[Kinesis]], [[Glue]] |
| **Develop Model** | Transform, train, tune, evaluate | [[EMR]], [[SageMaker]], [[Glue]] |
| **Deploy** | Package, serve, scale | [[SageMaker]], [[ECS]], [[ECR]] |
| **Monitor** | Track performance, detect drift | [[CloudWatch]], [[SageMaker]] |
