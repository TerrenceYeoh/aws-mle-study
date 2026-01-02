# Section 10: Security, Identity, and Compliance - Comparison Tables

## Encryption Types

### At Rest vs In Transit vs Client-Side

| Aspect | Encryption at Rest | Encryption in Transit | Client-Side Encryption |
|--------|-------------------|----------------------|------------------------|
| **When** | Data stored on disk | Data moving over network | Before sending to AWS |
| **Who Encrypts** | Server | TLS/SSL protocol | Client application |
| **Who Decrypts** | Server | TLS/SSL protocol | Receiving client |
| **Key Management** | Server (KMS) | TLS certificates | Client (may use KMS) |
| **Server Access** | Has decrypted access | N/A | Never sees decrypted data |
| **AWS Service** | KMS | HTTPS/TLS | Envelope Encryption |
| **Use Case** | Stored data protection | Network protection | Zero-trust, sensitive data |

---

## KMS Key Types

### Symmetric vs Asymmetric Keys

| Aspect | Symmetric (AES-256) | Asymmetric (RSA/ECC) |
|--------|---------------------|----------------------|
| **Keys** | Single key | Public + Private pair |
| **Operations** | Encrypt & Decrypt | Encrypt (public) / Decrypt (private) |
| **Key Access** | Never unencrypted | Public downloadable, private never |
| **KMS API Required** | Yes, always | No (can use public key outside AWS) |
| **AWS Integration** | All AWS services | Limited |
| **Use Case** | Standard AWS encryption | Encryption outside AWS |

### KMS Key Categories

| Key Type | Cost | Rotation | Management | Use Case |
|----------|------|----------|------------|----------|
| **AWS Owned** | Free | Automatic | AWS manages entirely | Default encryption |
| **AWS Managed** (aws/service-name) | Free | Auto every 1 year | AWS manages, you audit | Service-integrated encryption |
| **Customer Managed** (created in KMS) | $1/month | Must enable (auto & on-demand) | You manage | Custom policies, cross-account |
| **Customer Managed** (imported) | $1/month | Manual only (via alias) | You manage entirely | Bring-your-own-key (BYOK) |

**API Calls:** $0.03 per 10,000 calls

---

## IAM Components

### Users vs Groups vs Roles

| Aspect | Users | Groups | Roles |
|--------|-------|--------|-------|
| **Purpose** | People in organization | Organize users | Allow services to act |
| **Identity** | Has credentials | Collection of users | Assumed identity |
| **Contains** | Policies | Only users (not groups) | Policies |
| **Multiple Membership** | Can be in multiple groups | N/A | N/A |
| **Credentials** | Password, access keys | None | Temporary credentials |
| **Example** | Developer account | "DataScientists" group | EC2 Instance Role |

### Policy vs Role

| Aspect | IAM Policy | IAM Role |
|--------|------------|----------|
| **What It Is** | JSON permissions document | Identity that can be assumed |
| **Attached To** | Users, Groups, Roles | Services, Users (cross-account) |
| **Contains** | Effect, Action, Resource | Trust policy + Permission policies |
| **Use Case** | Define what's allowed | Define who can do actions |

---

## Network Security

### Security Groups vs Network ACLs

| Aspect | Security Group | Network ACL (NACL) |
|--------|----------------|-------------------|
| **Level** | Instance (ENI) | Subnet |
| **Rules** | Allow only | Allow AND Deny |
| **State** | Stateful (return traffic auto-allowed) | Stateless (must allow return traffic) |
| **Evaluation** | All rules evaluated | Rules in number order |
| **Association** | Must specify per instance | Auto-applies to all in subnet |
| **Default** | Deny all inbound, allow all outbound | Allow all (default NACL) |
| **Rule Limit** | 60 inbound + 60 outbound | 20 inbound + 20 outbound |

---

## VPC Endpoints

### Gateway vs Interface Endpoints

