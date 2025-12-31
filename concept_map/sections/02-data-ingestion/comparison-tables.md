# Section 2: Data Ingestion and Storage - Comparison Tables

## Data Architecture Comparisons

### Data Warehouse vs Data Lake vs Data Lakehouse

| Aspect | Data Warehouse | Data Lake | Data Lakehouse |
|--------|---------------|-----------|----------------|
| **Data Type** | Structured only | All types (raw) | All types |
| **Schema** | Schema-on-write | Schema-on-read | Both |
| **Processing** | ETL | ELT | Both |
| **Query Speed** | Fast (optimized) | Slower (raw) | Fast + flexible |
| **Cost** | Higher | Lower | Medium |
| **Use Cases** | BI, reporting | ML, exploration | Unified analytics |
| **AWS Service** | Redshift | S3 | S3 + Glue + Athena |

---

## Storage Service Comparisons

### S3 vs EBS vs EFS vs FSx

| Criteria | S3 | EBS | EFS | FSx |
|----------|----|----|-----|-----|
| **Type** | Object | Block | File (NFS) | File (varies) |
| **Access** | HTTP/API | Single EC2* | Multi-instance | Multi-instance |
| **Availability** | Multi-AZ | Single AZ | Multi-AZ | Varies |
| **OS Support** | Any | Any | Linux only | Depends on type |
| **Scaling** | Unlimited | Manual resize | Automatic | Manual/Auto |
| **Best For** | Data lake, backups | Boot volumes, DBs | Shared Linux files | HPC, Windows |
| **Cost Model** | Per GB stored | Per GB provisioned | Per GB used | Per GB + throughput |

*EBS Multi-Attach available for io1/io2 in same AZ

### EBS Volume Types

| Type | Category | Max IOPS | Max Throughput | Use Case |
|------|----------|----------|----------------|----------|
| gp3 | SSD | 16,000 | 1,000 MB/s | General purpose (recommended) |
| gp2 | SSD | 16,000 | 250 MB/s | General purpose (legacy) |
| io2 Block Express | SSD | 256,000 | 4,000 MB/s | Critical databases |
| io2/io1 | SSD | 64,000 | 1,000 MB/s | High-performance DBs |
| st1 | HDD | 500 | 500 MB/s | Throughput-intensive |
| sc1 | HDD | 250 | 250 MB/s | Cold data, lowest cost |

### FSx Variants

| FSx Type | Protocol | Max Performance | OS Support | Best For |
|----------|----------|-----------------|------------|----------|
| **Lustre** | Lustre | 100s GB/s, millions IOPS | Linux | HPC, ML training |
| **Windows** | SMB | 2+ GB/s | Windows | Windows apps, AD |
| **NetApp ONTAP** | NFS, SMB, iSCSI | 2+ GB/s | All | Multi-protocol |
| **OpenZFS** | NFS | 1M IOPS, <0.5ms | All | ZFS workloads |

---

## S3 Storage Class Comparisons

### S3 Storage Classes - Full Comparison

| Class | Availability | Durability | Min Storage | Retrieval Fee | Use Case |
|-------|--------------|------------|-------------|---------------|----------|
| Standard | 99.99% | 11 9s | None | None | Frequent access |
| Intelligent-Tiering | 99.9% | 11 9s | None | None | Unknown patterns |
| Standard-IA | 99.9% | 11 9s | 30 days | Per GB | Infrequent but fast |
| One Zone-IA | 99.5% | 11 9s* | 30 days | Per GB | Recreatable data |
| Glacier Instant | 99.9% | 11 9s | 90 days | Per GB | Archive + instant |
| Glacier Flexible | 99.99% | 11 9s | 90 days | Per GB | Min-hours retrieval |
| Glacier Deep Archive | 99.99% | 11 9s | 180 days | Per GB | 12-48 hrs retrieval |

*One Zone: 11 9s within single AZ only

### Glacier Retrieval Options

| Glacier Class | Expedited | Standard | Bulk |
|---------------|-----------|----------|------|
| Glacier Instant | Milliseconds | - | - |
| Glacier Flexible | 1-5 min | 3-5 hours | 5-12 hours |
| Glacier Deep Archive | N/A | 12 hours | 48 hours |

---

## S3 Encryption Comparisons

### S3 Encryption Methods

| Method | Key Management | Key Location | Audit Trail | Use Case |
|--------|----------------|--------------|-------------|----------|
| SSE-S3 | AWS manages | AWS | Limited | Default, simple |
| SSE-KMS | Customer via KMS | AWS KMS | CloudTrail | Compliance, audit |
| SSE-C | Customer provides | Customer | None in AWS | Full control |
| Client-Side | Customer manages | Customer | None in AWS | Encrypt before upload |

### When to Use Each Encryption

| Requirement | Best Option |
|-------------|-------------|
| Simple, no key management | SSE-S3 |
| Audit key usage | SSE-KMS |
| Separate key permissions | SSE-KMS |
| Customer-managed keys, no KMS | SSE-C |
| Regulatory: encrypt before cloud | Client-Side |

---

## Streaming Service Comparisons

### Kinesis Data Streams vs Data Firehose

| Aspect | Kinesis Data Streams | Amazon Data Firehose |
|--------|---------------------|----------------------|
| **Purpose** | Collect & store streams | Deliver to destinations |
| **Latency** | **Real-time** | **Near real-time** |
| **Data Storage** | Up to 365 days | **No storage** |
| **Replay** | **Yes** | **No** |
| **Scaling** | Manual (shards) or On-Demand | Automatic |
| **Management** | Producer/consumer code | Fully managed |
| **Destinations** | Custom (your code) | S3, Redshift, OpenSearch, 3rd party |
| **Transformation** | Via consumer code | Lambda integration |
| **Record Size** | 1 MB max | 1 MB max |

