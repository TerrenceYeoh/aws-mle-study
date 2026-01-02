# Section 1: Introduction - Concept Map

## Overview
This section introduces the AWS Certified Machine Learning Engineer Associate (MLA-C01) exam, covering the course structure, target candidate profile, and the ML lifecycle framework.

**Key Takeaway**: The exam focuses on *implementing* ML solutions on AWS, not designing end-to-end architectures.

---

## Exam Details

### MLA-C01-Exam
- **Certification**: AWS Certified Machine Learning Engineer - Associate
- **Exam Code**: MLA-C01
- **Focus**: Implementation and operationalization of ML workloads

### Target-Candidate
**Required Experience**:
- 1 year with [[05-sagemaker-algorithms#SageMaker]] and ML engineering services
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
| [[02-data-ingestion/02-data-ingestion]] | Data Ingestion & Storage | [[02-data-ingestion#Amazon-S3]], [[02-data-ingestion#Amazon-EBS]], [[02-data-ingestion#Amazon-EFS]], [[02-data-ingestion#Amazon-FSx]], [[02-data-ingestion#Amazon-Kinesis-Data-Streams]] |
| [[03-data-transformation/03-data-transformation]] | Data Transformation & Feature Engineering | [[03-data-transformation#Amazon-EMR]], [[05-sagemaker-algorithms#SageMaker]], [[03-data-transformation#AWS-Glue]] |

### Domain 2: Model Development
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[04-managed-ai-services/04-managed-ai-services]] | AWS Managed AI Services | [[04-managed-ai-services#Amazon-Comprehend]], [[04-managed-ai-services#Amazon-Rekognition]], [[04-managed-ai-services#Amazon-Textract]], [[04-managed-ai-services#Amazon-Personalize]], etc. |
| [[05-sagemaker-algorithms/05-sagemaker-algorithms]] | SageMaker Built-In Algorithms | [[05-sagemaker-algorithms#SageMaker]] |
| [[06-model-training/06-model-training]] | Model Training, Tuning & Evaluation | [[05-sagemaker-algorithms#SageMaker]] |

### Domain 3: Generative AI
| Section | Topic | Key Services |
|---------|-------|--------------|
| 07-genai-fundamentals | GenAI Model Fundamentals | [[08-bedrock-applications#SageMaker-JumpStart]] |
| 08-bedrock-applications | Building GenAI Apps with Bedrock | [[08-bedrock-applications#Amazon-Bedrock]] |

### Domain 4: MLOps
| Section | Topic | Key Services |
|---------|-------|--------------|
| [[09-mlops/09-mlops]] | Machine Learning Operations | [[05-sagemaker-algorithms#SageMaker]], [[09-mlops#ECS]], [[09-mlops#ECR]], [[09-mlops#CodePipeline]], [[09-mlops#MWAA]] |

### Domain 5: Security & Governance
| Section | Topic | Key Services |
|---------|-------|--------------|
| 10-security-compliance | Security, Identity & Compliance | [[10-security-compliance#IAM]], [[10-security-compliance#KMS]], [[10-security-compliance#VPC]], [[10-security-compliance#Amazon-Macie]] |
| 11-management-governance | Management & Governance | [[11-management-governance#CloudWatch]], [[11-management-governance#CloudTrail]], [[11-management-governance#AWS-Config]] |

### Domain 6: Best Practices & Exam
| Section                  | Topic             | Key Services             |
| ------------------------ | ----------------- | ------------------------ |
| 12-ml-best-practices | ML Best Practices | Well-Architected ML Lens |
| 13-exam-preparation  | Exam Preparation  | Practice questions       |
|                          |                   |                          |

---

## AWS-Well-Architected-ML-Lens

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
| Feature-Store | Store/retrieve features for training & inference | [[05-sagemaker-algorithms#SageMaker]] |
| [[09-mlops/09-mlops#Model-Registry]] | Version and manage model artifacts | [[05-sagemaker-algorithms#SageMaker]] |
| Online-Feature-Store | Low-latency feature retrieval for real-time inference | [[05-sagemaker-algorithms#SageMaker]] |
| Offline-Feature-Store | Batch feature retrieval for training | [[05-sagemaker-algorithms#SageMaker]] |

### Feedback Loops
- **Performance Feedback Loop**: Monitor → Train/Tune (retrain on drift)
- **Active Learning Feedback Loop**: Monitor → Collect Data (improve data quality)

---

## AWS Services Overview

### Storage Services
- [[02-data-ingestion#Amazon-S3]] - Object storage, data lakes
- [[02-data-ingestion#Amazon-EBS]] - Block storage for EC2
- [[02-data-ingestion#Amazon-EFS]] - Shared file system
- [[02-data-ingestion#Amazon-FSx]] - High-performance file systems

### Streaming
- [[02-data-ingestion#Amazon-Kinesis-Data-Streams]] - Real-time data streaming

### Data Processing
- [[03-data-transformation#Amazon-EMR]] - Big data processing (Spark/Hadoop)
- [[03-data-transformation#AWS-Glue]] - Serverless ETL

### ML Platform
- [[05-sagemaker-algorithms#SageMaker]] - End-to-end ML platform (central hub)
- [[08-bedrock-applications#Amazon-Bedrock]] - Foundation models & GenAI

### Managed AI Services (13 total)
| Category | Services |
|----------|----------|
| NLP/Text | [[04-managed-ai-services#Amazon-Comprehend]], [[04-managed-ai-services#Amazon-Textract]], [[04-managed-ai-services#Amazon-Translate]], [[04-managed-ai-services#Amazon-Transcribe]] |
| Vision | [[04-managed-ai-services#Amazon-Rekognition]] |
| Speech | [[04-managed-ai-services#Amazon-Polly]], [[04-managed-ai-services#Amazon-Lex]] |
| Recommendations | [[04-managed-ai-services#Amazon-Personalize]] |
| Forecasting | [[04-managed-ai-services#Amazon-Forecast]] |
| Search | [[04-managed-ai-services#Amazon-Kendra]], Amazon-Q |
| Anomaly/Fraud | [[04-managed-ai-services#Amazon-Lookout]], [[04-managed-ai-services#Amazon-Fraud-Detector]] |

### MLOps/DevOps
- [[09-mlops#ECS]], [[09-mlops#ECR]] - Containers
- [[09-mlops#CodeBuild]], [[09-mlops#CodeDeploy]], [[09-mlops#CodePipeline]] - CI/CD
- [[09-mlops#CloudFormation]], [[09-mlops#CDK]] - Infrastructure as Code
- [[09-mlops#EventBridge]], [[09-mlops#MWAA]] - Orchestration

### Security
- [[10-security-compliance#IAM]], [[10-security-compliance#KMS]], [[10-security-compliance#Secrets-Manager]] - Identity & encryption
- [[10-security-compliance#VPC]], [[10-security-compliance#PrivateLink]] - Network isolation
- [[10-security-compliance#AWS-WAF]], [[10-security-compliance#AWS-Shield]] - Protection
- [[10-security-compliance#Amazon-Macie]] - Data discovery

### Monitoring & Governance
- [[11-management-governance#CloudWatch]], [[11-management-governance#AWS-X-Ray]] - Monitoring
- [[11-management-governance#CloudTrail]], [[11-management-governance#AWS-Config]] - Auditing
- [[11-management-governance#Trusted-Advisor]], [[11-management-governance#AWS-Budgets]], [[11-management-governance#Cost-Explorer]] - Optimization

---

## Exam Tips
- Focus on **implementation**, not architecture design
- Know when to use each AWS service
- Understand the ML lifecycle and how services fit together
- [[05-sagemaker-algorithms#SageMaker]] is the central hub - know it deeply
- Related certifications: ML Specialty, Data Engineer Associate, AI Practitioner