| Aspect | Gateway Endpoint | Interface Endpoint |
|--------|-----------------|-------------------|
| **Services** | S3, DynamoDB only | Most other AWS services |
| **Cost** | Free | PrivateLink charges |
| **Implementation** | Route table entry | ENI in subnet |
| **IP Address** | No ENI, uses prefix list | Private IP in your VPC |
| **Technology** | AWS internal | AWS PrivateLink |
| **Zonal** | Regional | Per-AZ |
| **Security** | Endpoint policies | Endpoint policies + Security Groups |

---

## Hybrid Connectivity

### Site-to-Site VPN vs Direct Connect

| Aspect | Site-to-Site VPN | Direct Connect (DX) |
|--------|------------------|---------------------|
| **Connection Type** | Over public internet | Physical private line |
| **Security** | Encrypted (IPsec) | Private (not encrypted by default) |
| **Bandwidth** | Variable | Consistent (1 Gbps - 100 Gbps) |
| **Latency** | Variable | Low, consistent |
| **Setup Time** | Minutes to hours | 1+ month |
| **Cost** | Lower | Higher |
| **Redundancy** | Easy (multiple tunnels) | Requires second DX |
| **Best For** | Quick setup, lower bandwidth | High throughput, consistent latency |

---

## DDoS Protection

### Shield Standard vs Shield Advanced

| Aspect | Shield Standard | Shield Advanced |
|--------|-----------------|-----------------|
| **Cost** | Free | $3,000/month/organization |
| **Activation** | Automatic for all | Must enable |
| **Protection Level** | Basic Layer 3/4 | Sophisticated Layer 3/4/7 |
| **Attack Types** | SYN/UDP floods, reflection | All + application layer |
| **Resources Protected** | All AWS resources | EC2, ELB, CloudFront, Global Accelerator, Route 53 |
| **Support** | None | 24/7 DDoS Response Team (DRP) |
| **Cost Protection** | None | Yes (protects from usage spikes) |
| **WAF Integration** | None | Auto-deploys WAF rules |

---

## Data Protection Services

### Macie vs Secrets Manager vs KMS

| Aspect | Macie | Secrets Manager | KMS |
|--------|-------|-----------------|-----|
| **Purpose** | Discover sensitive data | Store/rotate secrets | Encrypt/decrypt data |
| **Primary Target** | S3 buckets | RDS credentials, API keys | Any AWS data |
| **Method** | ML + pattern matching | Encrypted storage + Lambda | Cryptographic keys |
| **PII Detection** | Yes | No | No |
| **Auto-Rotation** | N/A | Yes (RDS native) | Yes (key rotation) |
| **Alerts** | EventBridge | CloudWatch | CloudTrail |
| **Cost Model** | Per GB scanned | Per secret + API calls | Per key + API calls |

### Anonymization Techniques

| Technique | Reversible | Data Utility | Best For |
|-----------|------------|--------------|----------|
| **Replace with Random** | No | Low | Test data |
| **Shuffle** | Theoretically | Medium | Preserving distribution |
| **Deterministic Encrypt** | Yes (with key) | High | Cross-dataset joins |
| **Probabilistic Encrypt** | Yes (with key) | Medium | Maximum security |
| **Hash** | No | Low | Verification only |
| **Delete** | No | None | When data not needed |

---

## MFA Device Types

| Device Type | Examples | Physical | Multi-User | Best For |
|-------------|----------|----------|------------|----------|
| **Virtual MFA** | Google Authenticator, Authy | No (phone) | Multiple tokens/device | General use |
| **U2F Security Key** | YubiKey | Yes | Multiple users/key | High security |
| **Hardware Key Fob** | Gemalto | Yes | Single user | Dedicated device |
| **GovCloud Key Fob** | SurePassID | Yes | Single user | AWS GovCloud (US) |

---

## SageMaker Security Options

### Notebook Security Configurations

