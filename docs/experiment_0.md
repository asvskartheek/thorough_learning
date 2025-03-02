# Experiment 0 [WIP]
data to use: extracted json format for 6th chapter ncert maths textbook [here](../data/extracted_jsons/math_11_ch6_pnc_att3.json)
base model: [DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)

models to try:
- base model score on the exercises (no additional prompt), just follow the [recommended settings](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B#usage-recommendations)
- fine-tune the model on text+examples.
- thorough learning on text+examples.

things to keep track of for base model:
- raw generations on exercises
- accuracy on exercises

things to keep track for ft:
- raw generations on exercises (after every epoch)
- accuracy on exercises (after every epoch)
- train_loss

things to keep track for thorough learning:
- raw generations on exercises (after every epoch)
- accuracy on exercises (after every epoch)
- train_loss (during ft)
- train_loss (during rl)


evaluation:
- accuracy on the exercises.