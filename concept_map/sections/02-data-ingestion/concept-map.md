# Section 2: Data Ingestion and Storage

## Overview
This section covers AWS services and concepts for ingesting, storing, and streaming data for ML workloads. Key areas include data architecture patterns, storage services (S3, EBS, EFS, FSx), and real-time streaming (Kinesis, MSK).

## Core Concepts

### [[Data Architecture Patterns]]

#### Data Warehouse
- **Structured data** from operational systems
- Schema defined upfront (schema-on-write)
- Optimized for SQL queries and BI
- AWS Service: [[Amazon Redshift]]

#### Data Lake
- **Raw data** in any format (structured, semi-structured, unstructured)
- Schema applied at read time (schema-on-read)
- Low-cost storage for massive volumes
- AWS Service: [[Amazon S3]]

#### Data Lakehouse
- **Combines** Data Lake + Data Warehouse benefits
- Raw storage with structured query layer
- Supports both BI and ML workloads
- AWS Services: S3 + [[AWS Glue]] + [[Amazon Athena]]

#### Data Mesh
- **Decentralized** data ownership by domain teams
- Data as a product philosophy
- Federated governance with central standards
- Self-service data infrastructure

### [[ETL vs ELT]]

| Aspect | ETL | ELT |
|--------|-----|-----|
| Transform Location | Before loading | After loading |
| Speed | Slower (pre-processing) | Faster (load raw) |
| Flexibility | Less flexible | More flexible |
| Best For | Traditional warehouses | Modern data lakes |

### [[Data Formats]]

| Format | Type | Best For | Key Feature |
|--------|------|----------|-------------|
| CSV | Row-based | Simple interchange | Human readable |
| JSON | Row-based | APIs, documents | Flexible schema |
| Avro | Row-based | Streaming, Kafka | Schema evolution |
| Parquet | Columnar | Analytics, ML | Column pruning |
| ORC | Columnar | Hive workloads | High compression |

**Exam Tip**: Parquet = columnar = analytics; Avro = row-based = streaming

---

## AWS Storage Services

### [[Amazon S3]] - Object Storage

#### Key Characteristics
- **Infinitely scalable** object storage
- Objects: 0 bytes to 5TB (multi-part upload for >100MB)
- 11 9s (99.999999999%) durability
- Regional service with global namespace

#### Storage Classes

| Class | Availability | Min Storage | Use Case |
|-------|--------------|-------------|----------|
| Standard | 99.99% | None | Frequent access |
| Intelligent-Tiering | 99.9% | None | Unknown patterns |
| Standard-IA | 99.9% | 30 days | Infrequent access |
| One Zone-IA | 99.5% | 30 days | Recreatable data |
| Glacier Instant | 99.9% | 90 days | Instant archive access |
| Glacier Flexible | 99.99% | 90 days | Minutes-hours retrieval |
| Glacier Deep Archive | 99.99% | 180 days | 12-48 hour retrieval |

#### S3 Security

**Encryption Options:**
| Type | Key Management | Use Case |
|------|----------------|----------|
| SSE-S3 | AWS managed | Default, simple |
| SSE-KMS | Customer managed in KMS | Audit trail, key control |
| SSE-C | Customer provided | Full key control |
| Client-Side | Customer managed | Encrypt before upload |

**Access Control:**
- IAM Policies (user-based)
- Bucket Policies (resource-based, cross-account)
- ACLs (legacy, object-level)
- Access Points (simplified access for many users)

#### S3 Performance
- 3,500 PUT/POST/DELETE per prefix per second
- 5,500 GET/HEAD per prefix per second
- **Optimization**: Spread across prefixes, use Transfer Acceleration

#### S3 Features
- **Versioning**: Keep all object versions, protect against deletion
- **Replication**: CRR (cross-region) or SRR (same-region)
- **Lifecycle Rules**: Automate transitions between storage classes
- **Event Notifications**: Trigger Lambda, SQS, SNS, EventBridge
- **Object Lambda**: Transform data on retrieval

---

### [[Amazon EBS]] - Block Storage

- **Attached to single EC2** instance (except Multi-Attach io1/io2)
- Network-attached, persists independently of instance
- Locked to single AZ

**Volume Types:**

| Type | IOPS | Use Case |
|------|------|----------|
| gp3 | 16,000 | General purpose, cost-effective |
| gp2 | 3 IOPS/GB (max 16,000) | General purpose, burstable |
| io2 Block Express | 256,000 | Highest performance |
| st1 | 500 | Throughput-optimized HDD |
| sc1 | 250 | Cold HDD, lowest cost |

**Key Features:**
- Snapshots (backup to S3, cross-AZ/region copy)
- Elastic Volumes (resize without detaching)
- Encryption with KMS

---

### [[Amazon EFS]] - File Storage (NFS)

- **Managed NFS** file system
- **Multi-AZ** by default, shared across instances
- **Linux only** (POSIX compliant)
- Scales automatically (pay per use)

**Performance Modes:**
| Mode | Latency | Throughput | Use Case |
|------|---------|------------|----------|
| General Purpose | Low | Standard | Web serving, CMS |
| Max I/O | Higher | Higher | Big data, media |

**Storage Classes:**
- Standard + Standard-IA
- One Zone + One Zone-IA

