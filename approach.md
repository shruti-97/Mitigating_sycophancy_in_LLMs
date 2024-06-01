# Approach Update

## Problem Statement

Language models display sycophancy, limiting their reliability for information retrieval, QA, etc.

We aim to:
 - minimize sycophancy by use more sophisticated synthetic data interventions
 - an adversarial framework of using 2 LLMs pitted against each other to minimize sycophantic tendencies with minimal supervision

Existing work:
 - merely demonstrates an example of using synthetic data to reduce sycophancy. Does not explore sophesticated data augmentation or training loop changes

## Proposed Approach

We propose using an open LLM such as Llama/Llama 2 as our LLM.

We propose the following components:
 - A list of claims along with True/False answers to these claims
 - A misleading LLM: Role of this model is to generate biographies of prompters and other biasing information to supply along with a T/F question with a claim presented above
 - A robust LLM: Role of this model is to answer the T/F question correctly regardless of the biasing information provided to the model.
 - Loss function that penalizes misleading LLM when robust LLM answers correctly, and penalizes misleading LLM when robust LLM outputs the wrong answer.

## Key Experiment
 - Assumptions: 
    - Questions are answered with T/F only
    - Only claims for which answers are known before hand can be used.
    - Generator only fills in a template, does not generate free form text.
 - Dataset:
    - The following datasets will be used to create a list of claims, along with T/F labels attached to each claim.
        - FEVER dataset: Extract "Supports" claims at T and "Refutes" as F
        - TruthfulQA: Explode the questions and expected/best answers for T statements, and questions and wrong answers for F statements.
        - Climate-FEVER: Same treatment as FEVER
        - Politifact Factcheck dataset: Select only true and pants on fire claims as T/F statements.
    - The following data source is yet to be explored:
        - DBPedia: Wikipedia's knowledge graph. This can be used to extract precise facts based on Wikipedia data - useful since LLAMA is trained on open data like this. Advantage - virtually no limitation on cardinality of the claims set.
 - Pre-processing:
    1. Run each claim with no biasing statements through the model n times, and select only statements that are answered correctly almost 100% of the time. Model knows the ground truth for these
    2. Generate versions of each prompt with the following variations to the template:
 - Model architectures
    [TBD]
 - Implementation (libraries, code from papers, etc.)
    - Code from papers: Generation of synthetic data will build on top of Google's implementation [here](https://github.com/google/sycophancy-intervention).
    - Pre-trained model from paper: LLMS will be LLAMA models, provided freely and openly [here](https://ai.meta.com/resources/models-and-libraries/llama-downloads/).
    - GAN Implementation in PyTorch as a jumping off point
 - Metrics 
    - Accuracy score with biasing
        - K-accuracy score for statistical significance 
        - (Compare against baseline methods from Wei et al - basic synethetic data)
    - Performance of robust model on same zero-shot benchmarks as out-of-the-box LLAMA
    - Sycophancy % of Wei et al models using our trained generator
    - Produce metrics for following variations:
        - Slice and dice by source of the claim, whether ground truth answer is T/F, domain, category(misinformation, myth, conspiracy, etc.)
        - subsets of the dataset to identify failure cases

## Analysis
 - Ablations
    - Synthetic data attributes:
        - Re-order the answers
        - Place the biasing text towards the end rather than the start
        - Remove different biasisng factors in the biography (i.e., remove sex, age, profession, opinion, etc. and observe instance of sycophancy)
    - Hyperparameters
    - Loss?
 - Qualitative Analysis methods
    - Produce example prompts (claim + biographies) that:
        - Trick our model + Wei et al model (no improvement cases)
        - only our model (failure cases)
        - on Wei et al (success cases)
    - Some creative attempts by generator to trick that 
    - Examples showing unexpected biases in the model that were uncovered by the discriminator (e.g., if saying I am a physicist changes the model's answer about a sports question - humans wouln't expect this maybe such erroneous results exist)

## (Not for presentation) Timeline

Task 1: Produce synthetic data:
1. Create templates with spaces for biasing factors and claim
2. Combine source datasets into large claims database and deduplicate and collect some statistics about the nature of the data
3. If possible, explore extraction of facts from knowledge graph (KG) to use as well

Task 2: GAN training loop:
1. Get training framework up:
    - Run simple training with any basic LM to pick up implementation errors and test loss function
    - Write code to calculate the metrics we want
    - Basic implementation to monitor training health and identify any resource crunch/bottlenecks
    - Log generator prompts and other interesting data for post-hoc analysis
2. Get going with LLM:
    - Irons out any kinks in running LLAMA models locally (resource, compatibility, etc.)
    - Plug into GAN training loop

Task 3: Run experiments with all ablations

Task 4A: (If possible and required) Re-run with mistakes identified and fixed

Task 5: Analysis on why it worked/didn't work

Task 6: Write up, and wrap up


Grading information:
 - Must stick to time limit (5 mins)
 - Must upload slides on time
 - Must be clear about what we are proposing