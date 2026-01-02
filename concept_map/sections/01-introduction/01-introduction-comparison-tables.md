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
| [[02-data-ingestion#Amazon-S3]] | Object | Data lakes, model artifacts, any file | High | Low |
| [[02-data-ingestion#Amazon-EBS]] | Block | EC2 instance storage, databases | Low | Medium |
| [[02-data-ingestion#Amazon-EFS]] | File (NFS) | Shared storage across instances | Medium | Medium |
| [[02-data-ingestion#Amazon-FSx]] | File (various) | High-performance workloads (Lustre, Windows) | Very Low | High |

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

| Criteria | [[03-data-transformation#Amazon-EMR]] | [[03-data-transformation#AWS-Glue]] | [[05-sagemaker-algorithms#SageMaker]] Processing |
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

| Criteria | [[05-sagemaker-algorithms#SageMaker]] | [[08-bedrock-applications#Amazon-Bedrock]] |
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
| Text analysis | [[04-managed-ai-services#Amazon-Comprehend]] | Text | Sentiment, entities, topics |
| Document extraction | [[04-managed-ai-services#Amazon-Textract]] | Images/PDFs | Structured data |
| Translation | [[04-managed-ai-services#Amazon-Translate]] | Text | Translated text |
| Speech-to-text | [[04-managed-ai-services#Amazon-Transcribe]] | Audio | Text |
| Text-to-speech | [[04-managed-ai-services#Amazon-Polly]] | Text | Audio |
| Chatbots | [[04-managed-ai-services#Amazon-Lex]] | Text/Voice | Responses |
| Image/Video analysis | [[04-managed-ai-services#Amazon-Rekognition]] | Images/Video | Labels, faces, objects |
| Recommendations | [[04-managed-ai-services#Amazon-Personalize]] | User behavior | Recommendations |
| Time series forecast | [[04-managed-ai-services#Amazon-Forecast]] | Historical data | Predictions |
| Enterprise search | [[04-managed-ai-services#Amazon-Kendra]] | Documents | Search results |
| Fraud detection | [[04-managed-ai-services#Amazon-Fraud-Detector]] | Transaction data | Risk scores |
| Equipment anomaly | [[04-managed-ai-services#Amazon-Lookout]] | Sensor data | Anomalies |

---

### MLOps: CI/CD Service Comparison

| Service | Purpose | Stage |
|---------|---------|-------|
| [[09-mlops#CodeBuild]] | Build/compile code, run tests | Build |
| [[09-mlops#CodeDeploy]] | Deploy to EC2, Lambda, ECS | Deploy |
| [[09-mlops#CodePipeline]] | Orchestrate full CI/CD workflow | Orchestration |

**Pipeline Flow**:
```
Source (CodeCommit/GitHub) → CodeBuild → CodeDeploy
                              ↓
                        CodePipeline (orchestrates all)
```

---

### Infrastructure as Code: CloudFormation vs CDK

| Criteria | [[09-mlops#CloudFormation]] | [[09-mlops#CDK]] |
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

| Criteria | [[09-mlops#EventBridge]] | [[09-mlops#MWAA]] |
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
| [[10-security-compliance#IAM]] | Access management | Who can do what |
| [[10-security-compliance#KMS]] | Encryption key management | Data at rest |
| [[10-security-compliance#Secrets-Manager]] | Store secrets | Credentials, API keys |
| [[10-security-compliance#VPC]] | Network isolation | Network traffic |
| [[10-security-compliance#PrivateLink]] | Private connectivity | Service endpoints |
| [[10-security-compliance#AWS-WAF]] | Web application firewall | Web apps from attacks |
| [[10-security-compliance#AWS-Shield]] | DDoS protection | Infrastructure |
| [[10-security-compliance#Amazon-Macie]] | Data discovery | Sensitive data in S3 |

---

### Monitoring & Governance Services

| Service | Purpose | Data Type |
|---------|---------|-----------|
| [[11-management-governance#CloudWatch]] | Metrics, logs, alarms | Operational data |
| [[11-management-governance#CloudTrail]] | API call auditing | Who did what |
| [[11-management-governance#AWS-Config]] | Resource compliance | Configuration state |
| [[11-management-governance#AWS-X-Ray]] | Distributed tracing | Request flow |
| [[11-management-governance#Trusted-Advisor]] | Best practice checks | Recommendations |
| [[11-management-governance#AWS-Budgets]] | Cost alerts | Spending thresholds |
| [[11-management-governance#Cost-Explorer]] | Cost analysis | Historical costs |

---

## ML Lifecycle Phase Mapping

| Phase | Activities | Key Services |
|-------|------------|--------------|
| **Process Data** | Collect, store, catalog | [[02-data-ingestion#Amazon-S3]], [[02-data-ingestion#Amazon-Kinesis-Data-Streams]], [[03-data-transformation#AWS-Glue]] |
| **Develop Model** | Transform, train, tune, evaluate | [[03-data-transformation#Amazon-EMR]], [[05-sagemaker-algorithms#SageMaker]], [[03-data-transformation#AWS-Glue]] |
| **Deploy** | Package, serve, scale | [[05-sagemaker-algorithms#SageMaker]], [[09-mlops#ECS]], [[09-mlops#ECR]] |
| **Monitor** | Track performance, detect drift | [[11-management-governance#CloudWatch]], [[05-sagemaker-algorithms#SageMaker]] |
