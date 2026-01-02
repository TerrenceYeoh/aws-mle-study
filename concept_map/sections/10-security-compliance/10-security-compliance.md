# Section 10: Security, Identity, and Compliance - Concept Map

## Overview

This section covers AWS security fundamentals for ML workloads, including identity management (IAM), encryption (KMS), network security (VPC, WAF, Shield), and data protection strategies. Key focus areas include securing SageMaker resources and understanding the shared responsibility model.

**Key Takeaways:**
- Apply **Principle of Least Privilege** everywhere
- Encrypt data **at rest** (KMS) and **in transit** (TLS/SSL)
- Use **VPC** for network isolation of ML resources
- Monitor with **CloudWatch** and audit with **CloudTrail**
- Protect web applications with **WAF** and **Shield**

---

## Core Concepts

### Principle-of-Least-Privilege
- **Definition:** Grant only the permissions required to perform a task
- **Best Practices:**
  - Start broad while developing, lock down once requirements clear
  - Use **IAM Access Analyzer** to generate least-privilege policies
- **Implementation:**
  - Specific bucket ARNs (not wildcards)
  - Condition keys (e.g., `s3:prefix` for path restrictions)
  - Specific actions (e.g., `s3:GetObject`, `s3:GetObjectVersion`)
- Related: [[10-security-compliance#IAM]], [[10-security-compliance/10-security-compliance#IAM-Policies]]

### Data-Masking-and-Anonymization
- **Data Masking:** Obfuscates sensitive data (PII)
  - Example: Show only last 4 digits of SSN/credit card
  - Supported in: **Glue DataBrew**, **Redshift**
- **Anonymization Techniques:**
  - Replace with random values
  - Shuffle values
  - Encrypt (deterministic or probabilistic)
  - Hash (one-way transformation)
  - Delete/don't import
- Related: Glue-DataBrew, [[10-security-compliance#Amazon-Macie]]

### Encryption-at-Rest
- Data encrypted when stored on disk
- **AWS KMS** manages encryption keys
- Server decrypts before sending data back
- Related: [[10-security-compliance#KMS]], S3-Encryption

### Encryption-in-Transit
- Data encrypted before sending, decrypted after receiving
- **TLS certificates** enable HTTPS
- Prevents **Man-in-the-Middle (MITM)** attacks
- Related: TLS-SSL

### Client-Side-Encryption
- Data encrypted by client before sending
- Server never decrypts the data
- May use **Envelope Encryption**
- Related: [[10-security-compliance#KMS]]

---

## AWS Services

### IAM (Identity and Access Management)
- **Purpose:** Global service for managing users, groups, and permissions
- **Key Components:**
  - **Root Account:** Created by default - never use or share
  - **Users:** People within organization
  - **Groups:** Contain only users (not other groups)
  - **Roles:** Allow AWS services to act on your behalf
  - **Policies:** JSON documents defining permissions
- **Common SageMaker Permissions:**
  - CreateTrainingJob, CreateModel, CreateEndpointConfig
  - CreateTransformJob, CreateHyperParameterTuningJob
  - CreateNotebookInstance, UpdateNotebookInstance
- **Predefined Policies:**
  - AmazonSageMakerReadOnly
  - AmazonSageMakerFullAccess
  - DataScientist
  - AdministratorAccess
- Related: [[10-security-compliance/10-security-compliance#IAM-Policies]], IAM-Roles

### IAM-Policies
- **Structure:**
  | Element | Required | Description |
  |---------|----------|-------------|
  | Version | Yes | Policy language version ("2012-10-17") |
  | Statement | Yes | One or more statements |
  | Effect | Yes | Allow or Deny |
  | Action | Yes | List of actions allowed/denied |
  | Resource | Yes | Resources actions apply to |
  | Principal | Depends | Account/user/role this applies to |
  | Condition | No | When policy is in effect |
- **Inheritance:** Users inherit from groups; can also have inline policies
- Related: [[10-security-compliance#IAM]], Principle-of-Least-Privilege

### MFA (Multi-Factor Authentication)
- **Definition:** Password you know + security device you own
- **Purpose:** Protect Root and IAM users from credential theft
- **Device Options:**
  - Virtual MFA (Google Authenticator, Authy)
  - U2F Security Key (YubiKey)
  - Hardware Key Fob (Gemalto)
  - GovCloud Key Fob (SurePassID)
- Related: [[10-security-compliance#IAM]], Password-Policy

### KMS (Key Management Service)
- **Purpose:** Centralized encryption key management
- **Integration:** EBS, S3, RDS, SSM, SageMaker
- **Key Types:**
  - **Symmetric (AES-256):** Single key for encrypt/decrypt
  - **Asymmetric (RSA/ECC):** Public/private key pair
- **Key Categories:**
  | Type | Cost | Rotation |
  |------|------|----------|
  | AWS Owned | Free | Automatic |
  | AWS Managed (aws/service-name) | Free | Auto every 1 year |
  | Customer Managed (created in KMS) | $1/month | Must enable |
  | Customer Managed (imported) | $1/month | Manual only |
- **Key Policies:** Control access to keys (like S3 bucket policies)
- **Cross-Region:** Keys are regional; must re-encrypt when copying snapshots
- Related: Encryption-at-Rest, [[02-data-ingestion#Amazon-S3]]

### Secrets-Manager
- **Purpose:** Store and manage secrets (especially RDS credentials)
- **Features:**
  - Force rotation every X days
  - Auto-generate secrets on rotation (Lambda)
  - Native RDS integration (MySQL, PostgreSQL, Aurora)
  - Encrypted using KMS
- **Multi-Region:**
  - Replicate secrets across regions
  - Keep read replicas in sync
  - Promote replica to standalone
- **Use Cases:** Multi-region apps, disaster recovery
- Related: [[10-security-compliance#KMS]], RDS

### Macie
- **Purpose:** Data security and privacy service for S3
- **Capabilities:**
  - Uses ML and pattern matching
  - Discovers and protects sensitive data
  - Identifies **PII** (Personally Identifiable Information)
- **Integration:** Alerts via Amazon EventBridge
- **Flow:** S3 Buckets → Macie (analyze) → EventBridge (notify)
- Related: [[02-data-ingestion#Amazon-S3]], [[09-mlops#EventBridge]]

### WAF (Web Application Firewall)
- **Purpose:** Protect web applications from Layer 7 (HTTP) exploits
- **Deployment Targets:**
  - Application Load Balancer
  - API Gateway
  - CloudFront
  - AppSync GraphQL API
  - Cognito User Pool
- **Web ACL Rules:**
  - IP Set (up to 10,000 IPs)
  - HTTP inspection (headers, body, URI)
  - SQL injection/XSS protection
  - Size constraints
  - Geo-match (block countries)
  - Rate-based (DDoS protection)
- **Notes:**
  - Web ACLs are Regional (except CloudFront)
  - Does NOT support Network Load Balancer
  - Use Global Accelerator for fixed IP + WAF on ALB
- Related: [[10-security-compliance#AWS-Shield]], ALB, CloudFront

### Shield
- **Purpose:** DDoS (Distributed Denial of Service) protection
- **Shield Standard (Free):**
  - Activated for all AWS customers
  - Protects from SYN/UDP floods, reflection attacks
  - Layer 3/Layer 4 protection
- **Shield Advanced ($3,000/month/org):**
  - More sophisticated attack protection
  - Protects: EC2, ELB, CloudFront, Global Accelerator, Route 53
  - 24/7 DDoS Response Team (DRP)
  - Cost protection against DDoS usage spikes
  - Auto-deploys WAF rules for Layer 7 attacks
- Related: [[10-security-compliance#AWS-WAF]], CloudFront

### VPC (Virtual Private Cloud)
- **Purpose:** Private network for deploying resources
- **Scope:** Regional resource
- **Subnets:**
  - Partition network inside VPC
  - Availability Zone resource
  - **Public Subnet:** Accessible from internet
  - **Private Subnet:** Not accessible from internet
- **Route Tables:** Define access to internet and between subnets
- Related: Subnets, [[10-security-compliance/10-security-compliance#Security-Groups]], [[10-security-compliance/10-security-compliance#NACL]]

### Internet-Gateway
- Connects VPC instances to internet
- Public subnets have route to IGW
- Related: [[10-security-compliance#VPC]], NAT-Gateway

### NAT-Gateway
- **Purpose:** Allow private subnet instances to access internet
- Instances remain private (no inbound from internet)
- AWS-managed (vs self-managed NAT Instance)
- Related: [[10-security-compliance#VPC]], Internet-Gateway

### Security-Groups
- **Level:** Instance level (ENI)
- **Rules:** Allow only (no deny rules)
- **Stateful:** Return traffic auto-allowed
- **Evaluation:** All rules evaluated
- Related: [[10-security-compliance/10-security-compliance#NACL]], [[10-security-compliance#VPC]]

### NACL (Network ACL)
- **Level:** Subnet level
- **Rules:** Allow AND Deny
- **Stateless:** Must explicitly allow return traffic
- **Evaluation:** Rules in number order
- **Association:** Auto-applies to all instances in subnet
- Related: [[10-security-compliance/10-security-compliance#Security-Groups]], [[10-security-compliance#VPC]]

### VPC-Flow-Logs
- **Purpose:** Capture IP traffic information
- **Levels:** VPC, Subnet, or ENI
- **Captures:** ELB, RDS, Aurora, ElastiCache, etc.
- **Destinations:** S3, CloudWatch Logs, Kinesis Data Firehose
- Related: [[10-security-compliance#VPC]], [[11-management-governance#CloudWatch]]

### VPC-Peering
- **Purpose:** Connect two VPCs privately using AWS network
- **Requirements:**
  - No overlapping CIDR (IP ranges)
  - **Not transitive** - must establish for each VPC pair
- Related: [[10-security-compliance#VPC]], [[10-security-compliance#PrivateLink]]

### VPC-Endpoints
- **Purpose:** Connect to AWS services via private network
- **Benefits:** Enhanced security, lower latency
- **Types:**
  | Type | Services | Cost |
  |------|----------|------|
  | Gateway Endpoint | S3, DynamoDB | Free |
  | Interface Endpoint (ENI) | Most services | Uses PrivateLink |
- Related: [[10-security-compliance#VPC]], [[10-security-compliance#PrivateLink]]

### PrivateLink
- **Purpose:** Most secure & scalable way to expose service to 1000s of VPCs
- **Does NOT require:** VPC peering, Internet gateway, NAT, Route tables
- **Architecture:**
  - Service VPC: Network Load Balancer
  - Customer VPC: Elastic Network Interface (ENI)
- **Flow:** Application → NLB → PrivateLink → ENI → Consumer
- Related: VPC-Endpoints, NLB

### Site-to-Site-VPN
- **Connection:** Over public internet (encrypted)
- **Setup Time:** Quick
- **Cost:** Lower than Direct Connect
- Related: Direct-Connect, [[10-security-compliance#VPC]]

### Direct-Connect
- **Connection:** Physical private connection
- **Speed:** Fast, consistent
- **Setup Time:** At least 1 month
- **Cost:** Higher than VPN
- Related: Site-to-Site-VPN, [[10-security-compliance#VPC]]

---

## SageMaker Security

### Data at Rest
- **KMS encryption** for:
  - Notebooks
  - Training, tuning, batch transform, endpoints
  - Everything under `/opt/ml/` and `/tmp`
- **S3 encryption** for training data and hosted models

### Data in Transit
- All traffic supports **TLS/SSL**
- IAM roles for resource access
- **Inter-node training encryption:**
  - Optional (inter-container traffic encryption)
  - Increases training time and cost
  - Enable via console or API

### VPC Configuration
- **Training Jobs:** Run in VPC; can use private VPC
  - Need **S3 VPC endpoints** for S3 access
  - Custom endpoint policies and bucket policies
- **Notebooks:** Internet-enabled by default (security hole!)
  - If disabled: Need Interface endpoint (PrivateLink) OR NAT Gateway
- **Training/Inference Containers:**
  - Internet-enabled by default
  - Network isolation available (but prevents S3 access)

### Logging and Monitoring
- **CloudWatch:** Endpoint invocations/latency, instance health, Ground Truth metrics
- **CloudTrail:** Records actions from users, roles, services; logs to S3

---

## Concept Relationships

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        AWS Security Architecture                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────┐                                                        │
│  │     IAM      │──────────────────────────────────────────────┐        │
│  │  Users/Roles │                                               │        │
│  │   Policies   │                                               ▼        │
│  └──────┬───────┘                                         ┌──────────┐  │
│         │                                                  │ SageMaker│  │
│         ▼                                                  │ Security │  │
│  ┌──────────────┐     ┌──────────────┐                    └────┬─────┘  │
│  │     KMS      │────▶│   Secrets    │                         │        │
│  │  Encryption  │     │   Manager    │                         │        │
│  └──────┬───────┘     └──────────────┘                         │        │
│         │                                                       │        │
│         ▼                                                       ▼        │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                           VPC                                     │   │
│  │  ┌─────────────────────┐    ┌─────────────────────┐              │   │
│  │  │   Public Subnet     │    │   Private Subnet    │              │   │
│  │  │  ┌───────────────┐  │    │  ┌───────────────┐  │              │   │
│  │  │  │Security Groups│  │    │  │Security Groups│  │              │   │
│  │  │  └───────────────┘  │    │  └───────────────┘  │              │   │
│  │  │         │           │    │         │           │              │   │
│  │  │         ▼           │    │         ▼           │              │   │
│  │  │  ┌───────────┐      │    │  ┌────────────┐     │              │   │
│  │  │  │   NACL    │      │    │  │    NACL    │     │              │   │
│  │  │  └───────────┘      │    │  └────────────┘     │              │   │
│  │  └─────────────────────┘    └─────────────────────┘              │   │
│  │           │                           │                          │   │
│  │           ▼                           ▼                          │   │
│  │  ┌─────────────────┐         ┌─────────────────┐                 │   │
│  │  │Internet Gateway │         │   NAT Gateway   │                 │   │
│  │  └─────────────────┘         └─────────────────┘                 │   │
│  │                                                                   │   │
│  │  ┌──────────────────────────────────────────────┐                │   │
│  │  │              VPC Endpoints                    │                │   │
│  │  │  Gateway: S3, DynamoDB                        │                │   │
│  │  │  Interface: Other services (PrivateLink)      │                │   │
│  │  └──────────────────────────────────────────────┘                │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │                    Edge Protection                              │     │
│  │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │     │
│  │  │     WAF      │    │    Shield    │    │  CloudFront  │      │     │
│  │  │  (Layer 7)   │    │  (Layer 3/4) │    │    (CDN)     │      │     │
│  │  └──────────────┘    └──────────────┘    └──────────────┘      │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │                    Monitoring & Auditing                        │     │
│  │  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │     │
│  │  │  CloudWatch  │    │  CloudTrail  │    │    Macie     │      │     │
│  │  │  (Metrics)   │    │   (Audit)    │    │    (PII)     │      │     │
│  │  └──────────────┘    └──────────────┘    └──────────────┘      │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Exam Tips

### IAM & Permissions
- **Least privilege:** Always the correct answer for security best practices
- **IAM Access Analyzer:** Generates least-privilege policies from access logs
- Users can belong to **multiple groups** or **no group**
- Groups **cannot contain other groups**
- **Inline policies** attach directly to users (not recommended)

### Encryption
- "Encryption" on exam usually means **KMS**
- **KMS keys are regional** - re-encrypt when copying across regions
- **Symmetric keys:** Used by AWS services, never access unencrypted key
- **Asymmetric keys:** Public key downloadable, for encryption outside AWS
- **Customer Managed Keys:** $1/month + API call costs

### VPC Security
- **Security Groups:** Stateful, allow-only, instance-level
- **NACLs:** Stateless, allow+deny, subnet-level, ordered rules
- **VPC Endpoints:** Free for S3/DynamoDB (Gateway), paid for others (Interface)
- **PrivateLink:** Best for exposing services to many VPCs without peering
- SageMaker notebooks are **internet-enabled by default** (security concern!)

### Network Protection
- **WAF:** Layer 7 (HTTP), does NOT support NLB
- **Shield Standard:** Free, automatic, Layer 3/4
- **Shield Advanced:** $3k/month, 24/7 DRP, cost protection
- Use **Global Accelerator + ALB** for fixed IP with WAF

### Data Protection
- **Macie:** Finds PII in S3 using ML
- **Secrets Manager:** RDS credentials, auto-rotation
- **Glue DataBrew/Redshift:** Data masking

### Hybrid Connectivity
- **Site-to-Site VPN:** Quick setup, over internet, encrypted
- **Direct Connect:** 1+ month setup, private physical connection, faster

### Common Exam Patterns
- "Most secure way to access AWS services" → VPC Endpoints
- "Expose service to many VPCs" → PrivateLink
- "Protect from SQL injection/XSS" → WAF
- "DDoS protection" → Shield (Standard free, Advanced paid)
- "Find sensitive data in S3" → Macie
- "Encrypt SageMaker training data" → KMS
- "Private access to S3 from VPC" → Gateway Endpoint (free)

---

## Cross-Section Links

- [[02-data-ingestion/concept-map#S3]] - S3 encryption and storage
- [[02-data-ingestion/concept-map#Kinesis]] - Data streaming security
- [[03-data-transformation/concept-map#Glue]] - Glue DataBrew masking
- [[06-model-training/concept-map#SageMaker]] - SageMaker training security
- [[09-mlops/concept-map#CloudWatch]] - Monitoring and logging
