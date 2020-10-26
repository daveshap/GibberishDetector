from gpt2_client import GPT2Client


gpt2 = GPT2Client('117M')  # options: 117M, 345M, 774M, or 1558M
gpt2.load_model(force_download=False) 
# had to create a new conda environment from scratch with tensorflow-gpu 1.15, then it worked just fine.


prompts = [
  "I will not",
  #"You should",
  #"This is not the way to"
]

text = gpt2.generate_batch_from_prompts(prompts) # returns an array of generated text
print(text)