# Section 1: Introduction - Concept Map

## Overview
This section introduces the AWS Certified Machine Learning Engineer Associate (MLA-C01) exam, covering the course structure, target candidate profile, and the ML lifecycle framework.

**Key Takeaway**: The exam focuses on *implementing* ML solutions on AWS, not designing end-to-end architectures.

---

## Exam Details

### [[MLA-C01-Exam]]
- **Certification**: AWS Certified Machine Learning Engineer - Associate
- **Exam Code**: MLA-C01
- **Focus**: Implementation and operationalization of ML workloads

### [[Target-Candidate]]
**Required Experience**:
- 1 year with [[SageMaker]] and ML engineering services
- 1 year in software dev, DevOps, data engineering, or data science
- ML algorithms knowledge
- Data engineering fundamentals
- Software engineering and CI/CD

**NOT Required**:
- Designing end-to-end ML solutions
- Deep expertise in NLP, Computer Vision specializations

---

## Course Structure (12 Sections)

### Domain 1: Data Processing
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[02-data-ingestion]] | Data Ingestion & Storage | [[S3]], [[EBS]], [[EFS]], [[FSx]], [[Kinesis]] |
| [[03-data-transformation]] | Data Transformation & Feature Engineering | [[EMR]], [[SageMaker]], [[Glue]] |

### Domain 2: Model Development
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[04-managed-ai-services]] | AWS Managed AI Services | [[Comprehend]], [[Rekognition]], [[Textract]], [[Personalize]], etc. |
| [[05-sagemaker-algorithms]] | SageMaker Built-In Algorithms | [[SageMaker]] |
| [[06-model-training]] | Model Training, Tuning & Evaluation | [[SageMaker]] |

### Domain 3: Generative AI
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[07-genai-fundamentals]] | GenAI Model Fundamentals | [[SageMaker-JumpStart]] |
| [[08-bedrock-applications]] | Building GenAI Apps with Bedrock | [[Bedrock]] |

### Domain 4: MLOps
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[09-mlops]] | Machine Learning Operations | [[SageMaker]], [[ECS]], [[ECR]], [[CodePipeline]], [[MWAA]] |

### Domain 5: Security & Governance
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[10-security-compliance]] | Security, Identity & Compliance | [[IAM]], [[KMS]], [[VPC]], [[Macie]] |
| [[11-management-governance]] | Management & Governance | [[CloudWatch]], [[CloudTrail]], [[Config]] |

### Domain 6: Best Practices & Exam
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[12-ml-best-practices]] | ML Best Practices | Well-Architected ML Lens |
| [[13-exam-preparation]] | Exam Preparation | Practice questions |

---

## [[AWS-Well-Architected-ML-Lens]]

### ML Lifecycle Phases
```
┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Process Data │ → │Develop Model │ → │    Deploy    │ → │   Monitor    │
└──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
```

### Detailed Pipeline
```
Collect Data → Preprocess Data → Engineer Features → Train/Tune/Evaluate → Deploy → Monitor
     │              │                   │                  │                │        │
     ▼              ▼                   ▼                  ▼                ▼        ▼
   [S3]         [Glue/EMR]      [Feature Store]      [SageMaker]       [Endpoints] [CloudWatch]
```

### Key Components
| Component | Purpose | Related Services |
|-----------|---------|------------------|
| [[Feature-Store]] | Store/retrieve features for training & inference | [[SageMaker]] |
| [[Model-Registry]] | Version and manage model artifacts | [[SageMaker]] |
| [[Online-Feature-Store]] | Low-latency feature retrieval for real-time inference | [[SageMaker]] |
| [[Offline-Feature-Store]] | Batch feature retrieval for training | [[SageMaker]] |

### Feedback Loops
- **Performance Feedback Loop**: Monitor → Train/Tune (retrain on drift)
- **Active Learning Feedback Loop**: Monitor → Collect Data (improve data quality)

---

## AWS Services Overview

### Storage Services
- [[S3]] - Object storage, data lakes
- [[EBS]] - Block storage for EC2
- [[EFS]] - Shared file system
- [[FSx]] - High-performance file systems

### Streaming
- [[Kinesis]] - Real-time data streaming

### Data Processing
- [[EMR]] - Big data processing (Spark/Hadoop)
- [[Glue]] - Serverless ETL

### ML Platform
- [[SageMaker]] - End-to-end ML platform (central hub)
- [[Bedrock]] - Foundation models & GenAI

### Managed AI Services (13 total)
| Category | Services |
|----------|----------|
| NLP/Text | [[Comprehend]], [[Textract]], [[Translate]], [[Transcribe]] |
| Vision | [[Rekognition]] |
| Speech | [[Polly]], [[Lex]] |
| Recommendations | [[Personalize]] |
| Forecasting | [[Forecast]] |
| Search | [[Kendra]], [[Amazon-Q]] |
| Anomaly/Fraud | [[Lookout-for-Equipment]], [[Fraud-Detector]] |

### MLOps/DevOps
- [[ECS]], [[ECR]] - Containers
- [[CodeBuild]], [[CodeDeploy]], [[CodePipeline]] - CI/CD
- [[CloudFormation]], [[CDK]] - Infrastructure as Code
- [[EventBridge]], [[MWAA]] - Orchestration

### Security
- [[IAM]], [[KMS]], [[Secrets-Manager]] - Identity & encryption
- [[VPC]], [[PrivateLink]] - Network isolation
- [[WAF]], [[Shield]] - Protection
- [[Macie]] - Data discovery

### Monitoring & Governance
- [[CloudWatch]], [[X-Ray]] - Monitoring
- [[CloudTrail]], [[Config]] - Auditing
- [[Trusted-Advisor]], [[Budgets]], [[Cost-Explorer]] - Optimization

---

## Exam Tips
- Focus on **implementation**, not architecture design
- Know when to use each AWS service
- Understand the ML lifecycle and how services fit together
- [[SageMaker]] is the central hub - know it deeply
- Related certifications: ML Specialty, Data Engineer Associate, AI Practitioner
