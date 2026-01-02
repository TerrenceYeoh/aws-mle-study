# Section 6: Model Training, Tuning, and Evaluation

## Overview

This section covers deep learning fundamentals, neural network architectures, model tuning and regularization, evaluation metrics, SageMaker training features, and distributed training at scale.

**Key Takeaways:**
- Deep learning uses neural networks with non-linear activation functions
- CNNs for images, RNNs/Transformers for sequences
- Regularization (dropout, early stopping, L1/L2) prevents overfitting
- Evaluation metrics depend on use case: precision vs recall trade-off
- SageMaker provides comprehensive tools: AMT, Autopilot, Debugger, distributed training
- Distributed training enables training models with >1T parameters

---

## Core Concepts

### [[Deep-Learning-Fundamentals]]

**Biological Inspiration:**
- Neurons connected via axons, fire when threshold reached
- Cortical columns process in parallel (similar to GPUs)
- Layers of neurons yield learning behavior

**Frameworks:**
- [[TensorFlow]] / [[Keras]] - Popular, high-level API
- [[MXNet]] - AWS preferred framework
- [[PyTorch]] - Widely used for research

**Related:** [[Neural-Networks]], [[Activation-Functions]], [[GPU-Instances]]

---

### [[Neural-Network-Types]]

| Type | Use Case | Key Feature |
|------|----------|-------------|
| **Feedforward** | General purpose | Basic architecture |
| **CNN** | Image classification | Feature-location invariant |
| **RNN** | Sequences/time-series | Memory cells |
| **LSTM/GRU** | Long sequences | Handles vanishing gradient |
| **Transformer** | NLP, modern AI | Self-attention mechanism |

**Related:** [[CNN]], [[RNN]], [[Transformers]], [[Transfer-Learning]]

---

### [[Activation-Functions]]

**Purpose:** Define output given input signals; enable backpropagation

| Function | Range | Best For | Issue |
|----------|-------|----------|-------|
| **ReLU** | 0 to inf | Hidden layers (default) | Dying ReLU |
| **Leaky ReLU** | -inf to inf | When ReLU fails | - |
| **Sigmoid** | 0 to 1 | Binary output | Vanishing gradient |
| **TanH** | -1 to 1 | RNNs | Vanishing gradient |
| **Softmax** | 0 to 1 (sum=1) | Multi-class output | Single label only |
| **Swish** | ~-0.3 to inf | Very deep (40+ layers) | - |

**Key Problems:**
- **Vanishing Gradient:** Sigmoid/TanH change slowly at extremes
- **Dying ReLU:** Negative inputs produce 0, neuron stops learning

**Related:** [[Vanishing-Gradient]], [[Backpropagation]]

---

### [[CNN-Architecture]]

**Convolutional Neural Networks for Image Processing**

**Pipeline:** Input -> Conv2D -> MaxPooling -> Dropout -> Flatten -> Dense -> Softmax

**Inspired by Visual Cortex:**
- Local receptive fields respond to visual regions
- Higher layers identify increasingly complex features
- Feature-location invariant (finds patterns anywhere in image)

**Specialized Architectures:**
| Architecture | Innovation |
|--------------|------------|
| **LeNet-5** | Early CNN (handwriting) |
| **AlexNet** | Deeper networks |
| **GoogLeNet** | Inception modules |
| **ResNet** | Skip connections |

**Related:** [[Image-Classification]], [[Dropout]], [[MaxPooling]]

---

### [[RNN-Architecture]]

**Recurrent Neural Networks for Sequential Data**

**Use Cases:** Stock prediction, machine translation, image captions, music generation

**Topologies:**
| Pattern | Example |
|---------|---------|
| Seq -> Seq | Stock prices |
| Seq -> Vec | Sentiment analysis |
| Vec -> Seq | Image captioning |
| Seq -> Vec -> Seq | Translation (Encoder-Decoder) |

