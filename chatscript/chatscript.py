from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

# Prime the conversation with your advisor instructions
prime = (
    "You are a Crusader Kings 3 strategy advisor who helps players make in-game decisions, "
    "especially around religion reformation and culture customization. "
    "Answer as a medieval strategist, using in-game terms and offering contextual, strategic advice.\n"
    "Player: "
)
chat_history_ids = tokenizer.encode(prime, return_tensors='pt')

print("Advisor: Greetings, noble ruler! How may I assist you?\n")
for step in range(10):
    new_user_input_ids = tokenizer.encode(input("You: ") + tokenizer.eos_token, return_tensors='pt')
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=attention_mask
    )
    print("Advisor:", tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True))