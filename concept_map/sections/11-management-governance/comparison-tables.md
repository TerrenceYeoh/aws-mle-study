# Section 11: Management and Governance - Comparison Tables

## The Big Three: CloudWatch vs CloudTrail vs Config

| Aspect | CloudWatch | CloudTrail | Config |
|--------|------------|------------|--------|
| **Primary Purpose** | Performance monitoring | API auditing | Configuration compliance |
| **Answers** | "How is it performing?" | "Who did what?" | "Is it configured correctly?" |
| **Data Type** | Metrics, logs, events | API call records | Resource configurations |
| **Default State** | Must configure | Enabled by default | Must enable |
| **Scope** | Per-region (dashboards global) | All regions (default) | Per-region |
| **Real-time** | Yes (alarms, subscriptions) | Near real-time | On change or scheduled |
| **Can Prevent Actions** | No (alerts only) | No (audit only) | No (detect only) |

### ELB Example: When to Use Each

| Need | Service | Example |
|------|---------|---------|
| Monitor connections | CloudWatch | Track incoming connection metrics |
| Visualize errors | CloudWatch | Error codes as % over time dashboard |
| Track config changes | Config | Security group rule changes |
| Ensure SSL compliance | Config | Rule: ALB must have SSL certificate |
| Who changed settings? | CloudTrail | Track API calls to modify ALB |

---

## CloudWatch Logs Delivery Options

| Method | Latency | API/Feature | Best For |
|--------|---------|-------------|----------|
| **Subscriptions → Lambda** | Real-time | Subscription Filter | Immediate processing |
| **Subscriptions → Kinesis Streams** | Real-time | Subscription Filter | High-volume streaming |
| **Subscriptions → Kinesis Firehose** | Near real-time | Subscription Filter | S3, Redshift, OpenSearch |
| **S3 Export** | Up to 12 hours | CreateExportTask | Batch archival |
| **Metric Streams** | Near real-time | Metric Streams | 3rd party (Datadog, Splunk) |

---

## CloudWatch Agent Comparison

| Aspect | Logs Agent (Old) | Unified Agent (New) |
|--------|------------------|---------------------|
| **Status** | Legacy | Recommended |
| **Logs Collection** | Yes | Yes |
| **System Metrics** | No | Yes |
| **RAM Metrics** | No | Yes |
| **Process Metrics** | No | Yes |
| **Configuration** | Local file | SSM Parameter Store |
| **On-premises** | Yes | Yes |

---

## CloudWatch Alarm States

| State | Meaning | Typical Cause |
|-------|---------|---------------|
| **OK** | Within threshold | Normal operation |
| **INSUFFICIENT_DATA** | Not enough data | New metric, missing data points |
| **ALARM** | Threshold breached | Issue requiring attention |

---

## X-Ray vs CloudWatch Logs

| Aspect | X-Ray | CloudWatch Logs |
|--------|-------|-----------------|
| **Purpose** | Distributed tracing | Log aggregation |
| **View** | Service map, traces | Log entries |
| **Best For** | Debugging request flow | Searching log content |
| **Instrumentation** | X-Ray SDK | Agent or SDK |
| **Correlation** | Automatic (trace ID) | Manual (log patterns) |
| **Latency Analysis** | Built-in | Must parse logs |

---

## QuickSight Editions

| Feature | Standard | Enterprise |
|---------|----------|------------|
| **Price** | $9/user/month | $18/user/month |
| **SPICE** | 10GB/user | 10GB/user |
| **Row-level Security** | Yes | Yes |
| **Column-level Security** | No | Yes |
| **Active Directory** | No | Yes |
| **Encryption at Rest** | Yes | Yes |
| **Extra SPICE Cost** | $0.25/GB | $0.38/GB |
| **Q (NLP)** | Add $10/user | Add $10/user |

---

## QuickSight Visual Types by Use Case

| Use Case | Best Visual Type |
|----------|------------------|
| Compare values | Bar Charts |
| Distribution (histogram) | Bar Charts |
| Change over time | Line Graphs |
| Correlation | Scatter Plots, Heat Maps |
| Part of whole | Pie Charts, Donut Charts, Tree Maps |
| Tabular data | Pivot Tables |
| Key metrics | KPIs |
| Geographic data | Geospatial Charts |
| Progress to goal | Gauge Charts |
| Text frequency | Word Clouds |
| Let system decide | AutoGraph |

---

## CloudTrail Event Types

| Event Type | Description | Logged by Default | Volume |
|------------|-------------|-------------------|--------|
| **Management Events** | Control plane operations (IAM, VPC, etc.) | Yes | Low-Medium |
| **Data Events** | Data plane operations (S3 objects, Lambda invoke) | No | High |
| **Insights Events** | Anomaly detection | No | N/A |

### Management vs Data Events Examples

| Management Events | Data Events |
|-------------------|-------------|
| CreateBucket | GetObject |
| AttachRolePolicy | PutObject |
| CreateSubnet | DeleteObject |
| CreateTrail | Lambda Invoke |
| RunInstances | - |

---

## Config Rules Types

