# Section 9: Machine Learning Operations (MLOps) - Comparison Tables

## Deployment Strategies

### Blue/Green Deployment Options

| Strategy | Traffic Shift | Risk Level | Use Case |
|----------|---------------|------------|----------|
| **All at Once** | 100% immediately | Highest | Fast rollout, confident in new model |
| **Canary** | Small % first | Low | Test with subset before full rollout |
| **Linear** | Gradual steps | Medium | Controlled, measured rollout |
| **Shadow** | 0% (mirrored) | None | Compare performance without impact |

---

## Inference Types

### SageMaker Inference Options

| Aspect | Real-time | Serverless | Asynchronous |
|--------|-----------|------------|--------------|
| **Latency** | Lowest | Cold starts possible | Highest |
| **Max Payload** | 6 MB | 6 MB | 1 GB |
| **Scaling** | Manual/Auto | Auto (to zero) | Queue-based |
| **Best For** | User-facing apps | Infrequent traffic | Large files, long processing |
| **Cost Model** | Per hour | Per request | Per request |

---

## Container Services

### ECS vs EKS vs Fargate

| Aspect | ECS | EKS | Fargate |
|--------|-----|-----|---------|
| **Type** | AWS container platform | Managed Kubernetes | Serverless compute |
| **API** | AWS native | Kubernetes API | N/A (runs on ECS/EKS) |
| **Portability** | AWS only | Cloud-agnostic | AWS only |
| **Management** | Less complex | More complex | Minimal |
| **Best For** | AWS-native apps | K8s workloads, multi-cloud | No infrastructure management |

### ECS Launch Types

| Aspect | EC2 Launch Type | Fargate Launch Type |
|--------|-----------------|---------------------|
| **Infrastructure** | You provision EC2 instances | No infrastructure to manage |
| **Scaling** | Manage instance scaling | Scale by task count |
| **Maintenance** | You maintain EC2 instances | Fully serverless |
| **ECS Agent** | You install/manage | Automatic |
| **Cost** | EC2 pricing | Per task (vCPU + memory) |
| **Best For** | Control over infrastructure | Simplicity, no ops |

### EKS Node Types

| Node Type | Management | Scaling | Best For |
|-----------|------------|---------|----------|
| **Managed Node Groups** | EKS creates/manages | Part of ASG | Recommended default |
| **Self-Managed Nodes** | You create/register | You manage | Custom AMIs, specific config |
| **AWS Fargate** | No nodes to manage | Automatic | Serverless K8s workloads |

### ECS IAM Roles

| Role | Scope | Purpose | Used By |
|------|-------|---------|---------|
| **EC2 Instance Profile** | Instance-level | ECS agent operations | ECS agent (EC2 launch type) |
| **ECS Task Role** | Task-level | Task-specific permissions | Individual containers |

**Instance Profile Permissions:**
- Make API calls to ECS service
- Send logs to CloudWatch
- Pull images from ECR
- Access Secrets Manager / SSM Parameter Store

---

## Container Storage Options

### ECS/EKS Data Volumes

| Storage | ECS (EC2) | ECS (Fargate) | EKS |
|---------|-----------|---------------|-----|
| **EFS** | Yes | Yes | Yes (recommended with Fargate) |
| **EBS** | Yes | No | Yes |
| **FSx for Lustre** | Yes | No | Yes |
| **S3 (mounted)** | No | No | No |

---

## AWS Batch vs Glue

| Aspect | AWS Glue | AWS Batch |
|--------|----------|-----------|
| **Focus** | ETL (Apache Spark) | Any computing job |
| **Runtime** | Managed Spark | Docker containers |
| **Languages** | Scala, Python | Any (Docker image) |
| **Resources** | Fully managed | Created in your account |
| **Serverless** | Yes | Yes (dynamic provisioning) |
| **Best For** | ETL, Data Catalog | Non-ETL batch processing |
| **Integration** | Athena, Redshift Spectrum | CloudWatch Events, Step Functions |

---

## Infrastructure as Code

### CloudFormation vs CDK vs SAM

| Aspect | CloudFormation | CDK | SAM |
|--------|----------------|-----|-----|
| **Language** | YAML/JSON (declarative) | Python, JS, Java, .NET | YAML/JSON |
| **Abstraction** | Low-level | High-level constructs | Serverless-focused |
| **Output** | Direct deployment | Compiles to CloudFormation | Extends CloudFormation |
| **Best For** | Any AWS resource | Complex infrastructure | Lambda, API Gateway |
| **Learning Curve** | Moderate | Varies by language | Low (serverless) |

### CDK vs SAM Decision

| Question | Answer |
|----------|--------|
| Building Lambda functions quickly? | SAM |
| Need all AWS services? | CDK |
| Prefer programming languages? | CDK |
| Need local testing? | Both (SAM CLI for both) |
| Complex infrastructure with code? | CDK |

---

## CI/CD Services

### CodeBuild vs CodeDeploy vs CodePipeline

| Service | Purpose | Type | Notes |
|---------|---------|------|-------|
| **CodeBuild** | Build & test code | Serverless | Compiles, runs tests, produces packages |
| **CodeDeploy** | Deploy applications | Agent-based | EC2, on-premises (needs agent) |
| **CodePipeline** | Orchestrate CI/CD | Orchestrator | Connects all stages |

---

## Git Branching Strategies

### Git Flow vs GitHub Flow

| Aspect | Git Flow | GitHub Flow |
|--------|----------|-------------|
| **Branches** | Main, Develop, Feature, Release, Hotfix | Main, Feature |
| **Complexity** | More complex | Simpler |
| **Release Cadence** | Planned releases | Continuous |
| **Best For** | Scrum teams, versioned releases | Rapid deployment |
| **Hotfixes** | Dedicated branch | Feature branch |

