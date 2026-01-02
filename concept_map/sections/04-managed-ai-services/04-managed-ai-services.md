# Section 4: AWS Managed AI Services

## Overview
This section covers AWS pre-trained AI/ML services for common use cases including NLP, speech, vision, recommendations, document processing, and generative AI. These services provide token-based pricing, redundancy across AZs, and specialized hardware for cost efficiency.

---

## Service Categories

| Category | Services |
|----------|----------|
| **Generative AI** | Amazon Bedrock, Amazon Q Business, Amazon Q Developer, SageMaker JumpStart |
| **Text & Documents** | Comprehend, Translate, Textract |
| **Vision** | Rekognition |
| **Search** | Kendra |
| **Chatbots** | Lex |
| **Speech** | Polly, Transcribe |
| **Recommendations** | Personalize |
| **Fraud/Anomaly** | Fraud Detector, Lookout |
| **Human Review** | Amazon A2I |

---

## Natural Language Processing

### Amazon Comprehend

**Purpose:** Fully managed, serverless NLP service

**Built-in Capabilities:**

| Capability | Description |
|------------|-------------|
| **Language Detection** | Identify text language |
| **Key Phrase Extraction** | Extract places, people, brands, events |
| **Sentiment Analysis** | Positive/negative sentiment |
| **Tokenization** | Parts of speech analysis |
| **Topic Modeling** | Organize documents by topic |

**Named Entity Recognition (NER):**
- Person, Organization, Location, Date, Quantity
- Account numbers, routing numbers

**Custom Features:**

| Feature | Purpose | Training |
|---------|---------|----------|
| **Custom Classification** | Organize docs into YOUR categories | Labeled data → S3 |
| **Custom Entity Recognition** | Extract business-specific terms | Entity list + documents |

**Analysis Modes:**
- **Real-time:** Single document, synchronous
- **Async:** Multiple documents (batch), asynchronous

**Cross-Account Sharing:**
- Attach IAM policy to model version
- Must be in **same region**
- Need ARN, region, optional KMS key

---

### Amazon Translate

**Purpose:** Natural language translation

**Features:**
- Auto-detect source language
- Multiple target languages
- Localize websites and applications
- Translate large volumes efficiently

---

## Speech Services

### Amazon Transcribe

**Purpose:** Convert speech to text (ASR - Automatic Speech Recognition)

**Key Features:**

| Feature | Description |
|---------|-------------|
| **PII Redaction** | Automatically remove personally identifiable information |
| **Language Identification** | Auto-detect language in multi-lingual audio |
| **Toxicity Detection** | ML-powered using tone, pitch, and text cues |

**Toxicity Categories:**
- Profanity, Hate speech, Sexual content
- Insults, Violence/threats, Graphic content
- Harassment/abuse

**Improving Accuracy:**

| Method | Purpose | Best For |
|--------|---------|----------|
| **Custom Vocabularies** | Add specific words/phrases | Brand names, acronyms, jargon |
| **Custom Language Models** | Train on domain-specific text | Large volumes of domain speech |

**Best Practice:** Use BOTH for highest accuracy

**Example:** "AWS Microservices" → "A USA My crow services" without customization

---

### Amazon Polly

**Purpose:** Text-to-Speech (TTS) using deep learning

**Features:**

| Feature | Description |
|---------|-------------|
| **Lexicons** | Define pronunciation (e.g., "AWS" → "Amazon Web Services") |
| **SSML** | Speech Synthesis Markup Language for pronunciation control |
| **Voice Engines** | Generative, long-form, neural, standard |
| **Speech Marks** | Encode word/sentence positions for lip-sync or highlighting |

**SSML Tags:**
- `<break>` - Add pause
- `<emphasis>` - Emphasize words
- `<prosody>` - Control volume, rate, pitch
- `<phoneme>` - Phonetic pronunciation
- `<sub>` - Pronounce acronyms/abbreviations

---

## Vision Services

### Amazon Rekognition

**Purpose:** Image and video analysis using ML

**Capabilities:**

| Feature | Description |
|---------|-------------|
| **Object Detection** | Find objects, people, text, scenes |
| **Facial Analysis** | Gender, age range, emotions |
| **Face Search** | Compare against database of faces |
| **Celebrity Recognition** | Identify celebrities |
| **Content Moderation** | Detect inappropriate content |
| **Text Detection** | OCR in images |
| **Pathing** | Track movement (e.g., sports analysis) |

**Custom Labels:**
- Only needs **a few hundred images or less**
- Label images → Upload to S3 → Rekognition creates model
- Use cases: Company logos, product identification

**Content Moderation:**
- Reduces human review to **1-5% of total content**
- Integrated with **Amazon A2I** for human review
- **Custom Moderation Adaptors:** Train on your labeled images
- API: `DetectModerationLabels`

---

## Conversational AI

### Amazon Lex

**Purpose:** Build conversational chatbots using voice and text

**Key Concepts:**

| Concept | Description |
|---------|-------------|
| **Intent** | User's goal (e.g., "BookHotel") |
| **Slots** | Input parameters (e.g., city, date) |
| **Fulfillment** | Lambda function to execute the action |