**Training:** Backpropagation Through Time (BPTT)

**Related:** [[LSTM]], [[GRU]], [[Transformers]]

---

### [[Transformers]]

**Modern NLP Architecture with Self-Attention**

**Key Innovation:** Self-attention mechanism weighs significance of each input part

**Advantages over RNN:**
- Processes entire input at once (not word-by-word)
- Attention provides context
- Better parallelization

**Models:**
| Model | Description |
|-------|-------------|
| **BERT** | Bi-directional encoder |
| **GPT** | Generative pre-trained |
| **DistilBERT** | 40% smaller (knowledge distillation) |

**Related:** [[Transfer-Learning]], [[Hugging-Face]], [[Fine-Tuning]]

---

### [[Transfer-Learning]]

**Leverage Pre-trained Models**

**Why:** NLP models have hundreds of billions of parameters

**Sources:** Hugging Face model hub, SageMaker Deep Learning Containers

**Approaches:**
| Approach | When to Use |
|----------|-------------|
| Fine-tune | Model has more training data (low learning rate) |
| Freeze + new layers | Learn new predictions from old features |
| Retrain from scratch | Different data + compute capacity |
| Use as-is | Training data already matches |

**Related:** [[BERT]], [[Hugging-Face]], [[SageMaker-DLC]]

---

### [[Regularization]]

**Preventing Overfitting**

**Overfitting Signs:** High training accuracy, lower validation accuracy

**Techniques:**
| Technique | How It Works |
|-----------|--------------|
| **Dropout** | Randomly remove neurons during training |
| **Early Stopping** | Stop when validation accuracy decreases |
| **L1 (Lasso)** | Sparse output, feature selection |
| **L2 (Ridge)** | Dense output, all features retained |

**Related:** [[Overfitting]], [[Dropout]], [[L1-L2-Regularization]]

---

### [[Gradient-Problems]]

| Problem | Description | Solutions |
|---------|-------------|-----------|
| **Vanishing Gradient** | Slope approaches zero | LSTM, ResNet, ReLU |
| **Exploding Gradient** | Gradients too large | Gradient clipping |

**Related:** [[LSTM]], [[ResNet]], [[ReLU]]

---

### [[Model-Evaluation-Metrics]]

**Classification Metrics:**
| Metric | Formula | Use When |
|--------|---------|----------|
| **Recall** | TP/(TP+FN) | Care about false negatives (fraud) |
| **Precision** | TP/(TP+FP) | Care about false positives (medical) |
| **F1 Score** | Harmonic mean | Care about both |
| **AUC** | Area under ROC | Compare classifiers |

**Regression Metrics:** R-squared, RMSE, MAE

**Related:** [[Confusion-Matrix]], [[ROC-Curve]], [[Precision-Recall]]

---

## AWS Services

### [[SageMaker-AMT]]

**Automatic Model Tuning (Hyperparameter Optimization)**

**Purpose:** Find optimal hyperparameters automatically

