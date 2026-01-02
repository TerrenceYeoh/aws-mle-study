# Section 6: Model Training, Tuning, and Evaluation - Comparison Tables

## Neural Network Comparisons

### Neural Network Types

| Type | Input | Use Case | Key Feature | Example |
|------|-------|----------|-------------|---------|
| **Feedforward** | Any | General classification | Basic architecture | Spam detection |
| **CNN** | Images/grids | Image classification | Feature-location invariant | Stop sign detection |
| **RNN** | Sequences | Time-series | Memory cells | Stock prediction |
| **LSTM** | Long sequences | NLP, music | Separate short/long-term memory | Machine translation |
| **GRU** | Long sequences | Similar to LSTM | Simplified LSTM | Same as LSTM |
| **Transformer** | Sequences | Modern NLP | Self-attention | BERT, GPT |

---

### Activation Functions

| Function | Range | Hidden Layer | Output Layer | Issue |
|----------|-------|--------------|--------------|-------|
| **ReLU** | 0 to inf | Default choice | No | Dying ReLU |
| **Leaky ReLU** | -inf to inf | When ReLU fails | No | - |
| **Sigmoid** | 0 to 1 | Rarely | Binary classification | Vanishing gradient |
| **TanH** | -1 to 1 | RNNs | No | Vanishing gradient |
| **Softmax** | 0-1 (sum=1) | No | Multi-class (single label) | - |
| **Swish** | ~-0.3 to inf | 40+ layers | No | - |

**When to Use:**
| Scenario | Recommended |
|----------|-------------|
| Multi-class output | Softmax |
| Binary output | Sigmoid |
| RNN hidden layers | TanH |
| General hidden layers | ReLU (start here) |
| ReLU not working | Leaky ReLU |
| Very deep networks | Swish |

---

### CNN Architectures

| Architecture | Year | Innovation | Use Case |
|--------------|------|------------|----------|
| **LeNet-5** | 1998 | Early CNN | Handwriting |
| **AlexNet** | 2012 | Deeper, GPU | ImageNet |
| **GoogLeNet** | 2014 | Inception modules | Classification |
| **ResNet** | 2015 | Skip connections | Very deep networks |

---

### RNN Topologies

| Topology | Input | Output | Example |
|----------|-------|--------|---------|
| **Sequence to Sequence** | Sequence | Sequence | Stock price prediction |
| **Sequence to Vector** | Sequence | Single value | Sentiment analysis |
| **Vector to Sequence** | Single value | Sequence | Image captioning |
| **Encoder-Decoder** | Sequence | Sequence | Machine translation |

---

### Transformer Models

| Model | Full Name | Size | Use Case |
|-------|-----------|------|----------|
| **BERT** | Bi-directional Encoder Representations | Large | Understanding context |
| **GPT** | Generative Pre-trained Transformer | Very large | Text generation |
| **DistilBERT** | Distilled BERT | 40% smaller | Faster inference |
| **RoBERTa** | Robustly optimized BERT | Large | Improved BERT |
| **T5** | Text-to-Text Transfer Transformer | Varies | Multi-task NLP |

---

## Training & Tuning Comparisons

### Transfer Learning Approaches

| Approach | Modify Base Model | Add Layers | Learning Rate | When to Use |
|----------|-------------------|------------|---------------|-------------|
| **Fine-tune** | Yes | Optional | Very low | Pre-trained model has more data |
| **Freeze + new layers** | No | Yes | Normal | Repurpose features |
| **Both combined** | After training new | Yes | Low then lower | Best of both |
| **Retrain from scratch** | Replace | Optional | Normal | Different domain + compute |
| **Use as-is** | No | No | N/A | Training data matches |

---

### Learning Rate vs Batch Size Effects

| Parameter | Too High | Too Low | Optimal |
|-----------|----------|---------|---------|
| **Learning Rate** | Overshoot optimal | Training too slow | Balance speed & accuracy |
| **Batch Size** | Stuck in local minima | Noisy gradients | Escape local minima, stable |