**Integrations:**
- AWS Lambda (fulfillment)
- Amazon Connect (call center)
- Amazon Comprehend (sentiment)
- Amazon Kendra (search)

**Features:**
- Supports multiple languages
- Auto-understands user intent
- Prompts for missing slots

---

## Recommendations

### Amazon Personalize

**Purpose:** Real-time personalized recommendations (same technology as Amazon.com)

**Use Cases:**
- Product recommendations
- Re-ranking search results
- Customized direct marketing

**Data Sources:**
- S3 (batch)
- Real-time API integration

**Recipes (Pre-built Algorithms):**

| Recipe Category | Recipe Name | Use Case |
|----------------|-------------|----------|
| **USER_PERSONALIZATION** | User-Personalization-v2 | Recommend items for users |
| **PERSONALIZED_RANKING** | Personalized-Ranking-v2 | Rank items for a user |
| **POPULAR_ITEMS** | Trending-Now, Popularity-Count | Trending/popular items |
| **RELATED_ITEMS** | Similar-Items | Similar items |
| **PERSONALIZED_ACTIONS** | Next-Best-Action | Next best action |
| **USER_SEGMENTATION** | Item-Affinity | User segments |

**Exam Tip:** Personalize = Recommendations

---

## Document Processing

### Amazon Textract

**Purpose:** Extract text, handwriting, and structured data from documents

**Capabilities:**
- OCR for scanned documents
- Extract data from **forms and tables**
- Process PDFs, images

**Industry Use Cases:**

| Industry | Examples |
|----------|----------|
| Financial Services | Invoices, financial reports |
| Healthcare | Medical records, insurance claims |
| Public Sector | Tax forms, ID documents, passports |

---

### Amazon Kendra

**Purpose:** Fully managed enterprise document search powered by ML

**Features:**
- Natural language search
- Extract answers from within documents
- **Incremental Learning:** Learns from user feedback
- Manual fine-tuning (importance, freshness)

**Supported Formats:** Text, PDF, HTML, PowerPoint, Word, FAQs

**Data Sources:**
- S3, RDS
- Google Drive, SharePoint, OneDrive
- Salesforce, ServiceNow
- Custom connectors

---

## Human Review

### Amazon Augmented AI (A2I)

**Purpose:** Human oversight of ML predictions in production

**How It Works:**
1. ML model makes prediction
2. **High-confidence** → returned immediately
3. **Low-confidence** → sent for human review
4. Reviews consolidated (weighted scores)
5. Reviewed data can improve ML models

**Human Reviewers:**
- Your own employees
- 500,000+ AWS contractors
- Mechanical Turk
- Pre-screened vendors for confidentiality

**Works With:** SageMaker, Rekognition, Textract, custom models

---

## Anomaly Detection

### Amazon Lookout

**Purpose:** ML-powered anomaly detection

| Service | Use Case |
|---------|----------|
| **Lookout for Metrics** | Business metrics, ad campaigns |
| **Lookout for Equipment** | Predictive maintenance from sensors |
| **Lookout for Vision** | Quality inspection with computer vision |

**Key Concepts:**
- **Measure:** What you're optimizing
- **Dimensions:** Features that influence the measure
- **Detectors:** Monitor datasets for anomalies

**Lookout for Metrics Integrations:**
- Data: S3, Redshift, Athena, CloudWatch, Salesforce
- Actions: SNS, Lambda
- Supports feedback for fine-tuning

---

### Amazon Fraud Detector

**Purpose:** Detect fraud using ML

**Fraud Types:**
- Online payments
- New account fraud
- Trial program abuse
- Account takeovers

**Features:**
- Fully managed, customized to your data
- **Automatic model creation**
- Continuous learning over time
- Feature importance insights
- Rule-based actions
- SageMaker integration

**Workflow:**
1. Choose business use case
2. Create event type to monitor
3. Define entities associated with event
4. Point to data source
5. Define labels
6. Create IAM permissions
7. Create model → Train → Review → Deploy

---

## AWS AI Hardware

**GPU-based Instances:** P3, P4, P5, G3, G4, G5, G6

| Chip | Purpose | Instances | Benefits |
|------|---------|-----------|----------|
| **AWS Trainium** | Training | Trn1 | 50% cost reduction, 100B+ parameter models |
| **AWS Inferentia** | Inference | Inf1, Inf2 | 4x throughput, 70% cost reduction |

**Key Points:**
- Trn1 has 16 Trainium Accelerators
- Trainium & Inferentia have **lowest environmental footprint**
- Inferentia = inference, Trainium = training

---

## Generative AI Services

### Amazon Q Business

**Purpose:** Fully managed Gen-AI assistant for employees

**Based On:** Amazon Bedrock (cannot choose underlying FM)

**Capabilities:**
- Answer questions from company knowledge
- Provide summaries, generate content
- Automate tasks
- Perform routine actions (time-off requests, meeting invites)

**Data Connectors (40+ sources):**
- AWS: S3, RDS, Aurora, WorkDocs
- Third-Party: Microsoft 365, SharePoint, Slack, Salesforce, Google Drive, Gmail

