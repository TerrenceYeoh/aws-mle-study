# Section 11: Management and Governance

## Overview

This section covers AWS services for monitoring, logging, auditing, compliance, and cost management. Key services include **CloudWatch** (metrics, logs, alarms), **X-Ray** (distributed tracing), **QuickSight** (business analytics), **CloudTrail** (API auditing), **Config** (compliance), and cost management tools (Budgets, Cost Explorer, Trusted Advisor).

**Key Takeaways:**
- CloudWatch = Performance monitoring and alerting
- CloudTrail = API audit trail (enabled by default)
- Config = Configuration compliance (does NOT prevent actions)
- X-Ray = Distributed application debugging
- QuickSight = Serverless BI with ML insights

---

## Core Concepts

### [[Monitoring-vs-Auditing-vs-Compliance]]
- **Monitoring (CloudWatch):** Real-time performance metrics, logs, alarms
- **Auditing (CloudTrail):** Who did what? API call history
- **Compliance (Config):** Is the configuration correct? Does it meet rules?

### [[Real-Time-vs-Near-Real-Time-vs-Batch]]
| Delivery Type | CloudWatch Feature | Latency |
|--------------|-------------------|---------|
| Real-time | Logs Subscriptions → Lambda | Immediate |
| Near-real-time | Logs Subscriptions → Firehose | Seconds |
| Near-real-time | Metric Streams | Seconds |
| Batch | S3 Export (CreateExportTask) | Up to 12 hours |

### [[Distributed-Tracing]]
- **Trace:** End-to-end path of a request through services
- **Segment:** Individual component's contribution to trace
- **Sub-segment:** Granular breakdown within segment
- **Annotation:** Metadata for filtering/searching traces

---

## AWS Services

### [[Amazon-CloudWatch]]

**Purpose:** Centralized monitoring for AWS services and applications

**Components:**
| Component | Purpose |
|-----------|---------|
| **Metrics** | Numerical data points (CPU, memory, custom) |
| **Logs** | Text-based logging (applications, services) |
| **Alarms** | Trigger actions based on metric thresholds |
| **Dashboards** | Visual display of metrics |
| **Metric Streams** | Near-real-time metric export |
| **Logs Insights** | Query engine for logs |

**Key Concepts:**
- **Namespace:** Grouping for metrics (e.g., AWS/EC2)
- **Dimension:** Attribute to filter metrics (up to 30 per metric)
- **Custom Metrics:** User-defined metrics (e.g., RAM)

**CloudWatch Logs Structure:**
```
Log Group (application-level)
  └── Log Stream (instance/container-level)
       └── Log Events (individual entries)
```

**Log Expiration:** 1 day to 10 years, or never expire

**Related:** [[Kinesis-Data-Firehose]], [[S3]], [[Lambda]], [[SNS]]

---

### [[CloudWatch-Unified-Agent]]

**Purpose:** Collect logs AND system-level metrics from EC2/on-premises

**Metrics Collected:**
- CPU (active, guest, idle, system, user, steal)
- Disk metrics (free, used, total)
- Disk IO (writes, reads, bytes, iops)
- **RAM** (not available by default in CloudWatch!)
- Netstat (TCP/UDP connections)
- Processes (total, dead, blocked, running)
- Swap Space

**Configuration:** Centralized via **SSM Parameter Store**

**Related:** [[CloudWatch-Logs-Agent]], [[SSM-Parameter-Store]]

---

### [[CloudWatch-Alarms]]

**Purpose:** Trigger notifications and actions based on metric thresholds

**Alarm States:**
| State | Meaning |
|-------|---------|
| OK | Within threshold |
| INSUFFICIENT_DATA | Not enough data points |
| ALARM | Threshold breached |

**Targets:**
1. EC2 Actions (Stop, Terminate, Reboot, Recover)
2. Auto Scaling (trigger scaling)
3. SNS (notifications → Lambda, SQS, etc.)

**Composite Alarms:**
- Combine multiple alarms with AND/OR logic
- Reduce alarm noise
- Example: Alert only when BOTH CPU AND memory are high

**Logs-Based Alarms:**
```
CloudWatch Logs → Metric Filter → Metric → Alarm → SNS
```

**Related:** [[Auto-Scaling]], [[SNS]], [[EC2]]

---

### [[AWS-X-Ray]]

