# Thorough Learning

FOR UPTO DATE VERSION REFER [NOTION](https://www.notion.so/Thorough-Learning-1a874b2efdb7804dab67d7076e52ec76)

People learn in different stages from the main text they learn by memorisation. With the example workouts, they learn new thought processes — how to piece together new information and apply to solving a problem. Then we practice problem solving skills with just the reference answer in the exercises.

For the first part it will be an auto-regressively trained LoRA. Examples and exercises must be trained using GPRO (RL). We must choose a very strong base model, based on the evidence from R1 paper that RL failed due to bad models in the first place. Maybe we can even choose R1 as the base model. We are calling this method **Thorough Learning**. 

Thereby dividing a model’s post training into 2 parts:

- autoregressive FT on chapter texts as a parallel for memorisation
- RL on examples and exercises, as a parallel for problem solving.

**Few brainstorming ideas**

- For the first attempt, use DeepSeek-R1 thinking format:
```
<think>
</think>
```
we will do simple FT for auto-regression and GRPO like deep-seek r1 did, for the RL training

- Change the standard reasoning prompt to the following way:

```html
r1s thinking prompt format structure for getting the format reward:
<think>
</think>

idea 1:
<think>
<attempt 1>
</attempt 1>

<attempt 2>
</attempt 2>
:
:
:
</think>
```

- maybe add an inversely related to number of attempts to the overall reward.
- introduce a new type of step call it verification step.
- play with number of `max_attempts` as a hyper-parameter during inference.

**Intuition**

Based on usage of R1. It repeatedly using alternatively and give another attempt to solve the problem.

**Dataset requirement**

It should have 3 parts:

1. Chapter text
2. Solved examples of the chapter
3. Exercises with the final answer

**Benchmarking datasets**

- datasets used in R1
    - AIME 2024
    - MATH 500
    - **To-Do [Research]**
    - OpenAI extracted dataset names
        - Knowledge‐Based Datasets
            - MMLU (Hendrycks et al., 2020)
            - MMLU-Redux (Gema et al., 2024)
            - MMLU-Pro (Wang et al., 2024)
            - C-Eval (Huang et al., 2023)
            - CMMLU (Li et al., 2023)
            - IFEval (Zhou et al., 2023)
            - FRAMES (Krishna et al., 2024)
            - GPQA Diamond (Rein et al., 2023)
            - SimpleQA (OpenAI, 2024c)
            - C-SimpleQA (He et al., 2024)
            - AlpacaEval 2.0 (Dubois et al., 2024)
            - Arena-Hard (Li et al., 2024)
        - Problem‐Solving Datasets
            - SWE-Bench Verified (OpenAI, 2024d)
            - Aider 1
            - LiveCodeBench (Jain et al., 2024)
            - Codeforces
            - Chinese National High School Mathematics Olympiad (CNMO 2024)
            - American Invitational Mathematics Examination 2024 (AIME 2024) (MAA, 2024)
            - MATH-500
- For benchmarking the learning methods, we need to find good datasets maybe NCERT with problems to be solved are JEE?

**To-do [RESEARCH]: find good benchmark dataset for this.**

**Ablation Studies**

1. Baselines
    1. base model performance
    2. model + FT (on chapter text+examples. not including exercises, bcs they do have solution)
2. We should probably create multiple LoRAs.
    1. Only memorisation score
    2. Memorisation + RL score
    3. only RL score
3. Try different combinations number of examples and excercises and study their effect on the performance.
4. Checkout the activation maps of the LoRA and RL’s LoRa?
    1. **To-do [LEARN]: how to do plug and play with RL models? Does LoRa also work when trained with RL?**
    2. **Hypothesis**: for questions based on memorisation LoRA should have brighter heatmap, for problem solving questions RL should have brighter heatmap

- **Product related ideas**
    - An online hosted LLM which is served by us, with plug and play LoRAs.
    - They can create their own LoRAs by uploading textbook in the format of text, examples and exercises.
    - Maybe another add-on feature is just upload a textbook we will convert it to a data format needed for **Thorough Learning**.
    - All the LoRAs people create must be completely open and free to everyone in the world. **#KnowledgeMustBeCompletelyOpen**
    - Any private models need to be trained by self hosted servers only.