| Aspect | AWS Managed Rules | Custom Rules |
|--------|-------------------|--------------|
| **Count** | 75+ pre-built | Unlimited |
| **Created By** | AWS | You (Lambda function) |
| **Maintenance** | AWS maintains | You maintain |
| **Flexibility** | Limited to rule params | Full control |
| **Cost** | Same | Same |

---

## Config Notification Options

| Method | Events | Filtering | Best For |
|--------|--------|-----------|----------|
| **EventBridge** | NON_COMPLIANT only (configurable) | Rule-based | Automated responses |
| **SNS Direct** | All events | SNS Filtering or client-side | Broad notifications |

---

## Cost Management Services

| Service | Purpose | Key Feature | Pricing |
|---------|---------|-------------|---------|
| **Budgets** | Cost alerts | Threshold notifications | 2 free, then $0.02/day |
| **Cost Explorer** | Cost analysis | 12-month forecasting | Included |
| **Trusted Advisor** | Account assessment | 6-category recommendations | Plan-dependent |

### Budget Types

| Type | Tracks |
|------|--------|
| Usage | Resource usage |
| Cost | Dollar spending |
| Reservation | Reserved Instance utilization |
| Savings Plans | Savings Plan utilization |

---

## Trusted Advisor Access by Support Plan

| Support Plan | Access Level |
|--------------|--------------|
| Basic | Core security checks only |
| Developer | Core security checks only |
| **Business** | Full checks + API access |
| **Enterprise** | Full checks + API access |

### Trusted Advisor Categories

| Category | Example Checks |
|----------|----------------|
| Cost Optimization | Underutilized EC2, idle RDS |
| Performance | High utilization, CloudFront config |
| Security | MFA on root, public S3 buckets |
| Fault Tolerance | EBS snapshots, RDS Multi-AZ |
| Service Limits | Approaching service quotas |
| Operational Excellence | Best practice adherence |

---

## Quick Decision Tables

### Which Monitoring/Audit Service?

| Question | Answer |
|----------|--------|
| Monitor CPU, memory, network? | **CloudWatch Metrics** |
| Search application logs? | **CloudWatch Logs Insights** |
| Real-time log processing? | **CloudWatch Logs Subscriptions** |
| Create performance dashboard? | **CloudWatch Dashboard** |
| Trigger action on threshold? | **CloudWatch Alarms** |
| Track API calls (who did what)? | **CloudTrail** |
| Detect unusual API activity? | **CloudTrail Insights** |
| Check resource compliance? | **AWS Config** |
| Auto-fix non-compliant resources? | **Config + SSM Remediation** |
| Debug distributed app? | **AWS X-Ray** |
| Business analytics dashboard? | **QuickSight** |

### Which Cost Service?

| Question | Answer |
|----------|--------|
| Alert when spending exceeds threshold? | **AWS Budgets** |
| Analyze historical spending? | **Cost Explorer** |
| Forecast future costs? | **Cost Explorer** |
| Get Savings Plan recommendations? | **Cost Explorer** |
| Account best practices review? | **Trusted Advisor** |
| Find underutilized resources? | **Trusted Advisor** |

### Real-Time vs Batch?

| Need | Solution |
|------|----------|
| Immediate log processing | Subscriptions → Lambda |
| Stream metrics to Datadog | Metric Streams |
| Archive logs to S3 | S3 Export (12hr delay) OR Subscriptions → Firehose |
| Query historical logs | Logs Insights |

### Compliance vs Prevention?

| Need | Solution |
|------|----------|
| Detect non-compliant config | AWS Config |
| Prevent non-compliant config | IAM Policies, SCPs |
| Auto-remediate non-compliant | Config + SSM Automation |
| Alert on non-compliant | Config + EventBridge + SNS |

### Which X-Ray Component?

| Need | Component |
|------|-----------|
| Capture calls in code | X-Ray SDK |
| Send traces to AWS | X-Ray Daemon |
| View service dependencies | X-Ray Service Map |
| Search traces | X-Ray Console |
| Filter by custom metadata | Annotations |

---

## Latency Comparison

| Service/Feature | Latency |
|-----------------|---------|
| CloudWatch Alarms | 1 minute minimum |
| CloudWatch Logs Subscriptions → Lambda | Real-time |
| CloudWatch Logs Subscriptions → Kinesis | Real-time |
| CloudWatch Metric Streams | Near real-time |
| CloudWatch Logs S3 Export | Up to 12 hours |
| CloudTrail (Management Events) | ~15 minutes |
| Config Rule Evaluation | On change or scheduled |
| X-Ray Trace Processing | Near real-time |

---

## Pricing Quick Reference

| Service | Free Tier | Paid |
|---------|-----------|------|
| CloudWatch Metrics | 10 custom metrics | $0.30/metric/month |
| CloudWatch Logs | 5GB ingestion | $0.50/GB ingested |
| CloudTrail | Management events | Data events: $0.10/100K |
| Config | None | $0.003/config item |
| X-Ray | 100K traces | $5/million traces |
| QuickSight | 1 user (first month) | $9-28/user/month |
| Budgets | 2 budgets | $0.02/day/budget |
| Trusted Advisor | Core checks | Business/Enterprise plan |