**Plugins:**
- Built-in: Jira, ServiceNow, Zendesk, Salesforce
- Custom: Connect to any third-party app using APIs

**Security:**
- **Authentication:** IAM Identity Center (required)
- Users only see responses from documents they have access to
- Supports external Identity Providers

**Admin Controls (Guardrails):**
- Block specific words or topics
- Respond only with internal information
- Global controls & topic-level controls

### Amazon Q Apps

**Purpose:** Create Gen-AI powered apps without coding

**Features:**
- Natural language app creation
- Leverages company internal data
- Can use plugins

**Example Apps:** Content Creator, Meeting Notes Summarizer, Interview Question Generator

---

### Amazon Q Developer

**Purpose:** AI assistant for developers and AWS users

**Capabilities:**

| Feature | Description |
|---------|-------------|
| **AWS Documentation** | Answer questions about AWS services |
| **Account Resources** | Query resources in your AWS account |
| **CLI Suggestions** | Suggest AWS CLI commands |
| **Cost Analysis** | Help understand AWS costs |
| **Troubleshooting** | Resolve errors and debug |

**Code Companion Features:**
- Real-time code suggestions
- Security vulnerability scans
- Code generation, debugging, optimization
- Feature implementation
- Documentation generation

**Supported Languages:** Java, JavaScript, Python, TypeScript, C#, and more

**Supported IDEs:** Visual Studio Code, Visual Studio, JetBrains

---

## Concept Relationships

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Input Sources                                 │
│        (Text, Audio, Images, Documents, User Data)                  │
└───────────────────────────┬─────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│     TEXT      │   │    SPEECH     │   │    VISION     │
│  Comprehend   │   │  Transcribe   │   │  Rekognition  │
│  Translate    │   │    Polly      │   │               │
│   Textract    │   │               │   │               │
│    Kendra     │   │               │   │               │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │           CONVERSATIONAL AI            │
        │    Amazon Lex (Intents + Slots)       │
        │    → Lambda Fulfillment               │
        │    → Connect (Call Center)            │
        └───────────────────┬───────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ PERSONALIZE   │   │  FRAUD/ANOMALY │   │ HUMAN REVIEW  │
│ Recommendations│   │ Fraud Detector │   │   Amazon A2I  │
│   Recipes     │   │    Lookout     │   │               │
└───────────────┘   └───────────────┘   └───────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │           GENERATIVE AI               │
        │  ┌─────────────┐  ┌─────────────┐    │
        │  │ Q Business  │  │ Q Developer │    │
        │  │(Enterprise) │  │   (Code)    │    │
        │  └─────────────┘  └─────────────┘    │
        │           ↓                          │
        │     Amazon Bedrock (FMs)             │
        └───────────────────────────────────────┘
```

---

## Exam Tips

### Service Selection Guide

| Scenario | Service |
|----------|---------|
| "NLP sentiment analysis" | Amazon Comprehend |
| "Custom text classification" | Comprehend Custom Classification |
| "Speech to text" | Amazon Transcribe |
| "Text to speech" | Amazon Polly |
| "Image/video analysis" | Amazon Rekognition |
| "Build chatbot" | Amazon Lex |
| "Product recommendations" | Amazon Personalize |
| "Extract text from documents" | Amazon Textract |
| "Enterprise document search" | Amazon Kendra |
| "Human review of ML predictions" | Amazon A2I |
| "Detect fraud" | Amazon Fraud Detector |
| "Anomaly detection in metrics" | Lookout for Metrics |
| "Predictive maintenance" | Lookout for Equipment |
| "Visual quality inspection" | Lookout for Vision |
| "Employee Gen-AI assistant" | Amazon Q Business |
| "Developer AI assistant" | Amazon Q Developer |
| "No-code Gen-AI apps" | Amazon Q Apps |
| "Training acceleration" | AWS Trainium (Trn1) |
| "Inference acceleration" | AWS Inferentia (Inf1, Inf2) |

### Key Differentiators

| Question Pattern | Answer |
|------------------|--------|
| "Personalized recommendations" | Amazon Personalize |
| "Toxicity detection in audio" | Amazon Transcribe |
| "Custom pronunciation in TTS" | Amazon Polly (Lexicons, SSML) |
| "Reduce human content moderation" | Rekognition Content Moderation + A2I |
| "Train custom image classifier easily" | Rekognition Custom Labels |
| "Intent + Slots + Fulfillment" | Amazon Lex |
| "ML-powered document search" | Amazon Kendra |
| "Human oversight for low-confidence predictions" | Amazon A2I |
| "Lowest cost training chip" | AWS Trainium |
| "Lowest cost inference chip" | AWS Inferentia |
| "Gen-AI with company internal data" | Amazon Q Business |
| "IDE code completion" | Amazon Q Developer |

---

## Related Sections
- [[02-data-ingestion/02-data-ingestion]] - Data sources for AI services
- [[03-data-transformation/03-data-transformation]] - Data preparation before AI services
- [[05-sagemaker-algorithms/05-sagemaker-algorithms]] - Custom model training
- [[06-model-training/06-model-training]] - Training techniques
- 07-deployment - Deploying models at scale