---

### [[Amazon FSx]] - High-Performance File Systems

| FSx Type | Protocol | OS Support | Best For |
|----------|----------|------------|----------|
| **Lustre** | Lustre | Linux | HPC, ML, high-throughput |
| **Windows** | SMB | Windows | Windows workloads, AD |
| **NetApp ONTAP** | NFS, SMB, iSCSI | All | Multi-protocol enterprise |
| **OpenZFS** | NFS | All | ZFS migration, cloning |

**FSx for Lustre:**
- 100s GB/s, millions IOPS, sub-ms latency
- **S3 integration**: Read S3 as file system, write back to S3
- Scratch (temporary, 6x faster) vs Persistent (durable)

---

## Real-Time Streaming Services

### [[Amazon Kinesis Data Streams]]

- **Collect and store** streaming data in real-time
- Retention: up to 365 days
- **Replay capability** - can reprocess data
- Record size: up to 1 MB

**Capacity Modes:**
| Mode | Scaling | Pricing |
|------|---------|---------|
| Provisioned | Manual (shards) | Per shard/hour |
| On-Demand | Automatic | Per stream + data |

**Provisioned Limits (per shard):**
- Write: 1 MB/s or 1000 records/sec
- Read: 2 MB/s

**Libraries:**
- KPL (Producer Library) - optimized producers
- KCL (Client Library) - optimized consumers

---

### [[Amazon Data Firehose]]
*Formerly: Kinesis Data Firehose*

- **Load streaming data** to destinations
- **Near real-time** (buffered, not instant)
- **No replay** capability
- Fully managed, auto-scaling

**Destinations:** S3, Redshift, OpenSearch, Splunk, HTTP endpoints

**Features:**
- Format conversion to Parquet/ORC
- Compression (gzip, snappy)
- Lambda transformations

---

### [[Kinesis Data Analytics]] / [[Managed Service for Apache Flink]]

- **Real-time analytics** on streaming data
- SQL queries or custom Flink applications (Java, Python, Scala)
- Reference tables from S3 for JOINs
- **RANDOM_CUT_FOREST**: Anomaly detection function

**Pricing:** KPU (Kinesis Processing Unit) = 1 vCPU + 4GB

---

### [[Amazon MSK]] - Managed Streaming for Apache Kafka

- **Alternative to Kinesis** for Kafka workloads
- Manages broker nodes and Zookeeper
- Multi-AZ deployment (up to 3 AZs)
- Message size: 1MB default, configurable to 10MB+

**Authentication Options:**
- Mutual TLS + Kafka ACLs
- SASL/SCRAM + Kafka ACLs
- IAM Access Control

**Variants:**
- MSK Connect - Managed Kafka Connect workers
- MSK Serverless - No capacity management

---

## Concept Relationships

```
                    ┌─────────────────┐
                    │   Data Sources  │
                    │ (IoT, Apps, DBs)│
                    └────────┬────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │ Kinesis Data  │ │ Amazon MSK    │ │ AWS Glue      │
    │ Streams       │ │ (Kafka)       │ │ (Batch ETL)   │
    │ (Real-time)   │ │ (Real-time)   │ │               │
    └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
            │                 │                 │
            ▼                 ▼                 ▼
    ┌───────────────────────────────────────────────────┐
    │              Amazon S3 (Data Lake)                │
    │  ┌─────────┐  ┌─────────┐  ┌─────────────────┐   │
    │  │ Raw     │→ │Processed│→ │ ML-Ready        │   │
    │  │ Data    │  │ Data    │  │ (Parquet/CSV)   │   │
    │  └─────────┘  └─────────┘  └─────────────────┘   │
    └───────────────────────────────────────────────────┘
            │                 │                 │
            ▼                 ▼                 ▼
    ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
    │ SageMaker     │ │ Athena        │ │ Redshift      │
    │ (ML Training) │ │ (Query)       │ │ (Warehouse)   │
    └───────────────┘ └───────────────┘ └───────────────┘
```

---

## Exam Tips

### Storage Selection
- **S3**: Object storage, data lake, any file type
- **EBS**: Block storage for single EC2, databases
- **EFS**: Shared file system, Linux, multi-AZ
- **FSx Lustre**: HPC/ML, S3 integration, high throughput

### Streaming Selection
- **Kinesis Data Streams**: Real-time, replay needed, custom processing
- **Data Firehose**: Simple ETL to S3/Redshift, no replay
- **MSK**: Need Kafka ecosystem, larger messages

### Key Differentiators
| Question Pattern | Answer |
|------------------|--------|
| "Replay data" | Kinesis Data Streams |
| "Near real-time to S3" | Data Firehose |
| "Anomaly detection streaming" | RANDOM_CUT_FOREST |
| "Schema evolution" | Avro format |
| "Analytics/column queries" | Parquet format |
| "HPC/ML file storage" | FSx for Lustre |
| "Windows file server" | FSx for Windows |

### S3 Encryption Quick Reference
- Default encryption → SSE-S3
- Audit key usage → SSE-KMS
- Client controls keys → SSE-C or Client-Side

---

## Related Sections
- [[03-data-transformation]] - Glue, EMR for processing
- [[06-model-training]] - SageMaker training data sources
- [[09-mlops]] - Data pipelines and automation
