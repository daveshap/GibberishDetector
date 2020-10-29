from gpt2_client import GPT2Client


gpt2 = GPT2Client('117M')  # options: 117M, 345M, 774M, or 1558M
gpt2.load_model(force_download=False) 

corpus = 'c:/GibberishDetector/corpus20.txt'

result = gpt2.finetune(corpus, return_text=True) # Load your custom dataset
print(result)
