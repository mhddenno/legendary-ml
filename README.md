# Let's keep Track about what is happening in the World of AI

This video covers how the bridge pattern works and why it's useful. To spice things up, I'm going to deviate from the classic definition of the pattern from the Gang-of-four book (which is already quite powerful) and show you a couple of things you can do in Python to shorten the code and at the same time allow for extra flexibility.

# Mind Overview

## Algorithms layer

### First layer

```mermaid
mindmap
  root((AI))
    Classical Machine Learning
      Topics
        Regression
        Classification
        Clustering
        Association Rule Learning
        Reinforcement Learning
        Dimensionality Reduction
        Model Selection and Boosting
      Tools
        scikit-learn
    Deep Learning
      Topics
        Generative AI
            LLMs
      Tools
        Pytorch
        Tenserflow
        LangChain
        HuggingFace
        Lamini, Ollama
    Use Cases
      Spaces in Hugging Face
      Langchain UCs
```

### second layer

```mermaid
mindmap
  root((AI))
    Classical Machine Learning
      Topics
        Regression
            Simple Linear Regression
            Multiple Linear Regression
            Polynomial Regression
            Support Vector Regression (SVR)
            Decision Tree Regression
            Random Forest Regression
        Classification
            Logistic Regression
            K-Nearest Neighbors (K-NN)
            Support Vector Machine (SVM)
            Kernel SVM
            Naive Bayes
            Decision Tree Classification
            Random Forest Classification
        Clustering
            K-Means Clustering
            Hierarchical Clustering
        Association Rule Learning
            Apriori
            Eclat
        Reinforcement Learning
            Upper Confidence Bound (UCB)
            Thompson Sampling
        Dimensionality Reduction
        Model Selection and Boosting
      Tools
        scikit-learn
    Deep Learning
      Topics
        Neural Networks and Deep Neural Networks (DNNs)
        Convolutional Neural Networks (CNNs)
        Recurrent Neural Networks (RNNs)
        Long Short-Term Memory (LSTM)
        Gated Recurrent Unit (GRU)
        Autoencoders
        Generative Adversarial Networks (GANs)
        Transfer Learning
        Meta-Learning
        Attention Mechanisms
        Reinforcement Learning
        Explainable AI (XAI)
        Quantum Machine Learning
        Capsule Networks
        Neuroevolution
        Generative AI
            LLMs
      Tools
        Pytorch
        Tenserflow
        LangChain
        HuggingFace
        Lamini, Ollama
    Use Cases
      Spaces in Hugging Face
      Langchain UCs
```

## Data layer

```mermaid
mindmap
  root((Data Preprocessing))
    Scalling
    Spliting
    Encdoding
    Evaluation  
      Confusion Matrix
      R Square
    
```

## Statistics

```mermaid
mindmap
  root((Statistics))
    P_values
    T_test
    Variance
    Bias
    Backward Elimination
```

## ML Process

```mermaid
flowchart TD
    A(Load The Data) --> B(Clean the data)
    B --> C(Split into traning & test sets)
    C --> D(Build the model)
    D --> E(Train the model)
    E --> F(Make predictions)
    F --> G(Calculate performance metrics)
    G --> H(Make a verdict)
```