**Key Exam Points:**
- Large learning rate = overshoot correct solution
- Small learning rate = slow training
- Small batch size = escape local minima
- Large batch size = may converge on wrong solution

---

### Regularization Techniques

| Technique | How It Works | When to Use | Trade-off |
|-----------|--------------|-------------|-----------|
| **Dropout** | Remove random neurons | Too many neurons/layers | Some capacity lost |
| **Early Stopping** | Stop when val acc drops | Overfitting detected | May undertrain |
| **L1 (Lasso)** | Sum of weights | Feature selection | Computationally expensive |
| **L2 (Ridge)** | Sum of squared weights | Keep all features | No feature selection |

### L1 vs L2 Regularization

| Aspect | L1 (Lasso) | L2 (Ridge) |
|--------|------------|------------|
| **Formula** | Sum(abs(weights)) | Sum(weights^2) |
| **Output** | Sparse | Dense |
| **Feature Selection** | Yes (zeros out features) | No (all features kept) |
| **Computational** | Expensive | Efficient |
| **Use When** | Want fewer features | All features important |

---

### Gradient Problems

| Problem | Symptom | Cause | Solutions |
|---------|---------|-------|-----------|
| **Vanishing** | Slow/no learning | Deep networks, sigmoid | LSTM, ResNet, ReLU |
| **Exploding** | NaN/Inf values | Large weights | Gradient clipping |

---

## Evaluation Metrics

### Classification Metrics

| Metric | Formula | Optimize When | Example |
|--------|---------|---------------|---------|
| **Recall** | TP / (TP + FN) | Minimize false negatives | Fraud detection |
| **Precision** | TP / (TP + FP) | Minimize false positives | Drug testing |
| **F1 Score** | 2(P*R)/(P+R) | Both matter | Balanced classification |
| **Specificity** | TN / (TN + FP) | Measure negative ID | Disease screening |
| **AUC** | Area under ROC | Compare classifiers | Model selection |

### Classification vs Regression Metrics

| Task | Metrics | When to Use |
|------|---------|-------------|
| **Classification** | Accuracy, Precision, Recall, F1, AUC | Discrete categories |
| **Regression** | R-squared, RMSE, MAE | Continuous values |

### ROC vs P-R Curve

| Curve | Axes | Best For |
|-------|------|----------|
| **ROC** | TPR vs FPR | General classification |
| **P-R** | Precision vs Recall | Information retrieval, imbalanced data |

---

## Ensemble Methods

### Bagging vs Boosting

| Aspect | Bagging | Boosting |
|--------|---------|----------|
| **Training** | Parallel | Sequential |
| **Sampling** | Random with replacement | Weighted observations |
| **Learning** | Independent | Each learns from previous |
| **Accuracy** | Good | Generally better |
| **Overfitting** | Avoids | Can overfit |
| **Parallelization** | Easy | Harder |
| **Example Algorithm** | Random Forest | XGBoost |

---

## Hyperparameter Tuning

### Tuning Approaches

| Approach | How It Works | Parallelization | Best For |
|----------|--------------|-----------------|----------|
| **Grid Search** | Try every combination | N/A | Categorical only, small space |
| **Random Search** | Random combinations | Fully parallel | Large search spaces |
| **Bayesian** | Learn from prior runs | Limited | Continuous parameters |
| **Hyperband** | Dynamic resources, early stop | Parallel | Neural networks (fastest) |

---

## SageMaker Service Comparisons

### SageMaker Training Features

| Feature | Purpose | When to Use |
|---------|---------|-------------|
| **AMT** | Hyperparameter tuning | Find optimal hyperparameters |
| **Autopilot** | Full AutoML | Quick baseline, non-experts |
| **Debugger** | Monitor training | Debug issues, profiling |
| **Experiments** | Track trials | Compare approaches |
| **Model Registry** | Version models | Production deployment |

### AMT vs Autopilot

| Aspect | AMT | Autopilot |
|--------|-----|-----------|
| **Scope** | Hyperparameters only | Full pipeline |
| **Algorithm** | You choose | Auto-selected |
| **Preprocessing** | You handle | Automated |
| **Control** | High | Low |
| **Use Case** | Fine-tune known model | Quick baseline |