**Decision Guide:**
- Need replay/reprocess? → **Kinesis Data Streams**
- Simple load to S3/Redshift? → **Data Firehose**
- Custom real-time processing? → **Kinesis Data Streams**
- No infrastructure management? → **Data Firehose**

### Kinesis Data Streams vs Amazon MSK

| Aspect | Kinesis Data Streams | Amazon MSK |
|--------|---------------------|------------|
| **Technology** | AWS proprietary | Apache Kafka |
| **Message Size** | 1 MB (hard limit) | 1 MB default (configurable 10MB+) |
| **Data Structure** | Streams → Shards | Topics → Partitions |
| **Scaling** | Shard split/merge | Add partitions only |
| **In-flight Encryption** | TLS | PLAINTEXT or TLS |
| **At-rest Encryption** | KMS | KMS |
| **Authentication** | IAM only | Mutual TLS, SASL/SCRAM, IAM |
| **Authorization** | IAM only | Kafka ACLs or IAM |
| **Learning Curve** | Lower | Higher (Kafka knowledge) |
| **Ecosystem** | AWS-native | Kafka ecosystem |

**Decision Guide:**
- AWS-native, simple setup? → **Kinesis**
- Existing Kafka expertise? → **MSK**
- Need messages >1MB? → **MSK**
- Need Kafka Connect/ecosystem? → **MSK**

### Complete Streaming Services Comparison

| Service | Use Case | Latency | Storage | Replay | Scaling |
|---------|----------|---------|---------|--------|---------|
| Kinesis Data Streams | Collect streaming data | Real-time | 365 days | Yes | Manual/On-Demand |
| Data Firehose | Load to destinations | Near real-time | None | No | Automatic |
| Kinesis Analytics | Query streams | Real-time | N/A | N/A | Automatic |
| Amazon MSK | Kafka workloads | Real-time | Configurable | Yes | Add brokers/partitions |
| MSK Serverless | Serverless Kafka | Real-time | Configurable | Yes | Automatic |

---

## Data Format Comparisons

### Row vs Columnar Formats

| Format | Type | Schema | Compression | Best For |
|--------|------|--------|-------------|----------|
| CSV | Row | No schema | Poor | Simple interchange |
| JSON | Row | Flexible | Poor | APIs, documents |
| Avro | Row | Embedded, evolves | Good | Streaming, Kafka |
| Parquet | Columnar | Embedded | Excellent | Analytics, ML |
| ORC | Columnar | Embedded | Excellent | Hive workloads |

### Format Selection Guide

| Use Case | Recommended Format |
|----------|--------------------|
| Data streaming (Kafka/Kinesis) | Avro |
| Analytics queries (Athena) | Parquet |
| Data lake storage | Parquet |
| ML training data | Parquet or CSV |
| Schema needs to evolve | Avro |
| Hive/Hadoop ecosystem | ORC |
| Human-readable config | JSON |
| Simple data exchange | CSV |

---

## Kinesis Capacity Mode Comparison

### Provisioned vs On-Demand

| Aspect | Provisioned | On-Demand |
|--------|-------------|-----------|
| **Capacity Planning** | You choose shards | AWS manages |
| **Scaling** | Manual shard split/merge | Automatic |
| **Default Throughput** | Per shard limits | 4 MB/s in |
| **Cost Model** | Per shard per hour | Per stream + per GB |
| **Best For** | Predictable workloads | Variable/unknown workloads |

**Provisioned Per-Shard Limits:**
- Write: 1 MB/s or 1,000 records/sec
- Read: 2 MB/s or 5 GetRecords/sec

---

## S3 Access Control Comparison

| Method | Scope | Cross-Account | Use Case |
|--------|-------|---------------|----------|
| IAM Policies | User/Role | Via bucket policy | User permissions |
| Bucket Policies | Bucket | Yes | Public access, cross-account |
| ACLs | Object/Bucket | Limited | Legacy, avoid |
| Access Points | Bucket subset | Yes | Many users, specific prefixes |

---

## MSK Authentication Comparison

| Method | Authentication | Authorization | Complexity | Use Case |
|--------|----------------|---------------|------------|----------|
| Mutual TLS | X.509 certificates | Kafka ACLs | High | Enterprise, cert infrastructure |
| SASL/SCRAM | Username/password | Kafka ACLs | Medium | Simple auth needs |
| IAM Access Control | IAM credentials | IAM policies | Low | AWS-native integration |

---

## Quick Reference: "Which Service?" Decision Tree

### Storage Decision
```
Need object storage? → S3
Need block storage for EC2? → EBS
Need shared Linux file system? → EFS
Need Windows file server? → FSx for Windows
Need HPC/ML high-throughput? → FSx for Lustre
Need multi-protocol enterprise? → FSx for NetApp ONTAP
```

### Streaming Decision
```
Need real-time + replay? → Kinesis Data Streams
Need simple ETL to S3? → Data Firehose
Need Kafka ecosystem? → MSK
Need stream SQL/analytics? → Kinesis Data Analytics
Need anomaly detection? → RANDOM_CUT_FOREST in KDA
```

### Encryption Decision
```
Simple encryption? → SSE-S3
Need audit trail? → SSE-KMS
Customer manages keys? → SSE-C or Client-Side
```