**How It Works:**
1. Define hyperparameters and ranges
2. Define objective metric
3. SageMaker spins up tuning jobs
4. Learns as it goes (doesn't try every combination)

**Approaches:**
| Approach | Best For |
|----------|----------|
| Grid Search | Categorical only |
| Random Search | Fully parallelizable |
| Bayesian | Learns from prior runs |
| Hyperband | Iterative algorithms (fastest) |

**Features:** Early stopping, Warm start, Resource limits

**Related:** [[Hyperparameter-Tuning]], [[SageMaker-Autopilot]]

---

### [[SageMaker-Autopilot]]

**AutoML - Fully Automated ML Pipeline**

**Automates:** Algorithm selection, preprocessing, tuning, infrastructure

**Problem Types:** Binary classification, Multi-class, Regression

**Training Modes:**
| Mode | Description |
|------|-------------|
| HPO | Bayesian (<100MB) or Multi-fidelity (>100MB) |
| Ensembling | AutoGluon stacking (10 trials) |
| Auto | Ensembling <100MB, HPO >100MB |

**Integrates with:** [[SageMaker-Clarify]] for explainability (SHAP values)

**Related:** [[AMT]], [[SageMaker-Clarify]], [[SHAP]]

---

### [[SageMaker-Studio]]

**Visual IDE for ML**

**Components:**
- [[SageMaker-Notebooks]] - Jupyter notebooks with dynamic hardware
- [[SageMaker-Experiments]] - Track and compare ML jobs
- [[SageMaker-Debugger]] - Monitor training, detect issues
- [[SageMaker-Model-Registry]] - Version and deploy models
- [[TensorBoard]] - Visualization integration

**Related:** [[Jupyter]], [[MLOps]]

---

### [[SageMaker-Debugger]]

**Monitor and Debug Training Jobs**

**Features:**
- Save internal state at intervals (gradients, tensors)
- Define rules for unwanted conditions
- CloudWatch events on rule triggers
- Auto-generated training reports

**Built-in Rules:** CPUBottleneck, GPUMemoryIncrease, StepOutlier

**Actions:** StopTraining(), Email(), SMS()

**Supported:** TensorFlow, PyTorch, MXNet, XGBoost

**Related:** [[CloudWatch]], [[Training-Jobs]]

---

### [[SageMaker-Training-Compiler]]

**Hardware-Optimized Training**

- Accelerates training up to 50%
- Converts models to optimized instructions
- Tested with Hugging Face transformers
- Requires GPU instances (ml.p3, ml.p4, ml.g4dn, ml.g5)
- **NOT compatible with distributed training libraries**
- **No longer maintained**

**Related:** [[Deep-Learning-Containers]], [[Hugging-Face]]

---

### [[SageMaker-Distributed-Training]]

**Scale Training Across Multiple GPUs/Instances**

**Types of Parallelism:**
| Type | What's Distributed | Use Case |
|------|-------------------|----------|
| Data Parallelism | Training data | Large datasets |
| Model Parallelism | Model itself | >1B parameters |
| Job Parallelism | Training jobs | Hyperparameter tuning |

**Best Practice:** Max out single instance before multiple instances

**Related:** [[SageMaker-DDP]], [[SageMaker-MPP]], [[EFA]]

---

### [[SageMaker-DDP]]

**Distributed Data Parallelism Library**

**Collectives:**
- AllReduce: Distribute gradient computation
- AllGather: Inter-node communication

**Config:** `backend="smdpp"`, `smdistributed.dataparallel`

**NOT compatible with:** Training Compiler

**Related:** [[PyTorch-DDP]], [[Horovod]], [[DeepSpeed]]

---

### [[SageMaker-MPP]]

**Model Parallelism Library (for LLMs >1B parameters)**

**Features:**
| Feature | Trade-off |
|---------|-----------|
| Optimization State Sharding | Requires Adam/fp16 |
| Activation Checkpointing | Memory vs. compute |
| Activation Offloading | Memory vs. I/O |

**Framework:** PyTorch only

**Related:** [[LLM-Training]], [[Sharded-Data-Parallelism]], [[MiCS]]

---

### [[Training-Infrastructure]]

**Warm Pools:**
- Retain infrastructure for repeated training
- Set `KeepAlivePeriodInSeconds`
- Requires service limit increase

**Checkpointing:**
- Snapshots during training
- Auto-sync with S3
- Define `checkpoint_s3_uri`

**Health Checks (ml.g/ml.p instances):**
- GPU health monitoring
- NCCL verification
- Automatic instance replacement

**Related:** [[S3]], [[EC2-Instances]]

---

### [[EC2-GPU-Instances]]

| Instance | Hardware | Use Case |
|----------|----------|----------|
| **P3** | 8x Tesla V100 | Training |
| **P4d** | A100 UltraClusters | Supercomputing |
| **P4de** | A100 (80GB, 400Gbps) | Trillion-parameter |
| **Trn1/Trn1n** | AWS Trainium | Training (50% savings) |
| **Inf2** | AWS Inferentia2 | Inference |
| **G3/G5g** | M60/T4G | Graphics/ML |

**Related:** [[EFA]], [[Distributed-Training]]

---

### [[EFA]]

**Elastic Fabric Adapter**

**Purpose:** HPC-like network performance in cloud

**Requirements:**
- NVidia GPUs
- NCCL (NVidia Collective Communication Library)

**Setup:**
- Include NCCL, EFA, AWS OFI NCCL plugin
- Set `FI_PROVIDER="efa"`

**Related:** [[Distributed-Training]], [[P4de-Instances]]

---

## Concept Relationships

```
                    ┌─────────────────────────────────────────┐
                    │         DEEP LEARNING                   │
                    └─────────────────┬───────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          │                           │                           │
          v                           v                           v
   ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
   │     CNN      │          │   RNN/LSTM   │          │ Transformers │
   │   (Images)   │          │  (Sequences) │          │    (NLP)     │
   └──────────────┘          └──────────────┘          └──────────────┘
                                                                │
                                                                v
                                                       ┌──────────────┐
                                                       │Transfer Learn│
                                                       │  (BERT,GPT)  │
                                                       └──────────────┘

   ┌────────────────────────────────────────────────────────────────────┐
   │                        TRAINING PIPELINE                           │
   └────────────────────────────────────────────────────────────────────┘
          │                           │                           │
          v                           v                           v
   ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
   │  Tuning      │          │ Regularization│         │  Evaluation  │
   │ (AMT,HPO)    │          │(Dropout,L1/L2)│         │(Metrics,ROC) │
   └──────────────┘          └──────────────┘          └──────────────┘

   ┌────────────────────────────────────────────────────────────────────┐
   │                      SAGEMAKER ECOSYSTEM                           │
   └────────────────────────────────────────────────────────────────────┘
          │                           │                           │
          v                           v                           v
   ┌──────────────┐          ┌──────────────┐          ┌──────────────┐
   │Studio/Debug  │          │  Autopilot   │          │ Distributed  │
   │  Notebooks   │          │   (AutoML)   │          │  Training    │
   └──────────────┘          └──────────────┘          └──────┬───────┘
                                                              │
                                      ┌───────────────────────┼───────┐
                                      │                       │       │
                                      v                       v       v
                               ┌──────────────┐        ┌─────────┐ ┌─────┐
                               │     DDP      │        │   MPP   │ │ EFA │
                               │(Data Parallel)│       │(Model)  │ │     │
                               └──────────────┘        └─────────┘ └─────┘
```

---

## Exam Tips

### Neural Networks
- ReLU is default for hidden layers; Softmax for multi-class output
- Vanishing gradient: use LSTM, ResNet, or ReLU
- CNN for images, RNN for sequences, Transformers for modern NLP

### Tuning & Regularization
- Small batch sizes help escape local minima
- Large learning rates overshoot optimal solution
- Dropout prevents overfitting by removing neurons during training
- L1 = sparse (feature selection), L2 = dense

### Evaluation Metrics
- High recall = few false negatives (fraud, cancer detection)
- High precision = few false positives (drug testing)
- F1 = harmonic mean when both matter
- AUC 0.5 = random, 1.0 = perfect

### SageMaker Services
- AMT learns as it goes (Bayesian/Hyperband)
- Autopilot = full AutoML pipeline
- Debugger monitors training, fires CloudWatch events
- Training Compiler: 50% faster but NOT compatible with distributed

### Distributed Training
- Scale up (bigger instance) before scaling out (more instances)
- Data parallelism: large datasets
- Model parallelism: models >1B parameters
- EFA: HPC networking with NCCL
- MiCS/Sharded: enables >1T parameters