### Autopilot Training Modes

| Mode | Trials | Method | Data Size |
|------|--------|--------|-----------|
| **HPO** | Up to 100 | Bayesian (<100MB), Multi-fidelity (>100MB) | Any |
| **Ensembling** | 10 | AutoGluon stacking | <100MB |
| **Auto** | Varies | HPO or Ensembling | Auto-detect |

---

## Distributed Training

### Data Parallelism vs Model Parallelism

| Aspect | Data Parallelism | Model Parallelism |
|--------|------------------|-------------------|
| **What's Split** | Training data | Model itself |
| **Use Case** | Large datasets | Models >1B parameters |
| **Communication** | Gradient sync | Activation/gradient passing |
| **Complexity** | Lower | Higher |
| **SageMaker Library** | DDP | MPP |

### Distributed Training Libraries

| Library | Provider | Frameworks | SageMaker Config |
|---------|----------|------------|------------------|
| **SageMaker DDP** | AWS | PyTorch | `smdistributed.dataparallel` |
| **SageMaker MPP** | AWS | PyTorch | `smdistributed.modelparallel` |
| **PyTorch DDP** | PyTorch | PyTorch | `pytorchddp` |
| **torchrun** | PyTorch | PyTorch | `torch_distributed` |
| **DeepSpeed** | Microsoft | PyTorch | Custom |
| **Horovod** | Uber | Both | Custom |

---

### Memory Optimization Techniques

| Technique | How It Works | Trade-off |
|-----------|--------------|-----------|
| **Activation Checkpointing** | Clear activations, recompute | Memory vs. compute |
| **Activation Offloading** | Move to CPU | Memory vs. I/O |
| **Gradient Checkpointing** | Store fewer gradients | Memory vs. compute |
| **Mixed Precision (fp16)** | 16-bit floats | Memory vs. precision |

---

## EC2 Instance Comparisons

### GPU Instance Types for ML

| Instance | Hardware | Use Case | Special Feature |
|----------|----------|----------|-----------------|
| **P3** | 8x Tesla V100 | Training | General DL |
| **P4d** | A100 UltraClusters | Large scale | High bandwidth |
| **P4de** | A100 (80GB) | Trillion params | 400 Gbps network |
| **Trn1** | AWS Trainium | Training | 50% cost savings |
| **Trn1n** | AWS Trainium | Training | 1600 Gbps |
| **Inf2** | AWS Inferentia2 | Inference | Cost-optimized |
| **G3** | M60 | Graphics/ML | General purpose |
| **G5g** | T4G | Inference | Graviton |

### When to Use Each Instance

| Need | Recommended Instance |
|------|---------------------|
| General training | P3, P4d |
| Cost-optimized training | Trn1 |
| Inference | Inf2 |
| Trillion-parameter models | P4de with EFA |
| High network bandwidth | Trn1n |

---

## Quick Decision Tables

### Which Activation Function?

| Question | Answer |
|----------|--------|
| Multi-class classification output? | Softmax |
| Binary classification output? | Sigmoid |
| General hidden layer? | ReLU |
| RNN? | TanH |
| Very deep network (40+ layers)? | Swish |

### Which Evaluation Metric?

| Question | Answer |
|----------|--------|
| False negatives are costly? | Recall |
| False positives are costly? | Precision |
| Both matter equally? | F1 Score |
| Comparing classifiers? | AUC |
| Predicting continuous values? | RMSE, R-squared |

### Which Regularization?

| Question | Answer |
|----------|--------|
| Network too complex? | Dropout |
| Want feature selection? | L1 (Lasso) |
| Keep all features? | L2 (Ridge) |
| Validation accuracy dropping? | Early Stopping |

### Which Distributed Approach?

| Question | Answer |
|----------|--------|
| Large dataset, model fits on GPU? | Data Parallelism |
| Model doesn't fit on one GPU? | Model Parallelism |
| Model >1B parameters? | SageMaker MPP |
| Need HPC networking? | EFA + NCCL |
| Trillion-parameter model? | MiCS/Sharded + P4de |
