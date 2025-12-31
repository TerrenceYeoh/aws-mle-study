# AWS ML Engineer Associate (MLA-C01) - Master Concept Map

## Exam Overview
- **Certification**: AWS Certified Machine Learning Engineer - Associate
- **Exam Code**: MLA-C01
- **Target Experience**: 1 year SageMaker + 1 year software dev/devops/data engineering

---

## ML Lifecycle (AWS Well-Architected ML Lens)

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Process Data│ → │Develop Model│ → │   Deploy    │ → │   Monitor   │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
      │                 │                 │                 │
      ▼                 ▼                 ▼                 ▼
  Sections 2-3      Sections 4-6     Section 9        Section 9,11
```

### Detailed Pipeline Flow:
```
Collect Data → Preprocess Data → Engineer Features → Train/Tune/Evaluate → Deploy → Monitor
     │              │                   │                  │                │        │
     ▼              ▼                   ▼                  ▼                ▼        ▼
   [S3]         [Glue/EMR]      [Feature Store]      [SageMaker]       [ECS/ECR]  [CloudWatch]
                                  ↕         ↕              │
                              Online    Offline            ▼
                              Store     Store        Model Registry
```

---

## Course Structure & Section Dependencies

### Domain 1: Data (Sections 2-3)
```
Section 2: Data Ingestion & Storage
├── Data Types & Formats
├── Data Warehouses vs Lakes vs Lakehouses
├── ETL Pipelines
└── AWS Services: S3, EBS, EFS, FSx, Kinesis
         │
         ▼
Section 3: Data Transformation & Feature Engineering
├── EMR (Elastic MapReduce)
├── Handling: Missing/Unbalanced/Outlier Data
├── Common Transformations
├── SageMaker Data Processing
└── AWS Glue
```

### Domain 2: ML Services & Algorithms (Sections 4-6)
```
Section 4: AWS Managed AI Services
├── NLP: Comprehend, Lex, Textract, Transcribe, Translate
├── Vision: Rekognition
├── Recommendations: Personalize
├── Forecasting: Forecast
├── Speech: Polly
├── Search: Kendra, Q
├── Anomaly: Lookout for Equipment, Fraud Detector
         │
         ▼
Section 5: SageMaker Built-In Algorithms
├── Supervised Learning (Classification/Regression)
├── Unsupervised Learning (Clustering)
├── Deep Learning
└── Algorithm Selection
         │
         ▼
Section 6: Model Training, Tuning & Evaluation
├── Deep Learning Fundamentals
├── Hyperparameter Tuning
├── Model Performance Metrics
└── SageMaker Automatic Model Tuning
```

### Domain 3: Generative AI (Sections 7-8)
```
Section 7: GenAI Fundamentals
├── Transformer Architecture
├── Self-Attention Mechanism
├── How GPT Works
└── SageMaker JumpStart
         │
         ▼
Section 8: Building GenAI Apps with Bedrock
├── Foundation Models
├── RAG (Retrieval-Augmented Generation)
├── Knowledge Bases
├── Vector Stores
├── Guardrails
└── LLM Agents
```

### Domain 4: MLOps (Section 9)
```
Section 9: Machine Learning Operations
├── SageMaker (In-Depth)
│   ├── Pipelines
│   ├── Model Registry
│   └── Endpoints
├── Containers: ECS, ECR
├── Infrastructure as Code: CloudFormation, CDK
├── CI/CD: CodeBuild, CodeDeploy, CodePipeline
├── Orchestration: EventBridge, MWAA (Airflow)
```

### Domain 5: Security & Governance (Sections 10-11)
```
Section 10: Security, Identity & Compliance
├── SageMaker Security
├── IAM (Identity & Access Management)
├── KMS (Key Management)
├── Secrets Manager
├── Network: VPC, PrivateLink
├── Protection: WAF, Shield
└── Data Security: Macie

Section 11: Management & Governance
├── Monitoring: CloudWatch, X-Ray
├── Auditing: CloudTrail, Config
├── Cost: Budgets, Cost Explorer
├── Infrastructure: CloudFormation
└── Recommendations: Trusted Advisor
```

### Domain 6: Best Practices & Exam (Sections 12-13)
```
Section 12: ML Best Practices
└── AWS Well-Architected ML Lens

