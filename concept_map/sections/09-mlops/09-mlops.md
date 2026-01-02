# Section 9: Machine Learning Operations (MLOps)

## Overview

This section covers MLOps practices on AWS, including deployment strategies, containerization, CI/CD pipelines, monitoring, and orchestration services for production ML systems.

**Key Takeaways:**
- SageMaker models run in Docker containers with standardized `/opt/ml` structure
- Deployment guardrails enable safe rollouts (Blue/Green, Canary, Linear, Shadow)
- Model Monitor detects data drift, model quality degradation, bias, and feature attribution drift
- Container services (ECS, EKS, Fargate) provide flexible deployment options
- CI/CD with CodePipeline, CodeBuild, CodeDeploy automates ML deployments
- Step Functions and MWAA orchestrate complex ML workflows
- Lake Formation enables secure, governed data lakes

---

## Core Concepts

### Deployment-Safeguards

**Deployment Guardrails:**
- For asynchronous or real-time inference endpoints
- Controls shifting traffic to new models
- Supports auto-rollbacks on failure

**Blue/Green Strategies:**
| Strategy | Description |
|----------|-------------|
| **All at Once** | Shift everything immediately, monitor, terminate blue fleet |
| **Canary** | Shift small portion of traffic first, monitor |
| **Linear** | Shift traffic in linearly spaced steps |

**Shadow Tests:**
- Compare performance of shadow variant to production
- Production traffic mirrored to shadow (no user impact)
- Decide when to promote based on metrics

