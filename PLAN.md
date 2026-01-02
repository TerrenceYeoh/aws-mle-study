# AWS MLE Study - Concept Map Creation Plan

## Goal
Create efficient learning materials from 13 dense PDF sections (~100 pages each):
- **Concept Maps** → Understand relationships
- **Comparison Tables** → "Which service?" exam questions

---

## Chunked Processing Strategy

### Why Chunking?
- PDFs are ~100 pages each
- API error 413 occurred when processing full Section 2
- Solution: Read in 40-page chunks, synthesize incrementally

### Processing Flow Per Section
```
┌─────────────────────────────────────────────────────────┐
│  For each section PDF (~100 pages):                     │
├─────────────────────────────────────────────────────────┤
│  Step 1: Read pages 1-40                                │
│          → Extract concepts, services, key points       │
│          → Write to _WIP file                           │
│                                                         │
│  Step 2: Read pages 41-80                               │
│          → Extract concepts, services, key points       │
│          → Append to _WIP file                          │
│                                                         │
│  Step 3: Read pages 81-end                              │
│          → Extract remaining content                    │
│          → Append to _WIP file                          │
│                                                         │
│  Step 4: Synthesize into final outputs                  │
│          → concept-map.md                               │
│          → comparison-tables.md                         │
│          → Remove _WIP file                             │
│                                                         │
│  Step 5: Checkpoint                                     │
│          → Update PLAN.md progress                      │
│          → Clear context for next section               │
└─────────────────────────────────────────────────────────┘
```

### Safeguards
| Risk | Mitigation |
|------|------------|
| PDF too large | Read in **15-page chunks** (proven to work) |
| Context overflow | Save after each section, don't accumulate |
| API 413 error | See "413 Error Prevention" below |
| Session interrupt | PLAN.md tracks progress, can resume |
| Lost work | Write to disk immediately after each chunk |

### 413 Error Prevention (IMPORTANT)
The original 40-page chunk strategy caused 413 errors. **15-page chunks work reliably.**

**Pre-split PDFs before processing:**
```bash
# Use a PDF splitter to create chunks like:
section05_chunks/
├── 5-Sagemaker-Built-In-Algorithms_chunk01_pages1-15.pdf
├── 5-Sagemaker-Built-In-Algorithms_chunk02_pages16-30.pdf
└── ...
```

**If 413 still occurs:**
1. Reduce to 10-page chunks
2. Process one chunk, write to _WIP immediately
3. Never accumulate multiple chunks in context before writing

**Proven chunk sizes:**
| Section | Chunk Size | Result |
|---------|------------|--------|
| 02 | 40 pages | 413 error |
| 05 | 15 pages | Success (8 chunks) |

---

## Output Structure

```
concept_map/
├── 00-master-concept-map.md          # Existing overview
├── sections/
│   ├── 01-introduction/
│   │   ├── concept-map.md
│   │   └── comparison-tables.md
│   ├── 02-data-ingestion/
│   │   ├── concept-map.md
│   │   └── comparison-tables.md
│   ├── 03-data-transformation/
│   ├── 04-managed-ai-services/
│   ├── 05-sagemaker-algorithms/
│   ├── 06-model-training/
│   ├── 07-genai-fundamentals/
│   ├── 08-bedrock-applications/
│   ├── 09-mlops/
│   ├── 10-security-compliance/
│   ├── 11-management-governance/
│   ├── 12-ml-best-practices/
│   └── 13-exam-preparation/
└── consolidated/                      # Created after all sections done
    ├── all-service-comparisons.md
    └── quick-reference.md
```

### Per-Section Output Format

**concept-map.md:**
```markdown
# Section Title

## Overview
Brief summary, key takeaways

## Core Concepts
### [[Concept-Name]]
- Definition
- Key points
- Related: [[Other-Concept]], [[AWS-Service]]

## AWS Services
### [[Service-Name]]
- Purpose
- Use cases
- Key features

## Concept Relationships
(ASCII or description of how concepts connect)

## Exam Tips
- Important points
- Common question patterns
```

**comparison-tables.md:**
```markdown
# Section Title - Comparisons

## Service Comparisons
| Criteria | Service A | Service B | When to Use |
|----------|-----------|-----------|-------------|

## Concept Comparisons
| Aspect | Concept A | Concept B |
|--------|-----------|-----------|
```

---

## Progress Tracker

### Current Status
- **Last Completed Section**: Section 13 (Exam Preparation)
- **Next Section**: ALL SECTIONS COMPLETE!
- **Progress**: 13/13 sections complete (100%)

### Section Checklist
| Section | PDF File | Status | Chunk Progress |
|---------|----------|--------|----------------|
| 01 | 1-AWS-Certified-ML-Engineer-Associate-Slides-Introduction.pdf | ✅ Complete | Done |
| 02 | 2-Data-Ingestion-and-Storage.pdf | ✅ Complete | Done (8 chunks) |
| 03 | 3-Data-Transformation-Integrity-and-Feature-Engineering.pdf | ✅ Complete | Done (9 chunks) |
| 04 | 4-AWS-Managed-AI-Services.pdf | ✅ Complete | Done (3 chunks) |
| 05 | 5-Sagemaker-Built-In-Algorithms.pdf | ✅ Complete | Done (8 chunks) |
| 06 | 6-Model-Training-Tuning-and-Evaluation.pdf | ✅ Complete | Done (8 chunks) |
| 07 | 7-Generative-AI-Model-Fundamentals.pdf | ✅ Complete | Done (2 chunks) |
| 08 | 8-Building-Generative-AI-Applications-With-Bedrock.pdf | ✅ Complete | Done (2 chunks) |
| 09 | 9-Machine-Learning-Operations-(MLOps).pdf | ✅ Complete | Done (7 chunks) |
| 10 | 10-Security-Identity-and-Compliance.pdf | ✅ Complete | Done (4 chunks) |
| 11 | 11-Management-and-Governance.pdf | ✅ Complete | Done (5 chunks) |
| 12 | 12-ML-Best-Practices.pdf | ✅ Complete | Done (3 chunks) |
| 13 | 13-Exam-Preparation.pdf | ✅ Complete | Done (2 chunks) |

---

## Resume Instructions

If context limit or API error occurs:

1. **Check this file** for "Current Status" section
2. **Find the last checkpoint** in Section Checklist
3. **Resume command**:
   ```
   Continue from Section XX, chunk Y. Check PLAN.md for progress.
   ```
4. **Look for _WIP files** - they contain partial progress

---

## Linking Strategy

### Cross-Section Links
- Format: `[[02-data-ingestion/concept-map#S3]]`
- Common hubs: [[SageMaker]], [[S3]], [[IAM]], [[Bedrock]]

### Service Categories for Linking
- **Storage**: [[S3]], [[EBS]], [[EFS]], [[FSx]]
- **Processing**: [[Kinesis]], [[Glue]], [[EMR]]
- **ML Platform**: [[SageMaker]], [[Bedrock]]
- **Security**: [[IAM]], [[KMS]], [[VPC]], [[Secrets-Manager]]
- **Monitoring**: [[CloudWatch]], [[CloudTrail]], [[X-Ray]]