Section 13: Exam Preparation
├── Practice Questions
└── Exam Tips
```

---

## AWS Services by Category

### Storage
| Service | Purpose | Used In |
|---------|---------|---------|
| S3 | Object storage, data lake | Sections 2, 6, 8, 9 |
| EBS | Block storage for EC2 | Section 2 |
| EFS | Shared file system | Section 2 |
| FSx | High-performance file systems | Section 2 |

### Data Processing
| Service | Purpose | Used In |
|---------|---------|---------|
| Kinesis | Real-time streaming | Section 2 |
| EMR | Big data processing (Spark/Hadoop) | Section 3 |
| Glue | Serverless ETL | Section 3 |

### ML Platform
| Service | Purpose | Used In |
|---------|---------|---------|
| SageMaker | End-to-end ML platform | Sections 3, 5, 6, 7, 9 |
| Bedrock | Foundation models & GenAI | Section 8 |

### AI Services (Pre-trained)
| Service | Purpose | Used In |
|---------|---------|---------|
| Comprehend | NLP/Text analysis | Section 4 |
| Rekognition | Image/Video analysis | Section 4 |
| Textract | Document extraction | Section 4 |
| Transcribe | Speech-to-text | Section 4 |
| Translate | Language translation | Section 4 |
| Polly | Text-to-speech | Section 4 |
| Lex | Conversational AI | Section 4 |
| Personalize | Recommendations | Section 4 |
| Forecast | Time series forecasting | Section 4 |
| Kendra | Enterprise search | Section 4 |
| Q | AI assistant | Section 4 |
| Fraud Detector | Fraud detection | Section 4 |
| Lookout for Equipment | Anomaly detection | Section 4 |

### DevOps/MLOps
| Service | Purpose | Used In |
|---------|---------|---------|
| ECR | Container registry | Section 9 |
| ECS | Container orchestration | Section 9 |
| CodeBuild | Build automation | Section 9 |
| CodeDeploy | Deployment automation | Section 9 |
| CodePipeline | CI/CD pipelines | Section 9 |
| CloudFormation | IaC (JSON/YAML) | Section 9, 11 |
| CDK | IaC (Programming languages) | Section 9 |
| EventBridge | Event-driven automation | Section 9 |
| MWAA | Managed Airflow | Section 9 |

### Security
| Service | Purpose | Used In |
|---------|---------|---------|
| IAM | Access management | Section 10 |
| KMS | Encryption key management | Section 10 |
| Secrets Manager | Secrets storage | Section 10 |
| VPC | Network isolation | Section 10 |
| PrivateLink | Private connectivity | Section 10 |
| WAF | Web application firewall | Section 10 |
| Shield | DDoS protection | Section 10 |
| Macie | Data discovery/protection | Section 10 |

### Monitoring & Governance
| Service | Purpose | Used In |
|---------|---------|---------|
| CloudWatch | Monitoring & logging | Section 11 |
| CloudTrail | API auditing | Section 11 |
| Config | Resource compliance | Section 11 |
| X-Ray | Distributed tracing | Section 11 |
| Trusted Advisor | Best practice checks | Section 11 |
| Budgets | Cost alerts | Section 11 |
| Cost Explorer | Cost analysis | Section 11 |

---

## Cross-Section Concept Links

### SageMaker (Central Hub)
- Data Processing → Section 3
- Built-in Algorithms → Section 5
- Training/Tuning → Section 6
- JumpStart (GenAI) → Section 7
- MLOps/Pipelines → Section 9
- Security → Section 10

### S3 (Data Foundation)
- Raw data storage → Section 2
- Feature Store backend → Section 3
- Model artifacts → Section 6
- Training data → Section 9

### IAM (Access Control)
- SageMaker roles → Sections 9, 10
- Bedrock permissions → Section 8
- Service-to-service access → All sections

---

## Study Path Recommendation

```
Week 1-2: Foundation
├── Section 2: Data Ingestion & Storage
└── Section 3: Data Transformation

Week 3-4: ML Core
├── Section 4: Managed AI Services
├── Section 5: Built-in Algorithms
└── Section 6: Training & Evaluation

Week 5: Generative AI
├── Section 7: GenAI Fundamentals
└── Section 8: Bedrock

Week 6: Operations
└── Section 9: MLOps

Week 7: Security & Governance
├── Section 10: Security
└── Section 11: Management

Week 8: Review & Practice
├── Section 12: Best Practices
└── Section 13: Exam Prep
```