| Aspect | Internet Enabled (Default) | Internet Disabled |
|--------|---------------------------|-------------------|
| **Outbound Access** | Full internet | VPC only |
| **Security** | Lower (security hole) | Higher |
| **Requirements** | None | Interface endpoint OR NAT Gateway |
| **S3 Access** | Direct | Via VPC Endpoint |
| **Best Practice** | Development | Production |

### Inter-Container Encryption

| Aspect | Disabled (Default) | Enabled |
|--------|-------------------|---------|
| **Security** | Standard | Enhanced |
| **Training Time** | Normal | Increased |
| **Cost** | Normal | Increased (deep learning) |
| **Use Case** | General workloads | Sensitive data |

---

## WAF Rule Types

| Rule Type | What It Checks | Use Case |
|-----------|----------------|----------|
| **IP Set** | Source IP (up to 10,000) | Block known bad IPs |
| **HTTP Inspection** | Headers, body, URI | Custom application logic |
| **SQL Injection** | SQL patterns | Database protection |
| **XSS** | Script injection | Frontend protection |
| **Size Constraints** | Request size | Prevent large payload attacks |
| **Geo-Match** | Country of origin | Geographic restrictions |
| **Rate-Based** | Requests per time | DDoS protection |

---

## Quick Decision Tables

### Which Encryption Service?

| Question | Answer |
|----------|--------|
| Encrypt data at rest? | **KMS** |
| Store database credentials? | **Secrets Manager** |
| Find PII in S3? | **Macie** |
| Encrypt in transit? | **TLS/SSL (HTTPS)** |
| Need key rotation for RDS? | **Secrets Manager** |
| Need custom key policies? | **KMS Customer Managed Key** |

### Which VPC Endpoint?

| Question | Answer |
|----------|--------|
| Access S3 from VPC? | **Gateway Endpoint** (free) |
| Access DynamoDB from VPC? | **Gateway Endpoint** (free) |
| Access other AWS services? | **Interface Endpoint** (PrivateLink) |
| Expose service to many VPCs? | **PrivateLink** |
| Need Security Group on endpoint? | **Interface Endpoint** |

### Which DDoS Protection?

| Question | Answer |
|----------|--------|
| Basic protection needed? | **Shield Standard** (free, automatic) |
| Critical application? | **Shield Advanced** |
| Need DDoS Response Team? | **Shield Advanced** |
| Worried about cost spikes from attacks? | **Shield Advanced** |
| Layer 7 auto-mitigation? | **Shield Advanced** |

### Which Network Security?

| Question | Answer |
|----------|--------|
| Control traffic to EC2 instance? | **Security Group** |
| Control traffic at subnet level? | **NACL** |
| Need deny rules? | **NACL** |
| Stateful (auto-allow return)? | **Security Group** |
| Block specific IPs? | **NACL** (or WAF for HTTP) |

### Which Hybrid Connection?

| Question | Answer |
|----------|--------|
| Quick setup needed? | **Site-to-Site VPN** |
| Consistent low latency? | **Direct Connect** |
| Budget constrained? | **Site-to-Site VPN** |
| High bandwidth (>1 Gbps)? | **Direct Connect** |
| Backup connection? | **VPN** (over Direct Connect) |

### Which IAM Entity?

| Question | Answer |
|----------|--------|
| Human needs AWS access? | **IAM User** |
| Organize user permissions? | **IAM Group** |
| Service needs AWS access? | **IAM Role** |
| Define permissions? | **IAM Policy** |
| Cross-account access? | **IAM Role** |
| EC2 needs to call AWS APIs? | **IAM Role** (Instance Profile) |

### Which Logging/Monitoring?

| Question | Answer |
|----------|--------|
| Track API calls (who did what)? | **CloudTrail** |
| Monitor metrics (CPU, latency)? | **CloudWatch** |
| Capture network traffic info? | **VPC Flow Logs** |
| Find sensitive data? | **Macie** |