**Purpose:** Distributed tracing for debugging microservices

**Advantages:**
- Visualize service dependencies
- Identify performance bottlenecks
- Find errors and exceptions
- Check SLA compliance
- Trace request flow end-to-end

**Compatible Services:**
- Lambda, Elastic Beanstalk, ECS, ELB, API Gateway, EC2

**Setup Requirements:**
1. **Instrument code** with X-Ray SDK (Java, Python, Go, Node.js, .NET)
2. **Run X-Ray Daemon** (low-level UDP interceptor)
3. **IAM permissions** (AWSX-RayWriteOnlyAccess for Lambda)

**Security:**
- IAM for authorization
- KMS for encryption at rest

**Related:** [[Lambda]], [[API-Gateway]], [[ECS]]

---

### [[Amazon-QuickSight]]

**Purpose:** Serverless business intelligence and analytics

**Key Features:**
- Build visualizations and dashboards
- Ad-hoc analysis
- Accessible on any device
- **SPICE:** In-memory calculation engine (10GB per user)

**Data Sources:**
| AWS Sources | File Sources |
|-------------|--------------|
| Redshift, Aurora, RDS | Excel |
| Athena | CSV, TSV |
| S3 | Log files |
| EC2-hosted DBs | JDBC/ODBC |

**ML Insights:**
- **Anomaly Detection:** Unusual patterns
- **Forecasting:** Predict future values
- **Auto-narratives:** NL descriptions

**QuickSight Q:** Natural language queries ("What are top-selling items in Florida?")

**Security:**
| Feature | Edition |
|---------|---------|
| MFA | All |
| Row-level Security | All |
| Column-level Security | Enterprise only |
| Active Directory | Enterprise only |

**Pricing:**
- Standard: $9/user/month
- Enterprise: $18/user/month
- Enterprise + Q: $28/user/month
- Extra SPICE: $0.25-0.38/GB/month

**Anti-Patterns:**
- Heavy ETL (use [[Glue]] instead)

**Related:** [[Athena]], [[Redshift]], [[S3]]

---

### [[AWS-CloudTrail]]

**Purpose:** Audit trail of API calls in your AWS account

**Key Points:**
- **Enabled by default!**
- Records: Console, SDK, CLI, AWS Service API calls
- Scope: All Regions (default) or single Region
- **First place to look when a resource is deleted**

**Event Types:**
| Type | Description | Logged by Default |
|------|-------------|-------------------|
| Management Events | IAM, EC2 config, etc. | Yes |
| Data Events | S3 object-level, Lambda Invoke | No (high volume) |
| Insights Events | Unusual activity detection | No (must enable) |

**CloudTrail Insights Detects:**
- Inaccurate resource provisioning
- Hitting service limits
- Bursts of IAM actions
- Gaps in periodic maintenance

**Retention:**
- CloudTrail: 90 days
- Long-term: S3 → Athena queries

**Related:** [[S3]], [[Athena]], [[EventBridge]]

---

### [[AWS-Config]]

**Purpose:** Configuration compliance auditing

**Features:**
- Record configuration changes over time
- Evaluate resources against compliance rules
- View timeline of changes
- **Per-region service** (can aggregate cross-account/region)

**Important:** Config Rules **do NOT prevent actions** - only detect and report!

**Rule Types:**
- **AWS Managed Rules:** 75+ pre-built
- **Custom Rules:** Lambda-based

**Triggers:**
- On configuration change
- At regular intervals

**Remediations:**
- Auto-remediate via **SSM Automation Documents**
- AWS-managed or custom documents
- Can invoke Lambda
- Configurable retry count

**Notifications:**
- EventBridge → Lambda, SNS, SQS
- SNS direct (all events)

**Pricing:**
- $0.003 per config item recorded
- $0.001 per rule evaluation

**Related:** [[SSM]], [[Lambda]], [[EventBridge]]

---

### [[AWS-Budgets]]

**Purpose:** Cost alerts when spending exceeds threshold

**Budget Types:**
1. Usage
2. Cost
3. Reservation (RI utilization)
4. Savings Plans

**Features:**
- Up to 5 SNS notifications per budget
- Filter by service, account, tag, region, etc.
- RI tracking for EC2, ElastiCache, RDS, Redshift

**Pricing:**
- 2 budgets free
- $0.02/day/budget after

