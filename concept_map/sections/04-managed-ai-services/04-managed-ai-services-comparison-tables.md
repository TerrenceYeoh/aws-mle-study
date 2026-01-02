# Section 4: AWS Managed AI Services - Comparison Tables

## Speech Services Comparison

### Transcribe vs Polly

| Criteria | Amazon Transcribe | Amazon Polly |
|----------|-------------------|--------------|
| **Direction** | Speech → Text | Text → Speech |
| **Use Case** | Transcription, captioning | Voice interfaces, accessibility |
| **Customization** | Custom vocabularies, language models | Lexicons, SSML |
| **Key Feature** | Toxicity detection, PII redaction | Speech marks, multiple voice engines |

---

## Text/NLP Service Comparisons

### Comprehend vs Textract vs Translate

| Criteria | Comprehend | Textract | Translate |
|----------|------------|----------|-----------|
| **Purpose** | Understand text meaning | Extract text from documents | Convert between languages |
| **Input** | Text | Images, PDFs, scanned docs | Text |
| **Output** | Sentiment, entities, topics | Structured text, forms, tables | Translated text |
| **Custom Models** | Yes (classification, NER) | No | No |

---

### Comprehend Capabilities

| Capability | Description | Custom Version |
|------------|-------------|----------------|
| **Sentiment** | Positive/negative analysis | No |
| **Entity Recognition** | People, places, orgs, dates | Yes (Custom NER) |
| **Classification** | Categorize documents | Yes (Custom Classification) |
| **Key Phrases** | Extract important phrases | No |
| **Language Detection** | Identify language | No |
| **Topic Modeling** | Group by topic | No |

---

## Vision Service Comparisons

### Rekognition Features

| Feature | API | Use Case |
|---------|-----|----------|
| **Object Detection** | DetectLabels | Find objects, scenes |
| **Face Analysis** | DetectFaces | Age, gender, emotions |
| **Face Comparison** | CompareFaces | Verify identity |
| **Celebrity Recognition** | RecognizeCelebrities | Identify famous people |
| **Content Moderation** | DetectModerationLabels | Filter inappropriate content |
| **Text in Images** | DetectText | OCR |
| **Custom Labels** | Custom model | Domain-specific classification |

---

## Recommendation & Search Comparisons

### Personalize vs Kendra

| Criteria | Amazon Personalize | Amazon Kendra |
|----------|-------------------|---------------|
| **Purpose** | Product/content recommendations | Document search |
| **Output** | Ranked item list | Search results with answers |
| **Learning** | User interaction data | User feedback (relevance) |
| **Best For** | E-commerce, media | Enterprise knowledge bases |

---

### Personalize Recipe Categories

| Category | Recipe | Use Case |
|----------|--------|----------|
| **USER_PERSONALIZATION** | User-Personalization-v2 | "Recommended for you" |
| **PERSONALIZED_RANKING** | Personalized-Ranking-v2 | Re-rank search results |
| **POPULAR_ITEMS** | Trending-Now | "Trending now" section |
| **POPULAR_ITEMS** | Popularity-Count | Most popular items |
| **RELATED_ITEMS** | Similar-Items | "Customers also bought" |
| **PERSONALIZED_ACTIONS** | Next-Best-Action | Next best action to take |
| **USER_SEGMENTATION** | Item-Affinity | Create user segments |

---

## Chatbot & Conversational AI

### Lex Components

| Component | Description | Example |
|-----------|-------------|---------|
| **Intent** | What user wants to accomplish | BookHotel, OrderPizza |
| **Slot** | Information needed to fulfill | City, Date, RoomType |
| **Utterance** | Ways user expresses intent | "I want to book a hotel" |
| **Fulfillment** | Action to complete request | Lambda function |

### Lex Integrations

| Service | Purpose |
|---------|---------|
| **Lambda** | Execute fulfillment logic |
| **Connect** | Call center integration |
| **Comprehend** | Sentiment analysis |
| **Kendra** | Search integration |

---

## Anomaly & Fraud Detection

### Lookout Services Comparison

| Service | Data Type | Use Case |
|---------|-----------|----------|
| **Lookout for Metrics** | Business metrics | Ad campaign, sales anomalies |
| **Lookout for Equipment** | Sensor data | Predictive maintenance |
| **Lookout for Vision** | Images | Quality inspection, defects |

---

### Fraud Detector vs Lookout for Metrics

| Criteria | Fraud Detector | Lookout for Metrics |
|----------|----------------|---------------------|
| **Purpose** | Detect fraud | Detect anomalies |
| **Focus** | Fraudulent transactions/accounts | Business metric deviations |
| **Output** | Fraud score + rules | Anomaly alerts |
| **Learning** | Your labeled fraud data | Unsupervised anomaly detection |

---

## Human Review Options

### A2I Reviewer Sources

| Source | Description | Best For |
|--------|-------------|----------|
| **Internal Team** | Your own employees | Sensitive data |
| **Mechanical Turk** | Crowd workers | Scale, cost efficiency |
| **AWS Contractors** | 500,000+ vetted workers | Quality at scale |
| **Pre-screened Vendors** | Professional services | Confidentiality required |

---

## Generative AI Comparisons

### Q Business vs Q Developer