**Related:** Production-Variants, [[12-ml-best-practices/12-ml-best-practices#SageMaker-Model-Monitor]], [[11-management-governance#CloudWatch]]

---

### SageMaker-Docker

**Key Concept:** All models in SageMaker are hosted in Docker containers

**Pre-built Container Options:**
- Deep learning (TensorFlow, PyTorch, MXNet)
- scikit-learn and Spark ML
- Distributed training via Horovod or Parameter Servers

**Custom Options:**
- Your own training and inference code
- Extend a pre-built image
- Any script/algorithm regardless of runtime or language

**Training Container Structure (`/opt/ml`):**
```
/opt/ml
├── input
│   ├── config
│   │   ├── hyperparameters.json
│   │   └── resourceConfig.json
│   └── data/<channel_name>/<input data>
├── model
├── code/<script files>
└── output/failure
```

**Deployment Container:**
```
/opt/ml
└── model/<model files>
```

**Related:** [[09-mlops/09-mlops#ECR]], SageMaker-Containers-Library

---

### SageMaker-Containers-Library

**Purpose:** Make containers compatible with SageMaker

**Installation:** `RUN pip install sagemaker-containers` in Dockerfile

**Key Environment Variables:**
| Variable | Purpose |
|----------|---------|
| SAGEMAKER_PROGRAM | Script to run inside /opt/ml/code |
| SM_MODEL_DIR | Model directory |
| SM_CHANNELS / SM_CHANNEL_* | Data channels |
| SM_HPS / SM_HP_* | Hyperparameters |

**Related:** [[09-mlops/09-mlops#Docker]], [[09-mlops/09-mlops#ECR]]

---

### Production-Variants

**Purpose:** Test multiple models on live traffic (A/B testing)

**Features:**
- Variant Weights distribute traffic among variants
- Roll out new model at 10%, ramp to 100% when confident
- Offline validation isn't always sufficient

**Related:** Shadow-Tests, Deployment-Guardrails

---

### SageMaker-Neo

**Purpose:** Train once, run anywhere (edge optimization)

**Target Devices:**
- ARM, Intel, Nvidia processors
- Embedded devices (cars, IoT)

**Supported Frameworks:**
- TensorFlow, MXNet, PyTorch, ONNX
- XGBoost, DarkNet, Keras

**Components:**
- **Compiler:** Optimizes code for specific devices
- **Runtime:** Executes optimized model

**Deployment:**
- HTTPS endpoint (must match compilation instance type)
- **IoT Greengrass** for actual edge devices

**Related:** IoT-Greengrass, Edge-Deployment

---

### Inference-Types

| Type | Description | Best For |
|------|-------------|----------|
| **Real-time** | Interactive, low latency | User-facing applications |
| **Serverless** | Auto-scales, scales to zero | Infrequent/unpredictable traffic |
| **Asynchronous** | Queue requests, up to 1GB payloads | Large payloads, long processing |

**Serverless Inference:**
- Specify container, memory, concurrency
- Scales down to zero (cold starts possible)
- CloudWatch metrics: ModelSetupTime, Invocations, MemoryUtilization

**Related:** SageMaker-Endpoints, [[06-model-training/06-model-training#Auto-Scaling]]

---

### SageMaker-Inference-Recommender

**Purpose:** Recommend optimal instance type & configuration

**How It Works:**
1. Register model to model registry
2. Benchmark different endpoint configurations
3. Collect & visualize metrics
4. Deploy to optimal endpoint

**Recommendation Types:**
| Type | Duration | Description |
|------|----------|-------------|
| **Instance Recommendations** | ~45 min | Load tests on recommended types |
| **Endpoint Recommendations** | ~2 hours | Custom load test with your requirements |

**Related:** [[09-mlops/09-mlops#Model-Registry]], Instance-Types

---

### Inference-Pipelines

**Definition:** Linear sequence of 2-15 containers

**Features:**
- Pre-processing → Predictions → Post-processing
- Supports Spark ML (MLeap format) and scikit-learn
- Works with real-time and batch transforms

**Related:** Batch-Transform, Feature-Engineering

---

### SageMaker-Model-Monitor

**Purpose:** Monitor deployed models for quality deviations

**Monitoring Types:**
| Type | Description |
|------|-------------|
| **Data Quality Drift** | Compare to baseline statistical properties |
| **Model Quality Drift** | Compare accuracy to baseline |
| **Bias Drift** | Monitor for emerging bias |
| **Feature Attribution Drift** | NDCG score (training vs live feature ranking) |

**Infrastructure:**
- Data stored in S3 (secured)
- Monitoring jobs via Monitoring Schedule
- Metrics emitted to CloudWatch
- Corrective action: retrain model, audit data

**Data Capture:**
- Logs endpoint inputs and inference outputs
- Data delivered to S3 as JSON
- Supports encryption

**Visualization:** Tensorboard, QuickSight, Tableau, SageMaker Studio

**Related:** [[12-ml-best-practices#SageMaker-Clarify]], [[11-management-governance#CloudWatch]], Data-Drift

---

### SageMaker-Clarify

**Purpose:** Detect bias and explain model behavior

**Capabilities:**
- Detect potential bias (imbalances across groups)
- Monitor for bias with CloudWatch alerts
- Explain model behavior (feature importance)

**Pre-training Bias Metrics:**
| Metric | Abbreviation | Description |
|--------|--------------|-------------|
| Class Imbalance | CI | One group has fewer training values |
| Difference in Proportions of Labels | DPL | Imbalance of positive outcomes |
| Kullback-Leibler Divergence | KL | How much outcome distributions diverge |
| Jensen-Shannon Divergence | JS | Symmetric version of KL |
| Kolmogorov-Smirnov | KS | Maximum divergence between distributions |
| Conditional Demographic Disparity | CDD | Disparity by subgroups |

**Related:** [[12-ml-best-practices/12-ml-best-practices#SageMaker-Model-Monitor]], Fairness, Explainability

---

### SageMaker-Projects

**Purpose:** SageMaker Studio's native MLOps solution with CI/CD

**Capabilities:**
- Build images, prep data, feature engineering
- Train, evaluate, deploy models
- Monitor & update models

**Components:**
- Code repositories for building/deploying
- SageMaker Pipelines defining steps
- Model Registry
- EventBridge for triggers
- CodePipeline for model build/deploy
- CloudFormation for endpoint deployment

**Related:** [[09-mlops/09-mlops]], [[09-mlops/09-mlops#CI-CD]], [[09-mlops/09-mlops#Model-Registry]]

---

## AWS Services

### Amazon-ECS

**Amazon Elastic Container Service**

**Launch Types:**
| Type | Description |
|------|-------------|
| **EC2 Launch Type** | You provision EC2 instances with ECS Agent |
| **Fargate Launch Type** | Serverless, just define tasks |

**IAM Roles:**
- **EC2 Instance Profile:** ECS agent, pull images, CloudWatch logs
- **ECS Task Role:** Per-task permissions, defined in task definition

**Load Balancer Integrations:**
- Application Load Balancer (recommended)
- Network Load Balancer (high throughput)
- Classic Load Balancer (legacy, no Fargate)

**Data Volumes:**
- Mount EFS onto ECS tasks (both EC2 and Fargate)
- **Fargate + EFS = Serverless**
- S3 cannot be mounted as file system

**Related:** [[09-mlops/09-mlops#Fargate]], [[09-mlops#ECR]], [[09-mlops/09-mlops#EKS]]

---

### Amazon-EKS

**Amazon Elastic Kubernetes Service**

**Key Points:**
- Managed Kubernetes clusters on AWS
- Alternative to ECS (different API, same goal)
- Cloud-agnostic (works on any cloud)
- One EKS cluster per region for multi-region

**Node Types:**
| Type | Description |
|------|-------------|
| **Managed Node Groups** | EKS creates/manages nodes, part of ASG |
| **Self-Managed Nodes** | You create/register, use EKS Optimized AMI |
| **AWS Fargate** | No maintenance, no nodes managed |

**Data Volumes:** EBS, EFS (Fargate), FSx for Lustre, FSx for NetApp ONTAP

**Related:** Kubernetes, [[09-mlops#ECS]], [[09-mlops/09-mlops#Fargate]]

---

### Amazon-ECR

**Elastic Container Registry**

**Features:**
- Store and manage Docker images on AWS
- Private and Public repositories
- Fully integrated with ECS, backed by S3
- Image vulnerability scanning, versioning, lifecycle

**Access:** Controlled through IAM (permission errors → check policy)

**Related:** [[09-mlops/09-mlops#Docker]], [[09-mlops#ECS]], [[09-mlops/09-mlops#EKS]]

---

### AWS-Batch

**Purpose:** Run batch jobs as Docker images

**Features:**
- Dynamic provisioning (EC2 & Spot instances)
- Optimal quantity/type based on volume
- Fully serverless (no cluster management)
- Pay only for underlying EC2 instances

**Integration:**
- Schedule with CloudWatch Events
- Orchestrate with Step Functions

**Related:** [[09-mlops#Step-Functions]], [[03-data-transformation#AWS-Glue]]

---

### AWS-CloudFormation

**Purpose:** Declarative Infrastructure as Code

**Benefits:**
- No manual resource creation
- Changes reviewed through code
- Resources tagged with stack identifier
- Automated diagram generation (Infrastructure Composer)

**Features:**
- Supports most AWS resources
- "Custom resources" for unsupported
- Delete/recreate infrastructure on the fly

**Related:** [[09-mlops#CDK]], Infrastructure-as-Code

---

### AWS-CDK

**Cloud Development Kit**

**Purpose:** Define infrastructure using programming languages

**Supported Languages:** JavaScript/TypeScript, Python, Java, .NET

**Key Concepts:**
- **Constructs:** High-level components
- Compiles to CloudFormation template
- Deploy infrastructure AND application code together

**Workflow:**
```
CDK Application → cdk synth → CloudFormation Template → Deploy
```

**Related:** [[09-mlops#CloudFormation]], SAM

---

### AWS-CodePipeline

**Purpose:** Orchestrate CI/CD for automatic deployment

**Pipeline Flow:**
```
Code → Build → Test → Provision → Deploy
```

**Integrations:**
- CodeCommit, CodeBuild, CodeDeploy
- Elastic Beanstalk, CloudFormation
- GitHub, 3rd-party services

**Related Services:**
- **CodeBuild:** Compile, test, produce packages (serverless)
- **CodeDeploy:** Deploy to EC2/on-premises (needs agent)

**Related:** [[09-mlops/09-mlops#CI-CD]], [[09-mlops#CodeBuild]], [[09-mlops#CodeDeploy]]

---

### Amazon-EventBridge

**Formerly:** CloudWatch Events

**Purpose:** Serverless event bus for event-driven architectures

**Trigger Types:**
| Type | Description |
|------|-------------|
| **Schedule** | Cron jobs |
| **Event Pattern** | React to service events |

**Event Sources:** EC2 state changes, CodeBuild, S3, CloudTrail, Trusted Advisor

**Destinations:**
| Category | Services |
|----------|----------|
| **Compute** | Lambda, Batch, ECS Task |
| **Integration** | SQS, SNS, Kinesis |
| **Orchestration** | Step Functions, CodePipeline |

**Features:**
- Cross-account access via Resource-based Policies
- Archive events, replay archived events
- Schema Registry (auto-infer schema, versioning)

**Related:** [[09-mlops#Step-Functions]], [[09-mlops#AWS-Lambda]], Event-Driven

---

### AWS-Step-Functions

**Purpose:** Design and execute workflows as state machines

**Benefits:**
- Easy visualizations
- Advanced error handling and retry
- Workflow history audit
- **Max execution time: 1 year**

**State Types:**
| State | Purpose |
|-------|---------|
| **Task** | Execute Lambda, AWS services, 3rd party APIs |
| **Choice** | Conditional logic |
| **Wait** | Delay for specified time |
| **Parallel** | Separate branches of execution |
| **Map** | Run steps for each item (data engineering) |
| **Pass/Succeed/Fail** | Flow control |

**ML Use Cases:**
- Train/tune ML models
- Manage Batch jobs
- Process datasets in parallel (Map state)

**Related:** [[09-mlops#MWAA]], [[09-mlops#AWS-Lambda]], [[09-mlops/09-mlops#Orchestration]]

---

### Amazon-MWAA

**Managed Workflows for Apache Airflow**

**Apache Airflow:**
- Batch-oriented workflow tool
- Workflows as Python code (DAGs - Directed Acyclic Graphs)

**Amazon MWAA Features:**
- Managed service (no installation/maintenance)
- DAGs uploaded to S3
- Runs within VPC (2+ AZs)
- Automatic scaling (Fargate containers)

**Use Cases:**
- Complex workflows
- ETL coordination
- Preparing ML data

**Integrations:** Athena, Batch, EMR, Glue, Lambda, Redshift, SageMaker, S3

**Related:** [[09-mlops#Step-Functions]], ETL, [[09-mlops/09-mlops#Orchestration]]

---

### AWS-Lake-Formation

**Purpose:** Set up secure data lakes in days

**Capabilities:**
- Load data, monitor data flows
- Set up partitions, encryption
- Define transformation jobs
- Access control, auditing

**Built On:** AWS Glue

**Data Sources:** S3, RDBMS, NoSQL (on-premises or AWS)

**Query Services:** Athena, Redshift, EMR

**Pricing:** Free (underlying services charged)

**Security Features:**
- Cross-account permissions via AWS RAM
- **Governed Tables:** ACID transactions, streaming support
- **Data Filters:** Row-level, column-level, cell-level security

**Related:** [[03-data-transformation#AWS-Glue]], Data-Lake, Data-Governance

---

## Concept Relationships

```
                    ┌─────────────────────────────────────────────┐
                    │              SAGEMAKER MLOPS                 │
                    └─────────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   Training    │               │  Deployment   │               │  Monitoring   │
│  Containers   │               │  Strategies   │               │   & Drift     │
└───────────────┘               └───────────────┘               └───────────────┘
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│ /opt/ml       │               │ Blue/Green    │               │ Model Monitor │
│ structure     │               │ Canary/Linear │               │ + Clarify     │
│ ECR storage   │               │ Shadow Tests  │               │ Data Drift    │
└───────────────┘               └───────────────┘               └───────────────┘


                    ┌─────────────────────────────────────────────┐
                    │           AWS CONTAINER SERVICES             │
                    └─────────────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┼───────────────────────────────┐
        │                               │                               │
        ▼                               ▼                               ▼
┌───────────────┐               ┌───────────────┐               ┌───────────────┐
│   Amazon ECS  │               │  Amazon EKS   │               │  AWS Fargate  │
│ AWS Container │               │  Kubernetes   │               │  Serverless   │
└───────────────┘               └───────────────┘               └───────────────┘
        │                               │                               │
        └───────────────────────────────┴───────────────────────────────┘
                                        │
                                        ▼
                                ┌───────────────┐
                                │  Amazon ECR   │
                                │ Image Storage │
                                └───────────────┘


                    ┌─────────────────────────────────────────────┐
                    │               CI/CD PIPELINE                 │
                    └─────────────────────────────────────────────┘

    ┌─────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
    │  Code   │ → │  CodeBuild  │ → │ CodeDeploy  │ → │  Endpoint   │
    │ (Git)   │   │  (Build)    │   │  (Deploy)   │   │(Production) │
    └─────────┘   └─────────────┘   └─────────────┘   └─────────────┘
         │                                                    │
         └────────────────────────────────────────────────────┘
                        CodePipeline (Orchestration)


                    ┌─────────────────────────────────────────────┐
                    │           WORKFLOW ORCHESTRATION             │
                    └─────────────────────────────────────────────┘
                                        │
                ┌───────────────────────┴───────────────────────┐
                │                                               │
                ▼                                               ▼
        ┌───────────────┐                               ┌───────────────┐
        │Step Functions │                               │     MWAA      │
        │ State Machine │                               │  Apache DAGs  │
        └───────────────┘                               └───────────────┘
                │                                               │
                │  Trigger via                                  │
                └──────────────► EventBridge ◄──────────────────┘
```

---

## Exam Tips

### Deployment & Containers
- All SageMaker models run in Docker containers with `/opt/ml` structure
- Use `sagemaker-containers` library to make custom containers compatible
- ECR stores Docker images; IAM controls access
- Deployment Guardrails: All at Once, Canary, Linear strategies
- Shadow Tests compare new model to production without affecting users

### Inference Options
- **Real-time:** Low latency, user-facing
- **Serverless:** Scales to zero, infrequent traffic
- **Asynchronous:** Large payloads up to 1GB
- Inference Pipelines: 2-15 containers in sequence
- Inference Recommender benchmarks instance types

### Model Monitoring
- Model Monitor detects: Data Quality, Model Quality, Bias, Feature Attribution drift
- Clarify provides pre-training bias metrics and explainability
- Data Capture logs inputs/outputs to S3 as JSON
- Corrective action: retrain model or audit data

### Container Services
- **ECS:** AWS native, EC2 or Fargate launch types
- **EKS:** Kubernetes (cloud-agnostic), Managed/Self-Managed/Fargate nodes
- **Fargate:** Serverless containers (works with both ECS and EKS)
- ECS Task Role vs EC2 Instance Profile for IAM
- EFS can be mounted (Fargate + EFS = serverless), S3 cannot

### CI/CD & Infrastructure
- CodePipeline orchestrates: Code → Build → Test → Deploy
- CodeBuild is serverless; CodeDeploy needs agent
- CloudFormation = declarative IaC (YAML/JSON)
- CDK = imperative IaC (Python, JS, Java, .NET) → compiles to CloudFormation

### Orchestration
- Step Functions: State machines, max 1 year execution, Map state for parallel data
- MWAA: Managed Airflow, DAGs in Python, stored in S3
- EventBridge: Event-driven triggers, schedules, cross-account access
- AWS Batch: Docker jobs, dynamic EC2/Spot provisioning

### Data Lake & Governance
- Lake Formation: Secure data lakes built on Glue
- Governed Tables: ACID transactions
- Data Filters: Row, column, or cell-level security
- Lake Formation itself is free (underlying services charged)

### Instance Selection
- Training (Deep Learning): GPU instances (P3, g4dn)
- Inference: Compute instances (C5) usually sufficient
- Managed Spot Training: Up to 90% savings, use checkpoints

### Git Workflows
- Git Flow: Main, Develop, Feature, Release, Hotfix branches
- GitHub Flow: Simpler, just Main and Feature branches