**Related:** [[Cost-Explorer]], [[SNS]]

---

### [[AWS-Cost-Explorer]]

**Purpose:** Visualize and analyze AWS costs

**Features:**
- Custom reports
- High-level or granular (monthly/hourly/resource)
- Savings Plan recommendations
- **Forecast up to 12 months**

**Related:** [[Budgets]], [[Trusted-Advisor]]

---

### [[AWS-Trusted-Advisor]]

**Purpose:** High-level AWS account assessment

**6 Categories:**
1. Cost Optimization
2. Performance
3. Security
4. Fault Tolerance
5. Service Limits
6. Operational Excellence

**Access:**
- Basic/Developer: Core checks only
- Business/Enterprise: Full checks + API access

**Related:** [[Cost-Explorer]], [[Budgets]]

---

## Concept Relationships

```
                    ┌─────────────────────────────────────────┐
                    │         Management & Governance          │
                    └─────────────────────────────────────────┘
                                       │
        ┌──────────────┬──────────────┼──────────────┬──────────────┐
        ▼              ▼              ▼              ▼              ▼
   ┌─────────┐   ┌──────────┐   ┌─────────┐   ┌──────────┐   ┌─────────┐
   │CloudWatch│   │CloudTrail│   │ Config  │   │ X-Ray   │   │QuickSight│
   │(Monitor) │   │ (Audit)  │   │(Comply) │   │(Trace)  │   │  (BI)   │
   └────┬────┘   └────┬─────┘   └────┬────┘   └────┬────┘   └────┬────┘
        │             │              │             │              │
   ┌────┴────┐        │         ┌────┴────┐       │         ┌────┴────┐
   │Metrics  │        │         │Rules    │       │         │SPICE    │
   │Logs     │        │         │Remediate│       │         │ML Insight│
   │Alarms   │        │         │Notify   │       │         │Q (NLP)  │
   └─────────┘        │         └─────────┘       │         └─────────┘
                      │                           │
                      ▼                           ▼
               ┌────────────┐            ┌────────────────┐
               │ S3/Athena  │            │ Service Map    │
               │ (Long-term)│            │ Trace Analysis │
               └────────────┘            └────────────────┘

              ┌──────────────────────────────────────────┐
              │            Cost Management               │
              └──────────────────────────────────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
        ┌──────────┐     ┌───────────┐    ┌─────────────┐
        │ Budgets  │     │Cost Explorer│   │Trusted Advisor│
        │ (Alerts) │     │ (Analyze) │    │  (Assess)   │
        └──────────┘     └───────────┘    └─────────────┘
```

---

## Exam Tips

### CloudWatch
- **RAM not available by default** - need Unified Agent
- Logs S3 export takes **up to 12 hours** - use Subscriptions for real-time
- Composite Alarms = AND/OR logic to reduce noise
- Metric Streams → Kinesis Firehose → 3rd party (Datadog, Splunk)

### X-Ray
- Requires: X-Ray SDK + X-Ray Daemon
- Lambda needs **AWSX-RayWriteOnlyAccess** policy
- Traces → Segments → Sub-segments

### QuickSight
- SPICE = **10GB per user**
- Enterprise Edition for: Column-level security, Active Directory
- **NOT for ETL** - use Glue
- Q = Natural Language queries

### CloudTrail
- **Enabled by default** (Management Events)
- Data Events (S3 object-level, Lambda) = NOT default (high volume)
- Insights = unusual activity detection
- **90 days** default retention → S3 for longer

### Config
- **Does NOT prevent** - only detect and report
- Remediation via **SSM Automation Documents**
- Per-region (aggregate across accounts/regions)
- No free tier

### When to Use Which
| Question | Answer |
|----------|--------|
| Monitor performance? | CloudWatch |
| Who made API calls? | CloudTrail |
| Is config compliant? | Config |
| Debug distributed app? | X-Ray |
| Business dashboards? | QuickSight |
| Cost alerts? | Budgets |
| Analyze spending? | Cost Explorer |
| Account best practices? | Trusted Advisor |

### Critical Distinctions
- **CloudWatch Logs Insights** = Query engine, NOT real-time
- **Config Rules** = Detect only, NOT deny
- **CloudTrail** = API audit, NOT performance metrics
- **X-Ray** = Request tracing, NOT log aggregation