| Criteria | Q Business | Q Developer |
|----------|------------|-------------|
| **Target Users** | Business employees | Developers |
| **Data Source** | Company internal data (40+ connectors) | AWS documentation + account |
| **Use Cases** | Q&A, content gen, task automation | Code, CLI, troubleshooting |
| **Authentication** | IAM Identity Center | AWS credentials |
| **Underlying Tech** | Amazon Bedrock | Amazon Bedrock |

---

### Q Developer Features

| Feature Category | Capabilities |
|-----------------|--------------|
| **AWS Knowledge** | Documentation, CLI commands, cost analysis |
| **Code Assistance** | Completions, generation, debugging |
| **Security** | Vulnerability scanning |
| **IDEs** | VS Code, Visual Studio, JetBrains |

---

## AI Hardware Comparisons

### Trainium vs Inferentia

| Criteria | AWS Trainium | AWS Inferentia |
|----------|--------------|----------------|
| **Purpose** | Model training | Model inference |
| **Instance Type** | Trn1 | Inf1, Inf2 |
| **Cost Savings** | 50% vs GPU | 70% vs GPU |
| **Throughput** | High (training) | 4x improvement |
| **Model Size** | 100B+ parameters | Optimized inference |
| **Environment** | Lowest footprint | Lowest footprint |

### GPU Instance Types

| Instance Family | Use Case |
|-----------------|----------|
| **P3, P4, P5** | Training (NVIDIA) |
| **G3, G4, G5, G6** | Graphics, inference |
| **Trn1** | Training (Trainium) |
| **Inf1, Inf2** | Inference (Inferentia) |

---

## Quick Reference Decision Trees

### Text Processing Decision

```
Need to process text?
├── Understand meaning/sentiment → Comprehend
├── Extract from documents/images → Textract
├── Translate between languages → Translate
├── Search documents → Kendra
└── Custom classification → Comprehend Custom
```

### Speech Processing Decision

```
Speech processing needed?
├── Audio to text → Transcribe
│   ├── Custom terms → Custom Vocabulary
│   └── Domain-specific → Custom Language Model
└── Text to audio → Polly
    ├── Custom pronunciation → Lexicons
    └── Fine control → SSML
```

### Image/Video Decision

```
Analyze images/video?
├── Standard detection → Rekognition
│   ├── Objects/scenes → DetectLabels
│   ├── Faces → DetectFaces
│   ├── Moderation → DetectModerationLabels
│   └── Text/OCR → DetectText
└── Custom categories → Rekognition Custom Labels
```

### Recommendations Decision

```
Need recommendations?
├── Product recommendations → Personalize
│   ├── For specific user → User-Personalization-v2
│   ├── Re-rank results → Personalized-Ranking-v2
│   ├── Trending items → Trending-Now
│   └── Similar items → Similar-Items
└── Document search → Kendra
```

### Anomaly/Fraud Decision

```
Detect anomalies or fraud?
├── Fraudulent transactions → Fraud Detector
├── Business metric anomalies → Lookout for Metrics
├── Equipment/sensor anomalies → Lookout for Equipment
└── Visual quality issues → Lookout for Vision
```

### Gen-AI Assistant Decision

```
Need AI assistant?
├── For business employees → Q Business
│   └── No-code apps → Q Apps
├── For developers → Q Developer
└── Custom FM deployment → Amazon Bedrock
```

---

## Exam Pattern Quick Answers

| Question Pattern | Answer |
|------------------|--------|
| "NLP sentiment analysis" | Amazon Comprehend |
| "Custom document classification" | Comprehend Custom Classification |
| "Extract entities from text" | Comprehend NER |
| "Speech to text with PII redaction" | Amazon Transcribe |
| "Improve transcription accuracy" | Custom Vocabularies + Custom Language Models |
| "Text to speech with custom pronunciation" | Amazon Polly (Lexicons/SSML) |
| "Detect inappropriate images" | Rekognition Content Moderation |
| "Build chatbot with voice/text" | Amazon Lex |
| "Intent + Slots + Fulfillment" | Amazon Lex |
| "Product recommendations" | Amazon Personalize |
| "Rank items for specific user" | Personalize (Personalized-Ranking-v2) |
| "Extract text from scanned documents" | Amazon Textract |
| "Enterprise document search" | Amazon Kendra |
| "Human review of ML predictions" | Amazon A2I |
| "Detect online payment fraud" | Amazon Fraud Detector |
| "Business metric anomalies" | Lookout for Metrics |
| "Predictive maintenance from sensors" | Lookout for Equipment |
| "Visual quality inspection" | Lookout for Vision |
| "Gen-AI for business employees" | Amazon Q Business |
| "Gen-AI code assistant" | Amazon Q Developer |
| "No-code Gen-AI apps" | Amazon Q Apps |
| "Cost-effective ML training chip" | AWS Trainium (Trn1) |
| "Cost-effective ML inference chip" | AWS Inferentia (Inf1, Inf2) |
| "Low environmental footprint AI" | Trainium or Inferentia |
| "40+ enterprise data connectors" | Q Business Data Connectors |
| "Guard against inappropriate topics" | Q Business Admin Controls |
| "Reduce content moderation costs" | Rekognition + A2I (1-5% human review) |
| "Custom image classifier with few images" | Rekognition Custom Labels |