---

## Workflow Orchestration

### Step Functions vs MWAA vs EventBridge

| Aspect | Step Functions | MWAA (Airflow) | EventBridge |
|--------|----------------|----------------|-------------|
| **Type** | State machine | DAG workflows | Event bus |
| **Definition** | JSON (ASL) | Python code | Rules/patterns |
| **Max Duration** | 1 year | Unlimited | Instant (trigger) |
| **Best For** | AWS service orchestration | Complex ETL, ML pipelines | Event-driven triggers |
| **Visual Designer** | Yes | Airflow UI | No |
| **Scheduling** | Via EventBridge | Built-in scheduler | Native |

### Step Functions State Types

| State | Purpose | Use Case |
|-------|---------|----------|
| **Task** | Execute work | Lambda, API calls |
| **Choice** | Conditional logic | If/else branching |
| **Wait** | Delay execution | Time-based waits |
| **Parallel** | Concurrent branches | Independent tasks |
| **Map** | Iterate over items | Data processing (most relevant for ML) |
| **Pass** | Pass data through | Transform data |
| **Succeed/Fail** | Terminal states | End workflow |

---

## Model Monitoring

### Model Monitor Types

| Monitor Type | What It Detects | Baseline |
|--------------|-----------------|----------|
| **Data Quality** | Input data drift | Statistical properties |
| **Model Quality** | Accuracy degradation | Model metrics |
| **Bias Drift** | Emerging bias | Fairness metrics |
| **Feature Attribution** | Feature importance changes | NDCG score |

### Clarify Bias Metrics

| Metric | Abbreviation | What It Measures |
|--------|--------------|------------------|
| Class Imbalance | CI | Training data balance |
| Difference in Proportions of Labels | DPL | Outcome balance |
| Kullback-Leibler Divergence | KL | Distribution divergence |
| Jensen-Shannon Divergence | JS | Symmetric KL |
| Kolmogorov-Smirnov | KS | Max distribution difference |
| Conditional Demographic Disparity | CDD | Subgroup disparity |

---

## Instance Selection

### Training vs Inference Instances

| Use Case | Recommended Instance | Reason |
|----------|---------------------|--------|
| **Deep Learning Training** | GPU (P3, g4dn) | Parallel computation |
| **Inference** | Compute (C5) | Less demanding |
| **Cost-Sensitive Training** | Spot Instances | Up to 90% savings |

---

## SageMaker Neo Deployment

### Neo Deployment Options

| Target | Method | Notes |
|--------|--------|-------|
| **Cloud Endpoint** | HTTPS (C5, M5, P3, etc.) | Must match compilation instance |
| **Edge Device** | IoT Greengrass | Lambda inference apps |

---

## Lake Formation Security

### Data Filter Security Levels

| Configuration | Security Level | Controls |
|---------------|----------------|----------|
| All columns + row filter | Row-level | Which rows visible |
| All rows + specific columns | Column-level | Which columns visible |
| Specific columns + specific rows | Cell-level | Most granular |

### Lake Formation vs Standard IAM

| Aspect | Standard IAM/S3 | Lake Formation |
|--------|-----------------|----------------|
| **Granularity** | Bucket/prefix level | Row/column/cell level |
| **Central Management** | Per-service | Single location |
| **ACID Transactions** | No | Yes (Governed Tables) |
| **Cross-Account** | Complex | Built-in (via RAM) |

---

## Quick Decision Tables

### Which Container Service?

| Question | Answer |
|----------|--------|
| AWS-native, simple? | ECS |
| Kubernetes workloads? | EKS |
| No infrastructure management? | Fargate |
| Multi-cloud portability needed? | EKS |
| Running Docker images? | Any |

### Which Orchestration Service?

| Question | Answer |
|----------|--------|
| AWS service orchestration? | Step Functions |
| Complex Python workflows? | MWAA |
| Event-driven triggers? | EventBridge |
| Data parallel processing? | Step Functions (Map state) |
| Need visual workflow designer? | Step Functions |

### Which Deployment Strategy?

| Question | Answer |
|----------|--------|
| Fast rollout, high confidence? | All at Once |
| Test with small traffic first? | Canary |
| Gradual, controlled rollout? | Linear |
| Compare without user impact? | Shadow |
| Need auto-rollback? | Any with Deployment Guardrails |

### Which IaC Tool?

| Question | Answer |
|----------|--------|
| YAML/JSON preference? | CloudFormation or SAM |
| Programming language preference? | CDK |
| Serverless-focused? | SAM |
| All AWS services? | CloudFormation or CDK |
| High-level abstractions? | CDK |

### Which Inference Type?

| Question | Answer |
|----------|--------|
| User-facing, low latency? | Real-time |
| Infrequent, unpredictable traffic? | Serverless |
| Large payloads (>6 MB)? | Asynchronous |
| Scales to zero needed? | Serverless |
| Long processing time? | Asynchronous |

### Which Monitoring Type?

| Question | Answer |
|----------|--------|
| Input data changing? | Data Quality Monitor |
| Model accuracy dropping? | Model Quality Monitor |
| Fairness concerns? | Bias Drift Monitor |
| Feature importance changing? | Feature Attribution Monitor |
| Need explainability? | SageMaker Clarify |

### Which Load Balancer for ECS?

| Question | Answer |
|----------|--------|
| Most use cases? | Application Load Balancer |
| High throughput needed? | Network Load Balancer |
| AWS PrivateLink? | Network Load Balancer |
| Using Fargate? | ALB or NLB (not Classic) |
